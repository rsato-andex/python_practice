from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.Models.Manager_Model import db, Manager

# Flaskアプリケーションの設定
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://docker:docker@localhost/python_sample'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# アプリケーションコンテキストを設定
with app.app_context():
    db.init_app(app)

    try:
        # シードデータの作成
        managers = [
            Manager(username='aaaaa', password='aaaaa', mail="aaaaa@gmail.com", president_flg=1),
            Manager(username='bbbbb', password='bbbbb', mail="bbbbb@gmail.com", president_flg=0),
            Manager(username='ccccc', password='ccccc', mail="ccccc@gmail.com", president_flg=0),
        ]
        # データベースに挿入
        db.session.bulk_save_objects(managers)
        db.session.commit()
        print("Seeding completed.")
    except Exception as e:
        db.session.rollback()
        print(f"Error occurred: {e}")