import imp
from re import template
from django.shortcuts import render
from datetime import datetime
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.shortcuts import render
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request


def index(request):
	if request.method == 'POST':
		city = request.POST['city']
		''' api key might be expired use your own api_key
			place api_key in place of appid ="your_api_key_here " '''

		# source contain JSON data from API

		source = urllib.request.urlopen(
			'http://api.openweathermap.org/data/2.5/weather?q='
					+ city + '&appid=93f26e3c57081a6210de53b8dcfdfea4&units=metric').read()

		# converting JSON data to a dictionary
		list_of_data = json.loads(source)

		# data for variable list_of_data
		data = {
            "city":city,
			"country_code": str(list_of_data['sys']['country']),
			"coordinate": str(list_of_data['coord']['lon']) + ' '
						+ str(list_of_data['coord']['lat']),
			"temp": str(list_of_data['main']['temp']) + 'k',
			"pressure": str(list_of_data['main']['pressure']),
			"humidity": str(list_of_data['main']['humidity']),
		}
		print(data)
	else:
		data ={}
	return render(request, "home/index.html", data)

# class createuser(CreateView):
#     form_class=UserCreationForm
#     template_name='home/register.html'
#     success_url='/notes'

#     def get(self,request,*args,**kwargs):
#         if(self.request.user.is_authenticated):
#             return redirect("notes.list")
#         return super().get(request,*args,**kwargs)
# class loginuser(LoginView):
#     template_name='home/login.html'
# class logoutuser(LogoutView):
#     template_name='home/logout.html'
class HomeView(TemplateView):
    template_name='home/welcome.html'
    extra_content={'today':datetime.today()}

# class AuthorizedView(LoginRequiredMixin,TemplateView):
#     template_name='home/authorized.html'
#     login_url='/admin'
