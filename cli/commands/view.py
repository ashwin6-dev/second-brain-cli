from core.services.category_service import view_category

class ViewCommand:
    def __init__(self, subparsers):
        self.parser = subparsers.add_parser("create", help="Add a new note")
        self.parser.add_argument("category", type=str, help="The category to view - inbox, project, area, resource, archive")

    def execute_args(self, args):
        if args.command == 'view':
            view_category(args.category)
            return True

        return False