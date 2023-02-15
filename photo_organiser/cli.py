"""Console script for photo_organiser."""
import sys
import click


@click.command()
@click.option('--input_path', help='Number of greetings.')
@click.option('--output_path', help='The person to greet.')
def main(input_path: str, output_path: str) -> None:
    print('Entra por aquí')


if __name__ == "__main__":
    main()  # pragma: no cover