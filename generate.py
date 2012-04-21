import sys

import yaml
import jinja2

TECHNOLOGY_COLUMNS = 3
SKILLS_COLUMNS = 2

def render_html(resume_file):
    with open(resume_file) as f:
        resume = yaml.load(f)
        
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
    template = env.get_template('resume.html')
    
    resume["technology"]["columns"] = TECHNOLOGY_COLUMNS
    resume["skills"]["columns"] = SKILLS_COLUMNS
    
    return template.render(resume)


if __name__ == "__main__":

    resume_file = sys.argv[1]
    print render_html(resume_file)