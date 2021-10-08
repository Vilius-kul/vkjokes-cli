from clients import JokeManager

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
    joke_manager = JokeManager(count, lang)
    fetched_jokes =joke_manager.fetch_jokes(count, lang)
    for joke in fetched_jokes:
        click.echo(joke)
    
cli.add_command(random)
