from flask import Flask
from src.book_drop.web.BookController import BookController
from typing import List


class Web:

    @staticmethod
    def main(args: List[str]):
        app = Flask(__name__)
        BookController.register(app)
        app.config['WTF_CSRF_ENABLED'] = False

        return app

