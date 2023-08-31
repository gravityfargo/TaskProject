from turtle import color
from flask import Blueprint, redirect, render_template, request, json
from datetime import datetime
from application.models import db, Tags, Tasks
from application.utils import cprint
from sqlalchemy.sql import exists    
import requests as rq


core_bp = Blueprint('core', __name__, template_folder='templates')

@core_bp.route('/') # type: ignore
def taskTable():
    tasks = Tasks.query.all()
    tags = Tags.query.all()
    # checkForTagInTasks("boob")
    return render_template('index.html', tasks=tasks, tags=tags)

@core_bp.route('/tag/table', methods=['POST', 'GET']) # type: ignore
def tagTable():
    tags = Tags.query.order_by(Tags.id).all()
    return render_template('tagstable.html', tags=tags)

@core_bp.route('/api/task/add', methods=['POST', 'GET']) # type: ignore
def newTask():
    now = datetime.now()
    creation_date = now.strftime("%m/%d/%Y")
    # Coming from the web form
    if request.method == 'POST':
        task_content_post = request.form['content']
        task_tag_post = request.form['tag']
        task_due_post = request.form['datepicker'] 
        
        # check if tag exists in that table
        if task_tag_post != "":
            tagquery = db.session.query(exists().where(Tags.content == task_tag_post))
            if tagquery.scalar() is False:
                newTag(tagname=task_tag_post)  
                         
        try:
            new_task = Tasks(content=task_content_post, tag=task_tag_post, date_created=creation_date, date_due=task_due_post)
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
    # API request
    elif request.method == 'GET' and request.args.get('task_content'):
        task_content_get = request.args.get('task_content')
        task_tag_get = request.args.get('task_tag')
        task_due_get = request.args.get('task_due')
        # check if tag exists in that table
        if task_tag_get != "":
            tagquery = db.session.query(exists().where(Tags.content == task_tag_get))
            if tagquery.scalar() is False:
                newTag(tagname=task_tag_get)
        try:
            new_task = Tasks(content=task_content_get, tag=task_tag_get, date_created=creation_date, date_due=task_due_get)
            db.session.add(new_task)
            db.session.commit()
            return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
        except:
            return 'There was an issue adding your task'
    else:
        return "failed"

@core_bp.route('/api/task/delete/<int:id>')
def deleteTask(id):
    task_to_delete = Tasks.query.get_or_404(id)
    taskquery = getTaskQueryByID(id)
    if checkForTagInTasks(taskquery.tag) == False:
        tagID = getTagIDByContent(taskquery.tag)
        if tagID == False:
            pass
        else:
            deleteTag(getTagIDByContent(taskquery.tag))
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return redirect('/')

@core_bp.route('/api/task/update/<int:id>', methods=['GET', 'POST']) # type: ignore
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

@core_bp.route('/api/tag/add', methods=['POST', 'GET']) # type: ignore
def newTag(**kwargs):
    new_tag_arg = kwargs.get('tagname', None)
    
    if request.method == 'POST':
        new_tag_post = request.form['content']
        try:
            new_tag = Tags(content=new_tag_post, colorhex="")
            db.session.add(new_tag)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
    else:
        try:
            new_tag = Tags(content=new_tag_arg, colorhex="")
            db.session.add(new_tag)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

# @core_bp.route('/api/tag/delete', methods=['POST']) # type: ignore
def deleteTag(id):
    tag_to_delete = Tags.query.get_or_404(id)
    try:
        db.session.delete(tag_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return redirect('/')
    
def checkForTagInTasks(tag):
    tagexist = Tasks.query.filter_by(tag=tag).all()
    if len(tagexist) > 1:
        return True
    else:
        return False

def getTagIDByContent(contents):
    tagquery = Tags.query.filter_by(content=contents).all() 
    try:
        tagid = tagquery[0].id
        return tagid
    except:
        return False

def getTaskQueryByID(id):
    task = Tasks.query.filter_by(id=id).first() 
    return task