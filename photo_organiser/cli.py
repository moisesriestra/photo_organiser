"""Console script for photo_organiser."""
import sys
import click
from photo_organiser.photo_organiser import PhotoOrganiser


@click.command()
@click.option('--input_path', required=True, help='Directory that has the original images.', type=click.Path(exists=True, file_okay=False, resolve_path=True))
@click.option('--output_path', required=True, help='Directory where the result of the process will be stored.', type=click.Path(exists=True, file_okay=False, resolve_path=True))
@click.option('--remove/--no-remove', default=False, help='Set if you want to delete original images or not.')
def main(input_path: str, output_path: str, remove:bool) -> None:
    organiser = PhotoOrganiser(input_path, output_path)
    organiser.process()

if __name__ == "__main__":
    main()  