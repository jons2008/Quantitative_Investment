from datetime import datetime

from bottle import route, view, request, redirect, template, HTTPError

from models import PollNotFound
from models.factory import create_repository
from settings import REPOSITORY_NAME, REPOSITORY_SETTINGS

repository = create_repository(REPOSITORY_NAME, REPOSITORY_SETTINGS)

@route('/home1')
@view('index')
def home1():
    """Renders the home page, with a list of all polls."""
    return dict(
        title='Polls',
        year=datetime.now().year,
        polls=repository.get_polls(),
    )
