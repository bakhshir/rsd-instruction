import click
import github3


@click.group()
def cli():
    pass


@cli.command()
@click.argument('organization')
def repositories_of_organization(organization):
    """List of repositories in a GitHub organization"""
    gh = github3.GitHub()
    org = gh.organization(organization)
    for repo in org.repositories('public'):
        print(repo)


if __name__ == '__main__':
    cli()
