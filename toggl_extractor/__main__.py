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
@click.option("--slack")
def workdays(range, slack):

    result = processor.get_workdays_for_users_per_day(range)
    if slack:
        message = str()
        for day in result:
            message = message + str(day + ":" + "\n")
            for person in result[day]:
                message = message + str(person + ": " + result[day][person] + "\n")
            message = message + str("\n\n")
        processor.print_output_to_slack(message)
    else:
        for day in result:
            print(day + ":" + "\n")
            for person in result[day]:
                print(person + ": " + result[day][person])
            print("\n\n")


cli.add_command(workdays)


if __name__ == "__main__":
    cli()
