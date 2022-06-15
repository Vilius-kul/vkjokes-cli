import click
from pydantic import ValidationError

from clients import JokeManager
from src.schemas import VkJokesParams


@click.group()
def cli():
    """Welcome to the jokes CLI!\n
    This script returns jokes!
    """
    pass


@click.command()
@click.option("--count", default=1, help="--count <int> number of jokes")
@click.option("--lang", help="--lang <lt,pl,da or ru>")
def random(count: int, lang: str):
    """Returns  1 random Joke!\n
    [OPTIONS] out --count and --lang"""
    if lang is None:
        for_validation = {"count": count}  # click.option if no input, returns None
    else:
        for_validation = {"count": count, "lang": lang}

    try:
        validated = VkJokesParams(**for_validation)
    except ValidationError as exc:
        click.echo(str(exc))
        return

    joke_manager = JokeManager(validated.count, validated.lang)
    fetched_jokes = joke_manager.fetch_jokes()
    for joke in fetched_jokes:
        click.echo(joke)


cli.add_command(random)
