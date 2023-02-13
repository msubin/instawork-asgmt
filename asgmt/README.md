# Full-stack Take-home Assignment

The project implements a simple team-member management application that allows the user to view, edit, and delete team members.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).
#### Clone the repository
`git clone https://github.com/msubin/instawork-asgmt.git`
#### Create the virtual environment and Start the server
```bash
$ virtualenv project-env
$ source project-env/bin/activate
$ cd asgmt
$ pip install -r requirements.txt
$ python manage.py runserver
```
Your application should now be running at http://127.0.0.1:8000/

## Testing
Instructions on how to run the automated tests for this system.

```python manage.py test members_app.tests```

## Built With
- Django - The web framework used
- Python - The programming language

## Author

Subin Moon | [Github](https://github.com/msubin) | joy120594@gmail.com