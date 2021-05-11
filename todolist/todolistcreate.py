from todolistapp import db, todolist

db.drop_all()
db.create_all()

task_1 = todolist(task = 'vaccuum cleaning', status = True)
task_2 = todolist(task = 'dusting', status = False)
task_3 = todolist(task = 'wiping surfaces', status = False)
db.session.add(task_1)
db.session.add(task_2)
db.session.add(task_3)
db.session.commit()