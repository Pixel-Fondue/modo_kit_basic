# -- Python standard imports --
# -- Modo specific imports --
from lx import bless, symbol
from lxu.object import Message
# -- Kit specific imports --
from my_modo_kit import KIT_ABV
from my_modo_kit.command import KitCommand
from my_modo_kit.greeting import greet

# Define the name of the command
COMMAND_NAME = f"{KIT_ABV}.name"


class MyKitCommand(KitCommand):
    """Example command using KitCommand

    Examples:
        macro: "mmk.name name:ModoNaught"
        command: lx.command("mmk.name", name="ModoNaught")
    """

    def __init__(self):
        """Initialization of the kit command."""
        super(MyKitCommand, self).__init__()
        # Add the name argument for the user to input their name
        self.index_name = self.add_arg("name", symbol.sTYPE_STRING, optional=True)

    def cmd_Flags(self) -> int:
        """Modo Override: Set the internal flags of the command.

        Returns:
            (int): The command flags
        """
        return symbol.fCMD_UNDO

    def basic_Execute(self, msg: Message, flags: int) -> None:
        """Modo Override: Method that is run when the command is called.

        Args:
            msg (Message): The commands message object
            flags (int): The int result of cmd_Flags()
        """
        name = self.dyna_String(self.index_name, None)
        # Pass any processing to another function outside the command class
        greet(name)


# Bless the command with a name so that Modo can register it.
bless(MyKitCommand, COMMAND_NAME)
