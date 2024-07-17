from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.Models.System_Manager_Model import db, System_Manager
from app.Models.Office_Model import db, Office
from app.Models.Stuff_Model import db, Stuff
from app.Models.User_Model import db, User

# Flaskアプリケーションの設定
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://docker:docker@localhost/python_sample'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# アプリケーションコンテキストを設定
with app.app_context():
    db.init_app(app)

    try:
        # Managerシードデータの作成
        system_managers = [
            System_Manager(username='smanger', password='smanager', mail="smanager@gmail.com")
        ]
        # データベースに挿入
        db.session.bulk_save_objects(system_managers)
        db.session.commit()

        # Officeシードデータの作成
        offices = [
            Office(address='北海道', call_number='11-1111-1111'),
            Office(address='宮城県', call_number='022-2222-2222'),
        ]
        # データベースに挿入
        db.session.bulk_save_objects(offices)
        db.session.commit()

        # Stuffシードデータの作成
        Stuffs = [
            Stuff(username='aaaaa', password='aaaaa', mail="aaaaa@gmail.com",office_id="1", president_flg=1),
            Stuff(username='bbbbb', password='bbbbb', mail="bbbbb@gmail.com",office_id="1", president_flg=0),
            Stuff(username='ccccc', password='ccccc', mail="ccccc@gmail.com",office_id="1", president_flg=0),
            Stuff(username='ddddd', password='ddddd', mail="ddddd@gmail.com",office_id="1", president_flg=0),
            Stuff(username='11111', password='11111', mail="11111@gmail.com",office_id="2", president_flg=1),
            Stuff(username='22222', password='22222', mail="22222@gmail.com",office_id="2", president_flg=0),
            Stuff(username='33333', password='33333', mail="33333@gmail.com",office_id="2", president_flg=0),
            Stuff(username='44444', password='44444', mail="44444@gmail.com",office_id="2", president_flg=0),
        ]
        # データベースに挿入
        db.session.bulk_save_objects(Stuffs)
        db.session.commit()

        # Userシードデータの作成
        Users = [
            User(username='aaaaa', password='aaaaa', mail="uaaaaa@gmail.com",office_id="1", stuff_id=2),
            User(username='bbbbb', password='bbbbb', mail="ubbbbb@gmail.com",office_id="1", stuff_id=3),
            User(username='11111', password='11111', mail="u11111@gmail.com",office_id="2", stuff_id=3),
            User(username='22222', password='22222', mail="u22222@gmail.com",office_id="2", stuff_id=2),
        ]
        # データベースに挿入
        db.session.bulk_save_objects(Users)
        db.session.commit()


        print("Seeding completed.")
    except Exception as e:
        db.session.rollback()
        print(f"Error occurred: {e}")