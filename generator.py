import sys
import tempfile
import shutil, os.path

import yaml
import jinja2

TECHNOLOGY_COLUMNS = 3
SKILLS_COLUMNS = 2

def render_html(yaml_file):
    with open(yaml_file) as f:
        resume = yaml.load(f)
        
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
    template = env.get_template('resume.html')
    
    resume["technology"]["columns"] = TECHNOLOGY_COLUMNS
    resume["skills"]["columns"] = SKILLS_COLUMNS
    
    return template.render(resume)

def create_html_file(yaml_file):
    html = render_html(yaml_file)
    temp_name = tempfile.NamedTemporaryFile().name
    filename = temp_name + ".html"
    with open(filename, 'w') as f:
        f.write(html)
    
    return filename


if __name__ == "__main__":

    resume_file = sys.argv[1]
    
    try:
        html_file = create_html_file(resume_file)
        destination = os.path.splitext(os.path.basename(resume_file))[0] + ".html"
        shutil.move(html_file, destination)
        print "Created {0} from {1}".format(destination, resume_file)
    except:
        print "Error creating html file"