import processor
import click

help = "workdays = this command gives the toal worked hours of the employees inluding breaks smaller than 30 mins.Considering that in a 10 minutes break one is still in a work mindset and still solving problems, even if actually smoking / snacking / eating \f test = prints this is a test\f"


@click.command()
@click.option("--option", help=help)
@click.option(
    "--range",
    default=2,
    prompt="no. of days",
    help="the number of past days you want to check, starting from yesterday",
)
def main(option, range):
    if option == "workdays":
        processor.print_times(range)
    elif option == "test":
        print("this is a test")


if __name__ == "__main__":
    main()
