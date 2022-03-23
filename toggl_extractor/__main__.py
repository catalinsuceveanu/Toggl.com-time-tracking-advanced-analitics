import click

from toggl_extractor import processor
from toggl_extractor import client


@click.group()
def cli():
    pass


@click.command()
@click.option(
    "--range",
    "--r",
    default=2,
    prompt="no. of days",
    help="the number of past days you want to check, starting from yesterday",
)
def workdays(range):

    result = processor.get_workdays_for_users_per_day(range)
    for day in result:
        print(day + ":" + "\n")
        for person in result[day]:
            print(person + ": " + result[day][person])
        print("\n\n")


cli.add_command(workdays)


if __name__ == "__main__":
    cli()
