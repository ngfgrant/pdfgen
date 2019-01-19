# PDFGen

A simple Python 3 CLI that generates a PDF from a template and CLI arguments.

# Usage

```shell
pdfgen TEMPLATE --var=value --var2=value2 --var3=value3 OUTPUT_NAME
```

If OUTPUT_NAME is left blank then the output filename will be `template-name-YYYY-mm-dd.pdf`

```python
document_context = Context(config, template=template_path, variables=vars, ouput=output_path)

generator = Generator(document_context)

generator.execute()
```

# Use Cases

I was having to frequently do invoices that involved replacing values of a word doc then saving
a PDF and emailing that output to a specific address.

Would also be good for generating invitations, or anything else that you'd like in PDF format.

# Concepts

The three main concepts in PDFGen are:

## Config

Stores the configuration for a PDF document

## Document Context

A document context contains:

- the config for the PDF document (such as font size),
- the template path to use,
- the variables to pass to the template,
- and an output path.

## Generator

Responsible for taking a Context and merging the Template with the Variables and writing a PDF to
the Output Path.
