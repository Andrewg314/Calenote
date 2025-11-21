from sqlalchemy import text
from db import engine

class UserRepository:
    def create_user(self, user):
        with engine.connect() as sesh:
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

    def get_user_credentials(self, username): 
        with engine.connect() as sesh:
            result = sesh.execute(
                text("SELECT user_id, password FROM users WHERE username = :username"),
                {"username": username}
            )
            row = result.mappings().fetchone()

        if not row:
            return None
        
        return {
            "user_id": row["user_id"],
            "hashed_pw": row["password"]
        }