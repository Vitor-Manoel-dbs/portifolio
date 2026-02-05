from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager
from db import db
from models import Projetos
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

admin_user = os.getenv('ADMIN_USER')
admin_password = os.getenv('ADMIN_PASSWORD')

@app.route('/')
def home():
    projetos = db.session.query(Projetos).all()
    return render_template('home.html', projetos=projetos)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        user = request.form['usuario']
        admin = request.form['senha']
        if user == admin_user and admin == admin_password:
            titulo = request.form['titulo']
            descricao = request.form['descricao']
            url = request.form['url']
            image_url = request.form['image_url']
            novo_projeto = Projetos(nome=titulo, descricao=descricao, url=url, image_url=image_url)
            db.session.add(novo_projeto)
            db.session.commit()
            projetos = db.session.query(Projetos).all()
            return render_template('admin.html', projetos=projetos)

    projetos = db.session.query(Projetos).all()
    return render_template('admin.html', projetos=projetos)

@app.route('/admin/remove', methods=['POST', 'GET'])
def remove():
    if request.method == 'POST':
        admin_name = request.form['admin_name']
        admin_pass = request.form['admin_pass']
        projeto_id = request.form['projeto_nome']
        if admin_name == admin_user and admin_pass == admin_password:
            try:
                projeto = db.session.query(Projetos).filter_by(nome=projeto_id).first()
                db.session.delete(projeto)
                db.session.commit()
            except Exception as e:
                print(f"Erro ao remover projeto: {e}")
            return redirect(url_for('admin'))
    projetos = db.session.query(Projetos).all()
    return render_template('remove.html', projetos=projetos)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)