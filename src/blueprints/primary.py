import json

from pathlib import Path

from sanic import Blueprint
from sanic.request import Request
from sanic.response import HTTPResponse, html
from jinja2 import Environment, FileSystemLoader

config = json.loads((Path("html/primary.json")).read_text())

# Jinja
environment = Environment(loader=FileSystemLoader(Path("html")))
template_home = environment.get_template("home.jinja")
template_construction = environment.get_template("construction.jinja")

# Sanic
host = "localhost:8000" if config["debug"] else "luckay.la"
home = Blueprint("primary", host=host)


@home.route("/")
async def primary_home(req: Request) -> HTTPResponse:
    return html(template_home.render(active="home", **config))

@home.route("/projects", name="projects")
@home.route("/blog", name="blog")
@home.route("/about", name="about")
async def primary_construction(req: Request) -> HTTPResponse:
    return html(template_construction.render(active="home", **config))
