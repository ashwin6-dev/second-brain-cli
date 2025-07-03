from core.services.category_service import organise_note

class OrganiseCommand:
    def __init__(self, subparsers):
        self.parser = subparsers.add_parser("organise", help="Add a new note")
        self.parser.add_argument("filename", type=str, help="Name of file/note in inbox")
        self.parser.add_argument("category", type=str, help="The category you want the note to go in")
        self.parser.add_argument("folder", type=str, help="The folder you want the note to go in")

    def execute_args(self, args):
        if args.command == 'organise':
            organise_note(args.filename, args.category, args.folder)
            return True

        return False