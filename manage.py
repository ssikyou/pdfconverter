import os

if os.path.exists('.env'):
    print('Importing environment from .env...')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            # print('{}:{}'.format(var[0], var[1]))
            os.environ[var[0]] = var[1]


from app import create_app
from flask_script import Manager, Shell

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app)
manager.add_command("shell", Shell(make_context=make_shell_context))


@app.context_processor
def inject_appids():
    return dict(fbappid=app.config['FACEBOOK_APP_ID'], gatid=app.config['GA_TRACK_ID'])


if __name__ == '__main__':
    manager.run()
