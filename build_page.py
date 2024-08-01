from jinja2 import Environment, FileSystemLoader, select_autoescape
import json

env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape()
)

template = env.get_template("template.html")

with open('database.json', 'r') as db:
    data = json.load(db)

    output = template.render(protocols = data['protocols'], services = data['services'])
    with open('index.html', 'w') as f:
        f.write(output)
