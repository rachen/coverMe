from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required

from coverMe.forms import *


def index(request):
    return render_to_response('index.html', {'user': request.user})


# Gets the user profile page for a given user
# need to present a form to fill out info
@login_required
def profile(request):
    profile = request.user.get_profile()

