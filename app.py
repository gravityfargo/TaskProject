from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import exists
from datetime import datetime
from utils import cprint

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///TaskProject.db'
db.init_app(app)

class Tasks(db.Model): # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    tag = db.Column(db.String(20), nullable=True)
    date_created = db.Column(db.String, nullable=False)
    date_due = db.Column(db.String, nullable=True)
    def __repr__(self):
        return '<Task %r>' % self.id
    
class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)


@app.route('/', methods=['POST', 'GET']) # type: ignore
def index():
    if request.method == 'POST':
        task_content = request.form['content']

        task_tag = request.form['tag']
        if task_tag != "":
            tagquery = db.session.query(exists().where(Tags.title == task_tag))

            if tagquery.scalar() is False:
                addTagAPI(task_tag)

        task_due = request.form['datepicker']
        now = datetime.now()
        creationdate = now.strftime("%m/%d/%Y")
        new_task = Tasks(content=task_content, tag=task_tag, date_created=creationdate, date_due=task_due)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
    else:
        tasks = Tasks.query.order_by(Tasks.id).all()
        tags = Tags.query.order_by(Tags.id).all()
        return render_template('index.html', tasks=tasks, tags=tags)
    
@app.route('/tag/add', methods=['POST']) # type: ignore
def addTag():
    tag_content = request.form['content']
    new_tag = Tags(title=tag_content)
    try:
        db.session.add(new_tag)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an issue adding your category'

@app.route('/api/tag/add/<tagname>', methods=['POST', 'GET']) # type: ignore
def addTagAPI(tagname):
    new_tag = Tags(title=tagname)
    db.session.add(new_tag)
    db.session.commit()

@app.route('/tag/delete/<int:id>', methods=['POST']) # type: ignore
def deleteTag(id):
    tag_to_delete = Tags.query.get_or_404(id)
    try:
        db.session.delete(tag_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an issue adding your category'

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Tasks.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem loading the task.'

@app.route('/update/<int:id>', methods=['GET', 'POST']) # type: ignore
def update(id):
    task = Tasks.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was a problem.'
    else:
        return render_template('update.html', task=task)
    


if __name__ == "__main__":
    app.app_context().push()
    db.create_all()
    app.run(debug=True, threaded=True)