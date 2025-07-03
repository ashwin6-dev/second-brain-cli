from core.services.note_service import add_file

class AddCommand:
    def __init__(self, subparsers):
        self.parser = subparsers.add_parser("add", help="Add a new note")
        self.parser.add_argument("filepath", type=str,
                                help="The filepath of the note you want to add to your second brain")

    def execute_args(self, args):
        if args.command == 'add':
            add_file(args.filepath)
            return True

        return False