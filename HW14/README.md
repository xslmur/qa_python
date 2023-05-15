```shell
(venv) sl@sl:~/w/qa_python/HW14$ pytest -v
========================================================================================== test session starts ==========================================================================================
platform linux -- Python 3.11.2, pytest-7.3.1, pluggy-1.0.0 -- /home/sl/w/qa_python/HW14/venv/bin/python
cachedir: .pytest_cache
rootdir: /home/sl/w/qa_python/HW14
collected 3 items                                                                                                                                                                                       

test_qauto.py::TestCarsAPI::test_auto_create PASSED                                                                                                                                               [ 33%]
test_qauto.py::TestCarsAPI::test_auto_modify PASSED                                                                                                                                               [ 66%]
test_qauto.py::TestCarsAPI::test_auto_delete PASSED                                                                                                                                               [100%]

========================================================================================== 3 passed in 11.19s ===========================================================================================
```