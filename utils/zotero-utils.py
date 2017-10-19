import click
from pyzotero.zotero import Zotero


@click.group()
def cli():
    pass


@cli.command()
@click.option('--library_id', type=str, required=True)
@click.option('--library_type', type=str, default='group', required=True)
@click.option('--api_key', type=str, required=True)
@click.option('--collection_id', type=str, required=True)
@click.argument('titles_fn', type=click.File('rt'))
@click.argument('new_item_type')
def item_type(library_id, library_type, api_key, collection_id, titles_fn, new_item_type):
    """Changes the item type of each item with a title in titles file"""
    titles = set()
    for line in titles_fn:
        title = line.strip()
        titles.add(title)
    zot = Zotero(library_id, library_type, api_key)
    items = zot.collection_items(collection_id)
    for item in items:
        if item['title'] in titles:
            item['itemType'] = new_item_type
            print(item)
            # Zotero.update_item(item)


if __name__ == '__main__':
    cli()
