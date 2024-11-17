from os import getenv
from dotenv import load_dotenv
from sanic import Sanic, request

load_dotenv()

app = Sanic("luck-ayla")
app.config.FORWARDED_SECRET = getenv("SANIC_ID")
app.extend(config={"templating_path_to_templates": "html/"})
app.static("static/", "static/")


@app.get("/")
@app.ext.template("home.html")
async def home(req: request) -> dict:
    return {}


if __name__ == "__main__":
    app.run("127.0.0.1", 8000, fast=True, access_log=False)
