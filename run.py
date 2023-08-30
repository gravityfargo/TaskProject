from application import app
from application.models import db

if __name__ == "__main__":
    app.app_context().push()
    db.create_all()
    app.run()