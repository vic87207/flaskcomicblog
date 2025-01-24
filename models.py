"""
This is the actual database storing the data.
"""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import pytz

db = SQLAlchemy()
est = pytz.timezone("US/Eastern")
est_now = datetime.now(est)


class Comic(db.Model):
    """
    The class comic has every column in the data base a comic post needs.

    That includes a pk, title, description, img (path to it), and date

    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    decription = db.Column(db.Text, nullable=True)
    image_file = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, default=est_now)
