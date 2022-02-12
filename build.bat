xcopy /e /Y src\django_dart_reverse django-dart-reverse\django_dart_reverse


CALL venv\Scripts\activate.bat

cd django-dart-reverse

CALL python setup.py sdist

CALL python setup.py bdist_wheel

cd ..