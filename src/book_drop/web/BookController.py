import pyqrcode
from flask import render_template, redirect, request
from flask_classful import FlaskView, route  # type: ignore
import png

from src.book_drop.repository.sql_book_copy import SqlBookCopyRepository
from src.book_drop.repository.sql_person import SqlPersonRepository
from src.book_drop.repository.sql_ranking import SqlRankingRepository
from src.book_drop.repository.sql_review import SqlReviewRepository
from src.book_drop.web.BookForm import BookForm
from src.book_drop.web.ReviewForm import ReviewForm
from src.book_drop.web.UserForm import UserForm


class BookController(FlaskView):

    route_base = "/"

    @route('/')
    def index(self):
        return render_template("layout.html")

    @route('/ranking/', methods=['GET'])
    def blank_ranking(self):
        return render_template("ranking.html")

    @route('/ranking/<id>/', methods=['GET'])
    def ranking(self, id: str):
        ranking_repo = SqlRankingRepository(server="(local)\\SQLEXPRESS", database="cc520")

        results = ranking_repo.fetch_ranking(id)
        rows = results[0]
        cols = results[1]

        return render_template(
            "ranking.html",
            rows=rows,
            cols=cols)

    @route('/user-form/', methods=['GET'])
    def new_user(self):
        form = UserForm()
        return render_template("user-form.html", form=form)

    @route('/user-form/', methods=['POST'])
    def add_new_user(self):
        form = UserForm()

        user_name = form.user_name.data
        name = form.name.data

        person_repo = SqlPersonRepository(server="(local)\\SQLEXPRESS", database="cc520")
        person_repo.create_person(name, user_name)

        return redirect('/')

    @route('/book-form/', methods=['GET'])
    def new_book(self):
        form = BookForm()
        return render_template("book-form.html", form=form)

    @route('/book-form/', methods=['POST'])
    def add_new_book(self):
        form = BookForm()
        if not form.validate():
            return render_template("book-form.html", form=form)

        author_name = form.author_name.data
        book_name = form.book_name.data

        book_repo = SqlBookCopyRepository(server="(local)\\SQLEXPRESS", database="cc520")

        book_id = book_repo.create_book_copy(book_name, author_name)

        path = request.path
        url = pyqrcode.create(path)

        url_path = 'http://127.0.0.1:5000/' + 'qr-code/' + str(book_id)
        url.png('myqr.png', scale=6)

        return redirect(url_path)

    @route('/qr-code/<id>', methods=['GET'])
    def qr_code(self, id):
        print(id)
        url_path = 'http://127.0.0.1:5000/' + 'review-form/' + id

        return render_template("qrcode.html", url_path=url_path)

    @route('/review-form/<id>/', methods=['GET'])
    def new_review(self, id: int):
        form = ReviewForm()
        print(id)
        return render_template("review-form.html", form=form, id=id)

    @route('/review-form/<id>/', methods=['POST'])
    def add_new_review(self, id: int):
        form = ReviewForm()
        if not form.validate():
            return render_template("review-form.html", form=form)

        user_name = form.user_name.data
        star_rating = form.star_rating.data
        location = form.location.data

        person_repo = SqlPersonRepository(server="(local)\\SQLEXPRESS", database="cc520")
        user_id = person_repo.fetch_person(user_name)
        print(user_id)

        review_repo = SqlReviewRepository(server="(local)\\SQLEXPRESS", database="cc520")
        review_repo.create_review(user_id, id, star_rating, location)

        return redirect('/')

if __name__ == "__main__":
    BookController().add_new_review(4)