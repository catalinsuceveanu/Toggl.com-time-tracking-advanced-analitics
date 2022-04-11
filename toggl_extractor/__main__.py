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
@click.option("--slack", is_flag=True)
def workdays(range, slack):
    result = processor.get_workdays_for_users_per_day(range, slack)
    if slack:
        print("The output for the required days was posted on slack")
    else:
        print(result)


@click.command()
@click.option(
    "--range",
    "--r",
    default=2,
    help="the number of past days you want to check, starting from yesterday",
)
@click.option("--slack", is_flag=True)
@click.option("--useraverage", is_flag=True)
@click.option("--user", help="who is the user for which you want to see the report")
def efficiency(range, slack, useraverage, user):
    result = str()
    if not useraverage and not user:
        result = processor.get_efficiency_percentage_per_user_per_day(range, slack)
    if useraverage and not user:
        result = processor.get_average_efficiency_per_user_in_range(range, slack)
    if user and not useraverage:
        result = processor.get_efficiency_of_set_user_per_day(range, user, slack)
    if slack:
        print("The output for the required days was posted on slack")
    else:
        print(result)


cli.add_command(workdays)
cli.add_command(efficiency)


if __name__ == "__main__":
    cli()
