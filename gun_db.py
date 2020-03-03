#!/usr/bin/env python
"""
GunClear Gun DB CLI
"""
import click
from click_shell import shell

import json
from pathlib import Path

BASE_PATH=Path('db/')


def h2e(phrase):
    return phrase.replace('-', ' ').title()


def e2h(phrase):
    return phrase.replace(' ', '-').lower()


@shell(prompt='🔫 ~ ')
def gun_db():
    click.echo(__doc__)


@gun_db.command()
def makes():
    click.echo("\n".join([h2e(p.name) for p in BASE_PATH.iterdir() if p.is_dir()]))


@gun_db.command()
@click.argument('make')
def models(make):
    click.echo("\n".join([h2e(p.name) for p in (BASE_PATH / e2h(make)).iterdir() if p.is_dir()]))


@gun_db.command()
@click.argument('make')
@click.argument('model')
def variants(make, model):
    model_path = (BASE_PATH / e2h(make) / model)
    click.echo("\n".join([p.name.replace('.json', '') for p in model_path.iterdir() if p.is_file()]))


@gun_db.command()
@click.argument('make')
@click.argument('model')
@click.argument('variant')
def get_info(make, model, variant):
    file_path = (BASE_PATH / e2h(make) / model / variant).with_suffix('.json')
    with open(file_path, 'r') as f:
        click.echo(json.loads(f.read() or '{}'))


@gun_db.command()
@click.argument('make')
@click.argument('model')
@click.argument('variant')
@click.argument('param')
@click.argument('value')
def set_info(make, model, variant, param, value):
    file_path = (BASE_PATH / e2h(make) / model / variant).with_suffix('.json')
    with open(file_path, 'r') as f:
        parameters = json.loads(f.read() or '{}')

    click.echo(f"[{make}] {model} ({variant}):")
    click.echo("Before")
    click.echo(parameters)
    parameters[param] = value
    click.echo("After")
    click.echo(parameters)

    with open(file_path, 'w') as f:
        f.write(json.dumps(parameters))


if __name__ == '__main__':
    gun_db()
