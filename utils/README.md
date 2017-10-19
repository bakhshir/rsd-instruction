Utilities to help add items to Zotero.

# Install

```bash
pip install -r requirements.txt
```

# Add all GitHub releases of a GitHub organization to Zotero

```bash
python zenodo-utils.py depositions <zenodo_token> > depositions.json
python zenodo-utils.py dois --organization 3D-e-Chem depositions.json > dois.txt
``` 

In Zotero app paste contents of `dois.txt`.


TODO Set item type
```bash
python zenodo-utils.py titles --organization 3D-e-Chem depositions.json  > titles.txt
python zotero-utils.py item_type ...
```
