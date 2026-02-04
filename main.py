from flask import Flask, render_template
from db import db
from models import Projetos

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

@app.route('/')
def home():
    projetos = db.session.query(Projetos).all()
    return render_template('home.html', projetos=projetos)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)