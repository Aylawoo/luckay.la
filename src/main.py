from dotenv import load_dotenv
from quart import Quart

from blueprints.primary import primary

load_dotenv()

app = Quart("luckay.la")
app.register_blueprint(primary)


if __name__ == "__main__":
    app.run("127.0.0.1", 8000)