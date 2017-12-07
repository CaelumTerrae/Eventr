# Eventr

Eventr is a web-app designed with the intent of managing the many event posters posted around Harvard's campus. It uses optical character recognition to automatically recognize event-dates, the end-user just adds the title. Eventr is also an online registry of all other user-posted events, which can be navigated very easily on the site.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

This project is built on Flask and SQLite3. It also uses uses several python libraries. To run the application you will need:

* Python 2.7 
* pip should already be installed if you are using python, but if you attempt to use pip and for some reason it does not work, follow the installation instructions located [here](https://pip.pypa.io/en/stable/installing/)
* The dependencies required in ```requirements.txt``` To do this, simply navigate to the project directory after you have downloaded it and run the command below in your shell.

```
pip install -r requirements.txt
```

### Installing
This project cannot be run on the CS50 IDE because it has a python module that cannot be installed on the IDE for some reason. Instead it should be run on a computer using some shell. 

This will guide you to running the environment on your computer

First you will need to set up the Flask environment. If running on a Mac use:
```
export FLASK_APP=application.py
```

Windows:
```
set FLASK_APP=application.py
```

Next, enter
```
flask run
```

By default the server runs on [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [Jinja](http://jinja.pocoo.org/) - Templating engine
* [pip](https://pypi.python.org/pypi/pip) - Python package manager
* [OCR.Space](https://ocr.space/ocrapi) - Optical character recognition manager
* [datefinder](https://github.com/akoumjian/datefinder) - A python module for locating dates inside text
* [sqlite3](https://www.sqlite.org) - Database

## Authors

* **Gavin Lifrieri** - [CaelumTerrae](https://github.com/CaelumTerrae)


## Acknowledgments

* Thank you DJM for being a great lecturer
* Thank you CS50 heads for the starter code (C$50 Finance lol)
* Thank you Douglas for being an awesome TF and for fielding my awkward questions
* This was CS50
