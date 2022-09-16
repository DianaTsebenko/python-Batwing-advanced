from flask import Flask
from config import Config
from database import db
from api.book_api import book_router
from api.authors_api import authors_router
from api.book_authors_api import book_authors


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(book_router)
    app.register_blueprint(authors_router)
    app.register_blueprint(book_authors)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0")
