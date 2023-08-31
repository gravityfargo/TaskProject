from flask import Flask
from .models import db
from .blueprints.core.core_routes import core_bp

app = Flask(__name__, instance_relative_config=False)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///TaskProject.db'
app.config.from_object('config')
app.register_blueprint(core_bp)
db.init_app(app)