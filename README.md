# Setup instructions

* Clone this repo.
* Create a virtualenv:

        mkvirtualenv xtracker

* Install requirements:

        pip install -r requirements.txt

* Create tables:

        m migrate

* Create some sample data:

        m create_expenses 100


* Run your server:

        m runserver

* Enjoy: http://localhost:8000/

# Tips

* Linux/Mac: add to your `.bashrc` / `.bash_profile`:

    alias m='python manage.py'
    alias sp='python manage.py shell_plus'