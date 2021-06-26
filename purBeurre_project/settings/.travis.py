language: python
python:
  - '3.5'

# safelist
branches:
  only:
    - staging

before_script:
  - pip install -r riequirements.txt

services:
  - postgresql

env: DJANGO_SETTINGS_MODULE=disquaire_project.settings.travis

script:
  - python3 manage.py test
