from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Tasks(db.Model): # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    tag = db.Column(db.String(20), nullable=True)
    date_created = db.Column(db.String, nullable=False)
    date_due = db.Column(db.String, nullable=True)

    def __init__(self, content, tag, date_created, date_due):
        self.content = content
        self.tag = tag
        self.date_created = date_created
        self.date_due = date_due
    
class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(20), nullable=False)
    colorhex = db.Column(db.String(20), nullable=True)

    def __init__(self, content, colorhex):
        self.content = content
        self.colorhex = colorhex
