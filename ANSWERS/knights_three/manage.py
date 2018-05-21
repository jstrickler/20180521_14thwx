#!/usr/bin/env python
# (c)2015 John Strickler

from flask.ext.script import Manager, Server
from knights_three import create_app
from config import DevConfig

app = create_app(DevConfig)

manager = Manager(app)

manager.add_command("server", Server())

@manager.shell
def make_shell_context():
    return dict(app=app)


if __name__ == '__main__':
    manager.run()
