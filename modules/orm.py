from modules.database import *
from flask_login import UserMixin
from abc import *
import time


class RDMS(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @staticmethod
    def get_one_raw(param_name, identifier, destination) -> list:
        db = get_db()
        db.execute(
            f"SELECT * FROM `{destination}` WHERE {param_name} = %s LIMIT 1", (
                identifier, )
        )
        value = db.fetchone()
        return value

    @staticmethod
    def get_all_raw(param_name, identifier, destination) -> list:
        db = get_db()

        db.execute(
            f"SELECT * FROM `{destination}` WHERE {param_name} = %s", (
                identifier, )
        )
        # values = db.fetchone()
        values = db.fetchall()
        return values

    @abstractmethod
    def get(identifier):
        pass

    @staticmethod
    def delete(param_name, identifier, destination):
        db = get_db()
        db.execute(
            f"DELETE FROM `{destination}` WHERE `{param_name}` = %s",
            (identifier),
        )
        db.commit()


class User(UserMixin, RDMS):
    TABLE_NAME = 'popcorn_user'

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def __repr__(self):
        return f"User_{self.id}({self.name}: email={self.email})"

    @staticmethod
    def get(user_id):
        user = User.get_one_raw('id', user_id, User.TABLE_NAME)
        if not user:
            return None
        return User(*user)

    @staticmethod
    def create(name, phone_number):
        create_column(User.TABLE_NAME, name=name, phone_number=phone_number)
        
        
    
