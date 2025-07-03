from core.services.category_service import create_category_folder

class CreateCommand:
    def __init__(self, subparsers):
        self.parser = subparsers.add_parser("create", help="Add a new note")
        self.parser.add_argument("category", type=str, help="The PARA category the folder goes under")
        self.parser.add_argument("folder_name", type=str, help="The name of the folder you want to add")

    def execute_args(self, args):
        if args.command == 'create':
            create_category_folder(args.category, args.folder_name)
            return True

        return False