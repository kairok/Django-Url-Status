from django.shortcuts import render_to_response, redirect
from django.contrib import auth
#from django.core import
#from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf
# Create your views here.

#@csrf_protect
def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username','')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/post/')
        else:
            args['login_error']="User not found"
            return render_to_response('login.html', args)

    else:
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/auth/login/')