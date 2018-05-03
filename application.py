from setup import create_app, db
from models.helper import model_classes

application = create_app()


# can test application with 'flask shell'
@application.shell_context_processor
def make_shell_context():
    return dict({'db': db}, **model_classes)



if __name__ == "__main__":
    # application.debug = True
    application.run()
