import requests
import pytest
from copy import deepcopy

API_BASE = 'https://qauto2.forstudy.space/api/'


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

    def __init__(self, session: requests.sessions, name, last_name, user_login: UserLoginData):
        self.session = session
        self.user_login = user_login
        self.user_register = UserRegisterData(name, last_name, user_login)

    def login(self):
        return self.session.post(url=API_BASE + self.LOGIN_PATH,
                                 json=self.user_login.__dict__).json()

    def logout(self):
        return self.session.get(API_BASE + self.LOGOUT_PATH).json()

    def register(self):
        return self.session.post(url=API_BASE + self.REGISTER_PATH,
                                 json=self.user_register.__dict__).json()

    def delete(self):
        return self.session.delete(API_BASE + self.USERS_PATH).json()

    def get_profile(self):
        return self.session.get(API_BASE + self.PROFILE_PATH).json()


class DataUserProfileGet:
    def __init__(self, user_id, photo_file_name, name, last_name):
        self.userId = user_id
        self.photoFilename = photo_file_name
        self.name = name
        self.lastName = last_name

    def __str__(self):
        return self.__dict__


class UserProfileGet:
    def __init__(self, status: str, data: DataUserProfileGet):
        self.status = status
        self.data = data.__dict__


class TestRegister:
    def setup_class(self):
        self.session = requests.session()

        user_to_login = UserLoginData("test@tesster.com", "Qwerty12345", False)
        self.user = User(self.session, 'TestName', 'TestLastName', user_to_login)

    def test_user_register(self):
        result = self.user.register()
        self.user.delete()
        assert result['status'] == 'ok'

    # iterate over UserRegisterData fields
    @pytest.mark.parametrize('field_name', [
        'name', 'lastName', 'email', 'password', 'repeatPassword'])
    def test_user_register_empty_fields(self, field_name):
        # deepcopy to avoid self.user modifications
        malformed_user = deepcopy(self.user)

        # set empty field
        setattr(malformed_user.user_register, field_name, '')

        result = malformed_user.regdeepcopyister()

        # delete it in cases we got 'ok'
        if result['status'] == 'ok':
            malformed_user.delete()

        assert result['status'] == 'error'
        assert result['message'] == f'"{field_name}" is not allowed to be empty'

    def test_user_register_wrong_name(self):
        malformed_user = deepcopy(self.user)
        malformed_user.user_register.name = 'wrong_name'

        result = malformed_user.register()
        if result['status'] == 'ok':
            malformed_user.delete()

        assert result['status'] == 'error'
        assert result['message'] == 'Name is invalid'

    def test_user_register_wrong_lastname(self):
        malformed_user = deepcopy(self.user)
        malformed_user.user_register.lastName = 'wrong_last_name'

        result = malformed_user.register()
        if result['status'] == 'ok':
            malformed_user.delete()

        assert result['status'] == 'error'
        assert result['message'] == 'Last Name is invalid'

    @pytest.mark.parametrize('pwd', [
        'test', 't1T', 't' * 20, 't' * 10])
    def test_user_register_wrong_password(self, pwd):
        malformed_user = deepcopy(self.user)
        malformed_user.user_register.password = pwd

        result = malformed_user.register()
        if result['status'] == 'ok':
            malformed_user.delete()

        assert result['status'] == 'error'
        assert result['message'] == ('Password has to be from 8 to 15 characters long '
                                     'and contain at least one integer, one capital, and one small letter')

    def test_user_register_passwords_do_not_match(self):
        malformed_user = deepcopy(self.user)
        malformed_user.user_register.repeatPassword = 'test'

        result = malformed_user.register()
        if result['status'] == 'ok':
            malformed_user.delete()

        assert result['status'] == 'error'
        assert result['message'] == 'Passwords do not match'

    def teardown_class(self):
        self.user.login()
        self.user.delete()


class TestAuth:
    def setup_class(self):
        self.session = requests.session()

        user_to_login = UserLoginData("test@tesster.com", "Qwerty12345", False)
        self.user = User(self.session, 'TestName', 'TestLastName', user_to_login)

        self.user.register()
        self.user.logout()

    def setup_method(self):
        result = self.user.login()
        # save for profile tests
        self.user_id = result['data']['userId']

    def test_user_login(self):
        self.user.logout()
        result = self.user.login()
        assert result["status"] == "ok"

    def test_user_login_wrong_email(self):
        malformed_user = deepcopy(self.user)
        malformed_user.user_login.email = 'wrong_user@domain.invalid'
        self.user.logout()
        result = malformed_user.login()
        assert result["status"] == "error"
        assert result["message"] == "Wrong email or password"

    def test_user_login_wrong_password(self):
        malformed_user = deepcopy(self.user)
        malformed_user.user_login.password = 'wrong_pass'
        self.user.logout()
        result = malformed_user.login()
        assert result["status"] == "error"
        assert result["message"] == "Wrong email or password"

    def test_check_user_profile(self):
        result = self.user.get_profile()

        data = DataUserProfileGet(self.user_id, 'default-user.png',
                                  self.user.user_register.name,
                                  self.user.user_register.lastName)

        profile = UserProfileGet('ok', data)

        assert result["data"] == profile.data
        assert result["status"] == profile.status

    def teardown_method(self):
        self.user.logout()

    def teardown_class(self):
        self.user.login()
        self.user.delete()
