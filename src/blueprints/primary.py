import json

from pathlib import Path

from quart import Blueprint, render_template

primary = Blueprint("primary", "luckay.la", template_folder="html/templates/primary")
config = json.loads((Path("html/templates/primary/primary.json")).read_text())

@primary.route("/")
async def primary_home():
    return await render_template("home.jinja", **config)

@primary.route("/projects")
@primary.route("/blog")
@primary.route("/about")
async def primary_construction() -> str:
    return await render_template("construction.jinja", **config)
