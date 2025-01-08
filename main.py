from flask import Flask
from flask_migrate import Migrate
from src.extensions import db
from src.controllers.faculty_controller import faculty_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:spasojevic2002@localhost/faculty_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Register the faculty blueprint
app.register_blueprint(faculty_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
