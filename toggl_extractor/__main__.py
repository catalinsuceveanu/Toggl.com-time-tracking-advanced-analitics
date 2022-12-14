import click
from toggl_extractor import processor
from toggl_extractor import slack_client
from toggl_extractor import toggl_client


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
    if toggl_client.check_toggl_api_settings():
        result = processor.get_workdays_for_users_per_day(range)
        if slack:
            slack_client.post_to_slack(result)
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
    if toggl_client.check_toggl_api_settings():
        result = str()
        if user:
            if useraverage:
                result = processor.get_avrg_efficiency_of_set_user_in_range(range, user)
            else:
                result = processor.get_efficiency_of_set_user_per_day(range, user)
        else:
            if useraverage:
                result = processor.get_avrg_efficiency_per_user_in_range(range)
            else:
                result = processor.get_efficiency_percentage_per_user_per_day(range)

        if slack:
            slack_client.post_to_slack(result)
        else:
            print(result)


cli.add_command(workdays)
cli.add_command(efficiency)


if __name__ == "__main__":
    cli()
