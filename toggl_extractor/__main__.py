import click
from toggl_extractor import processor


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
@click.option("--slack", default=False)
def workdays(range, slack):
    result = processor.get_workdays_for_users_per_day(range, slack)
    if slack:
        print("The output for the required days was posted on slack")
    else:
        print(result)


cli.add_command(workdays)


if __name__ == "__main__":
    cli()
