from flask import render_template
from . import main

@main.app_errorhandler(404)
def fo_O_fo(error):
    """
    Function to render the 404 error page
    """
    return render_template('fo_O_fo.html'), 404