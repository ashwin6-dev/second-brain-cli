from core.services.category_service import view_category
from rich.console import Console

console = Console()

class ViewCommand:
    def __init__(self, subparsers):
        self.parser = subparsers.add_parser("view", help="Add a new note")
        self.parser.add_argument("category", type=str, help="The category to view - inbox, project, area, resource, archive")

    def execute_args(self, args):
        if args.command == 'view':
            category = args.category
            console.print(f'[blue][bold]Viewing contents of "{category}":[/bold][/blue]')

            for item in view_category(args.category):
                if item['is_folder']:
                    console.print(f'[green]> {item['name']}[/green]')
                else:
                    console.print(f'> {item['name']}')

            return True

        return False