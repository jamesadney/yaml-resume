import yaml
import jinja2

if __name__ == "__main__":

    with open("resume.yml") as f:
        resume = yaml.load(f)
        
    from jinja2 import Environment, FileSystemLoader
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('resume.html')
    
    print template.render(resume)
