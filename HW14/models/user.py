import requests


class UserLoginData:
    def __init__(self, email, password, remember):
        self.email = email
        self.password = password
        self.remember = remember


class UserRegisterData:
    def __init__(self, name, last_name, login_data: UserLoginData):
        self.name = name
        self.lastName = last_name
        self.email = login_data.email
        self.password = login_data.password
        self.repeatPassword = login_data.password


class User:
    LOGIN_PATH = 'auth/signin'
    LOGOUT_PATH = 'auth/logout'
    REGISTER_PATH = 'auth/signup'
    USERS_PATH = 'users'
    PROFILE_PATH = USERS_PATH + '/profile'

    def __init__(self, api_base, session: requests.sessions, name, last_name, user_login: UserLoginData):
        self.api_base = api_base
        self.session = session
        self.user_login = user_login
        self.user_register = UserRegisterData(name, last_name, user_login)

    def login(self):
        return self.session.post(url=self.api_base + self.LOGIN_PATH,
                                 json=self.user_login.__dict__).json()

    def logout(self):
        return self.session.get(self.api_base + self.LOGOUT_PATH).json()

    def register(self):
        return self.session.post(url=self.api_base + self.REGISTER_PATH,
                                 json=self.user_register.__dict__).json()

    def delete(self):
        return self.session.delete(self.api_base + self.USERS_PATH).json()

    def get_profile(self):
        return self.session.get(self.api_base + self.PROFILE_PATH).json()
