import click

<<<<<<< HEAD
import processor
=======
from toggl_extractor import processor
>>>>>>> e2b229ab2c5cc96bf30d0a74dfc99197531cfd2d

help = "workdays = this command gives the toal worked hours of the employees inluding breaks smaller than 30 mins.Considering that in a 10 minutes break one is still in a work mindset and still solving problems, even if actually smoking / snacking / eating \f test = prints this is a test\f"


@click.group()
def cli():
    pass


@click.command()
@click.option(
    "--range",
    "-r",
    default=2,
    prompt="no. of days",
    help="the number of past days you want to check, starting from yesterday",
)
def workdays(range):

    result = processor.get_workdays_for_users_per_day(range)

    # processor.print_times(range)


cli.add_command(workdays)


if __name__ == "__main__":
    cli()
