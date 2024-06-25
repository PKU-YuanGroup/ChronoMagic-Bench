# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.


import json
import dataclasses
import numpy as np
from dataclasses import Field, MISSING
from typing import IO, TypeVar, Type, get_args, get_origin, Union, Any, Tuple

_X = TypeVar("_X")


def load_dataclass(f: IO, cls: Type[_X], binary: bool = False) -> _X:
    """
    Loads to a @dataclass or collection hierarchy including dataclasses
    from a json recursively.
    Call it like load_dataclass(f, typing.List[FrameAnnotationAnnotation]).
    raises KeyError if json has keys not mapping to the dataclass fields.

    Args:
        f: Either a path to a file, or a file opened for writing.
        cls: The class of the loaded dataclass.
        binary: Set to True if `f` is a file handle, else False.
    """
    if binary:
        asdict = json.loads(f.read().decode("utf8"))
    else:
        asdict = json.load(f)

    # in the list case, run a faster "vectorized" version
    cls = get_args(cls)[0]
    res = list(_dataclass_list_from_dict_list(asdict, cls))

    return res


def _resolve_optional(type_: Any) -> Tuple[bool, Any]:
    """Check whether `type_` is equivalent to `typing.Optional[T]` for some T."""
    if get_origin(type_) is Union:
        args = get_args(type_)
        if len(args) == 2 and args[1] == type(None):  # noqa E721
            return True, args[0]
    if type_ is Any:
        return True, Any

    return False, type_


def _unwrap_type(tp):
    # strips Optional wrapper, if any
    if get_origin(tp) is Union:
        args = get_args(tp)
        if len(args) == 2 and any(a is type(None) for a in args):  # noqa: E721
            # this is typing.Optional
            return args[0] if args[1] is type(None) else args[1]  # noqa: E721
    return tp


def _get_dataclass_field_default(field: Field) -> Any:
    if field.default_factory is not MISSING:
        # pyre-fixme[29]: `Union[dataclasses._MISSING_TYPE,
        #  dataclasses._DefaultFactory[typing.Any]]` is not a function.
        return field.default_factory()
    elif field.default is not MISSING:
        return field.default
    else:
        return None


def _dataclass_list_from_dict_list(dlist, typeannot):
    """
    Vectorised version of `_dataclass_from_dict`.
    The output should be equivalent to
    `[_dataclass_from_dict(d, typeannot) for d in dlist]`.

    Args:
        dlist: list of objects to convert.
        typeannot: type of each of those objects.
    Returns:
        iterator or list over converted objects of the same length as `dlist`.

    Raises:
        ValueError: it assumes the objects have None's in consistent places across
            objects, otherwise it would ignore some values. This generally holds for
            auto-generated annotations, but otherwise use `_dataclass_from_dict`.
    """

    cls = get_origin(typeannot) or typeannot

    if typeannot is Any:
        return dlist
    if all(obj is None for obj in dlist):  # 1st recursion base: all None nodes
        return dlist
    if any(obj is None for obj in dlist):
        # filter out Nones and recurse on the resulting list
        idx_notnone = [(i, obj) for i, obj in enumerate(dlist) if obj is not None]
        idx, notnone = zip(*idx_notnone)
        converted = _dataclass_list_from_dict_list(notnone, typeannot)
        res = [None] * len(dlist)
        for i, obj in zip(idx, converted):
            res[i] = obj
        return res

    is_optional, contained_type = _resolve_optional(typeannot)
    if is_optional:
        return _dataclass_list_from_dict_list(dlist, contained_type)

    # otherwise, we dispatch by the type of the provided annotation to convert to
    if issubclass(cls, tuple) and hasattr(cls, "_fields"):  # namedtuple
        # For namedtuple, call the function recursively on the lists of corresponding keys
        types = cls.__annotations__.values()
        dlist_T = zip(*dlist)
        res_T = [
            _dataclass_list_from_dict_list(key_list, tp) for key_list, tp in zip(dlist_T, types)
        ]
        return [cls(*converted_as_tuple) for converted_as_tuple in zip(*res_T)]
    elif issubclass(cls, (list, tuple)):
        # For list/tuple, call the function recursively on the lists of corresponding positions
        types = get_args(typeannot)
        if len(types) == 1:  # probably List; replicate for all items
            types = types * len(dlist[0])
        dlist_T = zip(*dlist)
        res_T = (
            _dataclass_list_from_dict_list(pos_list, tp) for pos_list, tp in zip(dlist_T, types)
        )
        if issubclass(cls, tuple):
            return list(zip(*res_T))
        else:
            return [cls(converted_as_tuple) for converted_as_tuple in zip(*res_T)]
    elif issubclass(cls, dict):
        # For the dictionary, call the function recursively on concatenated keys and vertices
        key_t, val_t = get_args(typeannot)
        all_keys_res = _dataclass_list_from_dict_list(
            [k for obj in dlist for k in obj.keys()], key_t
        )
        all_vals_res = _dataclass_list_from_dict_list(
            [k for obj in dlist for k in obj.values()], val_t
        )
        indices = np.cumsum([len(obj) for obj in dlist])
        assert indices[-1] == len(all_keys_res)

        keys = np.split(list(all_keys_res), indices[:-1])
        all_vals_res_iter = iter(all_vals_res)
        return [cls(zip(k, all_vals_res_iter)) for k in keys]
    elif not dataclasses.is_dataclass(typeannot):
        return dlist

    # dataclass node: 2nd recursion base; call the function recursively on the lists
    # of the corresponding fields
    assert dataclasses.is_dataclass(cls)
    fieldtypes = {
        f.name: (_unwrap_type(f.type), _get_dataclass_field_default(f))
        for f in dataclasses.fields(typeannot)
    }

    # NOTE the default object is shared here
    key_lists = (
        _dataclass_list_from_dict_list([obj.get(k, default) for obj in dlist], type_)
        for k, (type_, default) in fieldtypes.items()
    )
    transposed = zip(*key_lists)
    return [cls(*vals_as_tuple) for vals_as_tuple in transposed]
