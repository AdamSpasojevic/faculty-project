from flask import Flask
from controller import faculty_blueprint

app = Flask(__name__)

# Register the faculty blueprint
app.register_blueprint(faculty_blueprint)


@app.route("/")
def home():
    return "Welcome to the Faculty API!"


if __name__ == "__main__":
    app.run(debug=True)
