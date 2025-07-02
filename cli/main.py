import argparse

from .commands import add

parser = argparse.ArgumentParser(description="A CLI for your second brain")

subparsers = parser.add_subparsers(dest="command")

# Add command
add_parser = subparsers.add_parser("add", help="Add a new note")
add_parser.add_argument("filepath", type=str, help="The filepath of the note you want to add to your second brain")

args = parser.parse_args()

if args.command == "add":
    add(args.filepath)
else:
    parser.print_help()
