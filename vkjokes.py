import click

@click.group()
def cli():
    """Welcome to the jokes CLI!"""
    pass

@click.command()
def random_joke():
    click.echo("1 randm joke!")
    
@click.command()
def random_5_jokes():
    click.echo("5 random jokes!")
    
@click.command()
def multi_random_jokes():
    click.echo("Multiple random jokess!")
    
@click.command()
def multi_language_jokes():
    click.echo("Multiple language jokes!")
    
cli.add_command(random_joke)
cli.add_command(random_5_jokes)
cli.add_command(multi_random_jokes)
cli.add_command(multi_language_jokes)