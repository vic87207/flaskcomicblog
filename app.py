"""
This is the main app.py.

We will have route to index ('/'), specific post using id, and new post
"""

from flask import Flask, render_template, redirect, url_for, request, flash
from models import db, Comic
from forms import ComicForm
import os
from werkzeug.utils import secure_filename
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comics.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "your_secret_key"
app.config["UPLOAD_FOLDER"] = "static/images"

db.init_app(app)

migrate = Migrate(app, db)


@app.route("/")
def index():
    """
    This is the index page, we should be able to pull all the posts from here

    """
    comics = Comic.query.order_by(Comic.date_posted.desc()).all()
    return render_template("index.html", comics=comics)


@app.route("/post/<int:comic_id>")
def post(comic_id):
    """
    this will be able to pull specific comic post with the id
    """
    comic = Comic.query.get_or_404(comic_id)
    return render_template("post.html", comic=comic)


@app.route("/new", methods=["GET", "POST"])
def new_comic():
    form = ComicForm()
    if form.validate_on_submit():
        if form.image.data:  # Check if a file was uploaded
            print(f"File: {form.image.data}")  # Debug print
            image_file = secure_filename(form.image.data.filename)
            print(f"Secure filename: {image_file}")  # Debug print
            form.image.data.save(os.path.join(app.config["UPLOAD_FOLDER"], image_file))
            new_comic = Comic(
                title=form.title.data,
                description=form.description.data,
                image_file=image_file,
                date_posted=form.date_published.data,
            )
            db.session.add(new_comic)
            db.session.commit()
            flash("Comic posted successfully!", "success")
            return redirect(url_for("index"))
        else:
            flash("No file uploaded!", "error")  # Add a flash message for debugging
    return render_template("new_post.html", form=form)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
