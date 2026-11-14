import re

from entities.user import User


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if username in self._user_repository.find_all():
            raise UserInputError("Invalid username or password")

        if len(username) < 3:
            raise UserInputError("Username has to consist only of letters(a-z) and be atleast 3 characters long")

        if not re.match("^[a-z]+$", username):
            raise UserInputError("Username has to consist only of letters(a-z) and be atleast 3 characters long")

        if len(password) < 8:
            raise UserInputError("Password has to be atleast 8 characters long and contain atleast 1 non-letter character")

        if re.match("^[a-z]+$", password):
            raise UserInputError("Password has to be atleast 8 characters long and contain atleast 1 non-letter character")


        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
