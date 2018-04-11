from setup import create_app
from setup import db
from models.helper import model_classes

main_application = create_app()


# can test application with 'flask shell'
@main_application.shell_context_processor
def make_shell_context():
    return dict({'db': db}, **model_classes)



if __name__ == "__main__":
    # main_application.debug = True
    main_application.run()
