some django beginner-intermediate-advanced projects from books / tutorials modified to learn quickly and try features out

#### made use of {in no particular order}
  - Brad Traversy
  - simpleisbetterthancomplex.com
  - Django 3 by example (3rd ed)
  - Django 3 web dev. cookbook (4th ed)
  - Building Django 2 web applications
  - django for beginners (WS Vincent)
  - django for professionals (WSV)
  - django for apis (WSV)
  - django crash course from the guys who made 2 scoops of django

  - various udemy / codemy / packt video / skillshare tutorials
  - Practical django 2 and channels /pro-complex/ (F. Marani)
      this uses channels that is event driven asgi - django 3 has "stolen" it
  - Testdriven.io tutorial(s)
  - ...and one of the bests: TalkPython.fm training materials



#### to install
have python 3.7+ available and create a virtual environment for pip packages first (py3)  
```python3 -m venv .venv```

optionally install watchman for quicker dev. srv. reload (pywatchman is in dev reqs)  
```brew install watchman```

activate it  
```source ./.venv/bin/activate```

install packages  
```pip install -r requirements[_dev].txt```

try it  
```cd into folder and use python ./manage.py migrate/collectstatic/*runserver*```