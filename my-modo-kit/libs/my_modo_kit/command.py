from typing import List, Optional
from operator import ior
from functools import reduce

from lx import symbol
from lxu.command import BasicCommand


class KitCommand(BasicCommand):
    """Command wrapper to add an index return when adding an argument."""
    arg_index = 0

    def add_arg(
            self, name: str, arg_type: str, optional: bool = False, query: bool = False,
            flags: List[int] = None
    ) -> int:
        """Adds an argument to the command and returns its index.

        Args:
            name (str): The name of the argument.
            arg_type (str): The string type of the argument.
            optional (bool): If the argument is optional.
            query (bool): If the argument is queryable.
            flags (List[int]): List of flags.

        Returns:
            current_index (int): The index of the newly added argument.
        """
        self.dyna_Add(name, arg_type)
        current_index = self.arg_index

        # If we have a list of flags, use that, otherwise create a new list.
        flags = flags if flags else list()
        # Since optional and query are the most common, we just require a bool.
        if optional:
            flags.append(symbol.fCMDARG_OPTIONAL)
        if query:
            flags.append(symbol.fCMDARG_QUERY)

        # Add flags to argument. reduce with ior == flag | flag | ...
        if flags:
            self.dyna_SetFlags(current_index, reduce(ior, flags))
        # Increment index for the next argument.
        self.arg_index += 1

        return current_index
