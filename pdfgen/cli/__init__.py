# -*- coding: utf-8 -*-

"""
pdfgen.cli

This module implements PDFGEN's CLI, and should not be directly imported.
"""

import os
import click

from pdfgen import __version__
from pdfgen.cli.generate import generate_command


@click.group()
@click.version_option(version=__version__, prog_name="PDFGEN")
@click.option(
    "--var", multiple=True, help="A variable to template into config files.")
@click.pass_context
def cli(
        ctx, var
):
    """
    PDFGEN is a tool to generate PDF documents from Jinja Templates.
    """
    ctx.obj = {
        "variables": {},
        "config_path": os.path.joing(os.getcwd(), 'config'),
        "tempalte_path": os.path.joing(os.getcwd(), 'templates'),
        "output_path": os.path.joing(os.getcwd(), 'output')
    }

    if var:
        for variable in var:
            variable_key, variable_value = variable.split("=")
            ctx.obj.get("variables").update(
                {variable_key: variable_value}
            )


cli.add_command(generate_command)
