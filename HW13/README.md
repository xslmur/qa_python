run:
```shell
(venv) sl@sl:~/w/qa_python/HW13$ pytest -v
========================================================================================== test session starts ==========================================================================================
platform linux -- Python 3.11.2, pytest-7.3.1, pluggy-1.0.0 -- /home/sl/w/qa_python/HW10/venv/bin/python
cachedir: .pytest_cache
rootdir: /home/sl/w/qa_python/HW13
collected 17 items                                                                                                                                                                                      

test_api.py::TestRegister::test_user_register PASSED                                                                                                                                              [  5%]
test_api.py::TestRegister::test_user_register_empty_fields[name] PASSED                                                                                                                           [ 11%]
test_api.py::TestRegister::test_user_register_empty_fields[lastName] PASSED                                                                                                                       [ 17%]
test_api.py::TestRegister::test_user_register_empty_fields[email] PASSED                                                                                                                          [ 23%]
test_api.py::TestRegister::test_user_register_empty_fields[password] PASSED                                                                                                                       [ 29%]
test_api.py::TestRegister::test_user_register_empty_fields[repeatPassword] PASSED                                                                                                                 [ 35%]
test_api.py::TestRegister::test_user_register_wrong_name PASSED                                                                                                                                   [ 41%]
test_api.py::TestRegister::test_user_register_wrong_lastname PASSED                                                                                                                               [ 47%]
test_api.py::TestRegister::test_user_register_wrong_password[test] PASSED                                                                                                                         [ 52%]
test_api.py::TestRegister::test_user_register_wrong_password[t1T] PASSED                                                                                                                          [ 58%]
test_api.py::TestRegister::test_user_register_wrong_password[tttttttttttttttttttt] PASSED                                                                                                         [ 64%]
test_api.py::TestRegister::test_user_register_wrong_password[tttttttttt] FAILED                                                                                                                   [ 70%]
test_api.py::TestRegister::test_user_register_passwords_do_not_match PASSED                                                                                                                       [ 76%]
test_api.py::TestAuth::test_user_login PASSED                                                                                                                                                     [ 82%]
test_api.py::TestAuth::test_user_login_wrong_email PASSED                                                                                                                                         [ 88%]
test_api.py::TestAuth::test_user_login_wrong_password PASSED                                                                                                                                      [ 94%]
test_api.py::TestAuth::test_check_user_profile PASSED                                                                                                                                             [100%]

=============================================================================================== FAILURES ================================================================================================
______________________________________________________________________ TestRegister.test_user_register_wrong_password[tttttttttt] _______________________________________________________________________

self = <test_api.TestRegister object at 0x7f9c03c847d0>, pwd = 'tttttttttt'

    @pytest.mark.parametrize('pwd', [
        'test', 't1T', 't' * 20, 't' * 10])
    def test_user_register_wrong_password(self, pwd):
        malformed_user = deepcopy(self.user)
        malformed_user.user_register.password = pwd
    
        result = malformed_user.register()
        if result['status'] == 'ok':
            malformed_user.delete()
    
        assert result['status'] == 'error'
>       assert result['message'] == ('Password has to be from 8 to 15 characters long '
                                     'and contain at least one integer, one capital, and one small letter')
E       AssertionError: assert 'Passwords do not match' == 'Password has... small letter'
E         - Password has to be from 8 to 15 characters long and contain at least one integer, one capital, and one small letter
E         + Passwords do not match

test_api.py:135: AssertionError
======================================================================================== short test summary info ========================================================================================
FAILED test_api.py::TestRegister::test_user_register_wrong_password[tttttttttt] - AssertionError: assert 'Passwords do not match' == 'Password has... small letter'
===================================================================================== 1 failed, 16 passed in 10.79s =====================================================================================
(venv) sl@sl:~/w/qa_python/HW13$ 

```
note:
```shell
test_api.py::TestRegister::test_user_register_wrong_password[tttttttttt] FAILED                                                                                                                   [ 70%]
```
is expected to be failed coz API has bug in the password field validator
