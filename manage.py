from flask_script import Manager

from my_app import app, db, Car

manager = Manager(app)
app.config['DEBUG'] = True

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, Car=Car)

if __name__ ==   '__main__':
    manager.run()