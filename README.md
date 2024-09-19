[![Project generated with PyScaffold](https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold)](https://pyscaffold.org)

# TEMPO
  A Cosmic Data Story about NASA's first Earth Venture Instrument mission to measure pollution of North America.

## Requirements
- Python-based Cosmic Data Stories now run on [solara](https://solara.dev).
- `tempods` requires the base [`cosmicds`](https://github.com/cosmicds/cosmicds/) to be installed.
- Developers need an API key to access the CosmicDS database. Contact the team for more information.

## Installation
- Optional but recommended, set up a new python environment.
- Install `pip` if you don't already have it.
- If you haven't already installed these packages,
```
    $ pip install solara
    $ pip install python-dotenv
```
- Pull down both the cosmicds & tempods repos.
- Inside the cosmicds folder in your terminal,
    `$ pip install -e .`
- Inside the tempods folder in your terminal,
    `$ pip install -e .`

## Running TempoDS
Inside the tempods folder in your terminal,
```
    $ CDS_API_KEY="<your api key>" solara run tempods.pages --theme-variant dark
```

## Development Tip

If you update .css, you have to force refresh your browser (`shift-command-r` on a mac) for the changes to register.

