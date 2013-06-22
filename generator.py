#!/usr/bin/env python2

import sys
import tempfile
import shutil
import os.path
import subprocess

import yaml
import jinja2

TECHNOLOGY_COLUMNS = 3
SKILLS_COLUMNS = 2
PDF_COMMAND = "wkhtmltopdf -s letter -B 1in -L 1in -R 1in -T .70in"


def render_html(yaml_file):
    with open(yaml_file) as f:
        resume = yaml.load(f)

    env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
    template = env.get_template('resume.html')

    try:
        resume["technology"]["columns"] = TECHNOLOGY_COLUMNS
        resume["skills"]["columns"] = SKILLS_COLUMNS
    except KeyError:
        pass

    return template.render(resume)


def create_html_file(yaml_file):
    html = render_html(yaml_file)
    temp_name = tempfile.NamedTemporaryFile().name
    filename = temp_name + ".html"
    with open(filename, 'w') as f:
        f.write(html)

    return filename


def create_pdf_file(yaml_file):
    html_filename = create_html_file(yaml_file)
    pdf_filename = os.path.splitext(html_filename)[0] + ".pdf"

    full_command = PDF_COMMAND.split() + [html_filename, pdf_filename]
    try:
        subprocess.check_call(full_command)
    except OSError:
        sys.exit("`wkhtmltopdf` does not exist.")

    return pdf_filename


if __name__ == "__main__":

    resume_file = sys.argv[1]

    pdf = create_pdf_file(resume_file)
    destination = os.path.splitext(os.path.basename(resume_file))[0] + ".pdf"
    shutil.move(pdf, destination)
    print "Created {0} from {1}".format(destination, resume_file)
