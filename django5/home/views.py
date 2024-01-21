from django.shortcuts import render

#my code
from django.http import HttpResponse
from datetime import datetime
# (deleted) from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect


# Create your views here.
#my code

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)
    
class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}

class AuthorizedView(LoginRequiredMixin,TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'

''' (deleted):
def home(request):
    return render(request, 'home/welcome.html',{'today':datetime.today()})
'''

'''(deleted):
@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'home/authorized.html', {})
:)'''

