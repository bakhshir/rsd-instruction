import click
import requests
import json

ZENODO_API = 'https://zenodo.org/api/'


@click.group()
def zenodo():
    pass


def fetch_depositions(url, access_token):
    response = requests.get(url, params={'access_token': access_token})
    response.raise_for_status()
    page = response.json()
    for deposit in page:
        yield deposit
    if 'next' in response.links:
        next_url = response.links['next']['url']
        for deposit in fetch_depositions(next_url, access_token):
            yield deposit


@zenodo.command()
@click.argument('access_token')
def depositions(access_token):
    """Retrieve all Zenodo depositions belonging to owner of token"""
    url = ZENODO_API + 'deposit/depositions/?status=published&sort=mostrecent'
    data = [d for d in fetch_depositions(url, access_token)]
    print(json.dumps(data, indent=2))


def by_organisation(deposition, organization):
    has_related = 'related_identifiers' in deposition['metadata']
    if not has_related:
        return False
    ris = deposition['metadata']['related_identifiers']
    org_id = 'https://github.com/' + organization
    return any([ri['identifier'].startswith(org_id) for ri in ris])


@zenodo.command()
@click.argument('depositions', type=click.File('rt'))
@click.option('--organization', help='Filter on GitHub organization')
def dois(depositions, organization):
    """DOI of for each deposition"""
    for deposition in json.load(depositions):
        if by_organisation(deposition, organization):
            print(deposition['doi_url'])


@zenodo.command()
@click.argument('depositions', type=click.File('rt'))
@click.option('--organization', help='Filter on GitHub organization')
def titles(depositions, organization):
    """Title of for each deposition"""
    for deposition in json.load(depositions):
        if by_organisation(deposition, organization):
            print(deposition['title'])


if __name__ == '__main__':
    zenodo()
