from clients import JokeManager
from src.schemas import VkJokesParams
from pydantic import ValidationError

import click

@click.group()
def cli():
    """Welcome to the jokes CLI!\n
        This script returns jokes!
    """
    pass

@click.command()
@click.option('--count',default=1, help='--count <int> number of jokes')
@click.option('--lang',default='',help='--lang <lt,pl,da or ru>')
def random(count, lang):
    """Returns  1 random Joke!\n
    [OPTIONS] out --count and --lang """
    for_validation = {"count":count, "lang":lang}
    try:
        validated = VkJokesParams(**for_validation)
        joke_manager = JokeManager(validated.count,validated.lang)
        fetched_jokes =joke_manager.fetch_jokes()
        for joke in fetched_jokes:
            click.echo(joke)  
    except ValidationError as exc:
        click.echo(str(exc))    
         
    # joke_manager = JokeManager(validated.count, lang)
    # fetched_jokes =joke_manager.fetch_jokes(validated.count, lang)
    # for joke in fetched_jokes:
    #     click.echo(joke)
    
cli.add_command(random)
