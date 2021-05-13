from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@34.105.183.54/todolist_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = 'sdffdgdfhdbnvcn'
db = SQLAlchemy(app) 

class todolist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(50), nullable=False)
    status = db.Column(db.Boolean, default=False)

class newform(FlaskForm):
    task = StringField("Task")
    submit = SubmitField("New Task")

class formC(FlaskForm):
    submit = SubmitField ("Complete")

class formUNC(FlaskForm):
    submit = SubmitField ("Uncomplete")

@app.route('/')
def home():
    return 'This is a to-do list!'

@app.route('/new', methods=["GET", "POST"])
def new():
    form = newform()
    if form.validate_on_submit():
        new_task = todolist(task=form.task.data)
        db.session.add(new_task)
        db.session.commit()
        return redirect('index')
    return render_template('new.html', form=form)

@app.route('/update/<int:task_id>', methods=["GET", "POST"])
def update(task_id):
    form = newform()
    update_task = todolist.query.get(task_id)
    if form.validate_on_submit():
        update_task.task = form.task.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == "GET":
        form.task.data = update_task.task
    return render_template("update.html", form=form)

@app.route('/complete/<int:task_id>')
def complete(task_id):
    completed_task = (todolist.query.get(task_id))
    completed_task.status = True
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/uncomplete/<int:task_id>')
def uncomplete(task_id):
    uncompleted_task = (todolist.query.get(task_id))
    uncompleted_task.status = False
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    condemned_task = (todolist.query.get(task_id))
    db.session.delete(condemned_task)
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/index', methods=["GET", "POST"])
def index():

    queryall = todolist.query.all()
    return render_template('index.html', queryall=queryall)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')