from werkzeug.security import generate_password_hash, check_password_hash
from repositories.user_repository import UserRepository
from flask_jwt_extended import create_access_token

class AuthService:
    # returns jwt token on success, none on failure
    def create_account(self, user):
        if UserRepository.username_exists(user.username):
            return None # null value if username already exists
        
        user.password = generate_password_hash(user.password) # hash password

        UserRepository.create_user(user) # insert into database

        creds = UserRepository.get_user_credentials(user.username) # fetch credentials
        
        return create_access_token(identity=creds["user_id"]) # return jwt token