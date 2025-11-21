from sqlalchemy import text
from db import engine

class UserRepository:
    def create_user(self, user):
        with engine.begin() as sesh:
            sesh.execute(
                text("INSERT INTO users (username, password, first_name, last_name) VALUES (:u, :p, :f, :l)"),
                {
                    "u": user.username, 
                    "p": user.password, 
                    "f": user.first_name, 
                    "l": user.last_name
                 }
            )
            
            sesh.commit()

    def username_exists(self, username):
        with engine.connect() as sesh:
            result = sesh.execute(
                text("SELECT 1 FROM users WHERE username = :u"),
                {"u": username}
            ).fetchone()

        return result is not None

    def get_user_credentials(self, username): 
        with engine.connect() as sesh:
            result = sesh.execute(
                text("SELECT user_id, password FROM users WHERE username = :username"),
                {"username": username}
            ).mappings().fetchone()

        if not result:
            return None
        
        return {
            "user_id": result["user_id"],
            "hashed_pw": result["password"]
        }
    
    def get_user_by_id(self, user_id):
        with engine.connect() as sesh:
            result = sesh.execute(
                text("SELECT username, first_name, last_name FROM users WHERE user_id = :user_id"),
                {"user_id": user_id}
            ).mappings().fetchone()

        if result is None:
            return None

        return {
            "username": result["username"],
            "first_name": result["first_name"],
            "last_name": result["last_name"]
        }