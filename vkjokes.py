import requests

import click

base_url = 'http://127.0.0.1:5000/'


@click.group()
def cli():
    """Welcome to the jokes CLI!\n
        This script returns jokes!
    """
    pass

@click.command()
def random_joke():
    endpoint = 'random-joke'
    url = base_url + endpoint
    r = requests.get(url)
    click.echo(r.text)
    
@click.command()
def random_5_jokes():
    endpoint = 'random-5-jokes'
    url = base_url + endpoint
    r = requests.get(url)
    click.echo(r.text)
    
@click.command()
@click.option('--count', default=1, help='type --count <number of jokes>')
def multi_random_jokes(count):
    endpoint = 'multi-random-jokes'
    url = base_url + endpoint
    payload = {'count': count}
    r = requests.get(url, params=payload)
    click.echo(r.text)
    
    
@click.command()
@click.option('--count', default=1, help="--count <number of jokes>")
@click.argument('lang')
def multi_language_jokes(count, lang):
    endpoint = 'multi-language-jokes'
    url = base_url + endpoint
    payload = {'count': count,'language':lang}
    r = requests.get(url, params=payload)
    click.echo(r.text)
    
cli.add_command(random_joke)
cli.add_command(random_5_jokes)
cli.add_command(multi_random_jokes)
cli.add_command(multi_language_jokes)