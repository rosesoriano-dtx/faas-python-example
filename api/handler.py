from jinja2 import Template
import json

def handle(req):
    input = json.loads(req)

    t = Template("{{greeting}} {{name}}")
    res = t.render(name=input["name"], greeting=input["greeting"])
    return res 