from os import path

import click

from pdfgen.pdfgen import Context
from pdfgen.pdfgen import Generator


@click.command(name="generate")
@click.argument("template", required=True)
@click.pass_context
def generate_command(ctx, template):
    """
    Generate a PDF from a Jinja template.

    """
    config_extension = '.py'
    template_extension = '.html'
    output_extension = '.pdf'

    context = Context(
        config=path.join(
            ctx.obj.get("config_path"),
            template + config_extension
        ),
        template_path=path.join(
            ctx.obj.get("template_path"),
            template + template_extension
        ),
        variables=ctx.obj.get("varibales"),
        output_path=path.join(
            ctx.obj.get("output_path"),
            template, output_extension),
    )

    generator = Generator(context)
    generator.execute()
    exit(0)
