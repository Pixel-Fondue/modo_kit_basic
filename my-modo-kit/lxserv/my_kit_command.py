# -- Python standard imports --
# -- Modo specific imports --
from lx import bless, symbol
from lxu.object import Message
# -- Kit specific imports --
from my_modo_kit import KIT_ABV
from my_modo_kit.command import KitCommand


class MyKitCommand(KitCommand):
    """Example command using KitCommand

    Examples:
        macro: "my_modo_kit name:ModoNaught"
        command: lx.command("my_modo_kit", name="ModoNaught")
    """

    def __init__(self):
        """Initialization of the kit command."""
        super(MyKitCommand, self).__init__()
        # Add arguments
        self.index_name = self.add_arg("name", symbol.sTYPE_STRING)

    def cmd_Flags(self) -> int:
        """Modo Override: Set the internal flags of the command.

        Returns:
            (int): The command flags
        """
        return symbol.fCMD_UNDO

    def basic_Execute(self, msg: Message, flags: int) -> None:
        """Modo Override: Launches the editor for the selected Python Mesh Operator.

        Args:
            msg (Message): The commands message object
            flags (int): The int result of cmd_Flags()
        """
        if self.dyna_IsSet(self.index_name):
            # The optional name has a value, lets grab it.
            name = self.dyna_String(self.index_name)
        else:
            name = "No Name"

        print(name)


# Bless the command so that Modo can register it.
bless(MyKitCommand, f"{KIT_ABV}.my_command")
