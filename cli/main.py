import argparse

from .commands import AddCommand, CreateCommand, ViewCommand, OrganiseCommand


def execute():
    parser = argparse.ArgumentParser(description="A CLI for your second brain")
    subparsers = parser.add_subparsers(dest="command")

    commands = [
        AddCommand(subparsers),
        CreateCommand(subparsers),
        ViewCommand(subparsers),
        OrganiseCommand(subparsers),
    ]

    args = parser.parse_args()

    for command in commands:
        if command.execute_args(args):
            return

    parser.print_help()

execute()