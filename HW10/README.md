### ДЗ 10. Дебаг коду
run:
```shell
(venv) sl@sl:~/w/qa_python/HW10$ python for_debug_hw_lesson4_refactored.py 
Введіть назву першого товару: qwe
Введіть бажаєму кількість першого товару: 2
Введіть ціну першого товару: 2.00
Введіть назву другого товару: rty
Введіть бажаєму кількість другого товару: 3
Введіть ціну другого товару: 3.3




~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Фіскальний чек~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                             МАГАЗИН "ВСЕ ДЛЯ ДОМУ"                             
Товар                            кількість             ціна             вартість             
qwe.................             2                     2.00             4.00                 
rty.................             3                     3.30             9.90                 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ВСЬОГО                           5                     x                13.90                
                                                             20-04-2023 00:01:22

```
flake8/mypy:
```shell
(venv) sl@sl:~/w/qa_python/HW10$ flake8 for_debug_hw_lesson4_refactored.py 
(venv) sl@sl:~/w/qa_python/HW10$ mypy for_debug_hw_lesson4_refactored.py 
Success: no issues found in 1 source file
```
---
### ДЗ 11. Написання функцій та їх тестування
run:
```shell
(venv) sl@sl:~/w/qa_python/HW10$ python library.py 
ОЛО
```
pytest:
```shell
(venv) sl@sl:~/w/qa_python/HW10$ pytest -v .
========================================================================================== test session starts ==========================================================================================
platform linux -- Python 3.11.2, pytest-7.3.1, pluggy-1.0.0 -- /home/sl/w/qa_python/HW10/venv/bin/python
cachedir: .pytest_cache
rootdir: /home/sl/w/qa_python/HW10
collected 5 items                                                                                                                                                                                       

test_library.py::test_remove_lowercase_positive[\u0434\u043b\u043e\u041e\u041b\u041e  55 !-\u041e\u041b\u041e] PASSED                                                                             [ 20%]
test_library.py::test_remove_lowercase_positive[abc-] PASSED                                                                                                                                      [ 40%]
test_library.py::test_remove_lowercase_positive[ABC-ABC] PASSED                                                                                                                                   [ 60%]
test_library.py::test_remove_lowercase_positive[-] PASSED                                                                                                                                         [ 80%]
test_library.py::test_remove_lowercase_positive[XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXXX] PASSED                                                              [100%]

=========================================================================================== 5 passed in 0.01s ===========================================================================================
```
flake8/mypy:
```shell
(venv) sl@sl:~/w/qa_python/HW10$ flake8 library.py 
(venv) sl@sl:~/w/qa_python/HW10$ mypy library.py 
Success: no issues found in 1 source file
```