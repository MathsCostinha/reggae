from django.views.generic import TemplateView

# Create your views here.

class LoginPageView(TemplateView):
    template_name = 'login.html'
    
class HomePageView(TemplateView):
    template_name = 'home.html'