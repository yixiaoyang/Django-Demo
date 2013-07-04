# Create your views here.
from django.template import loader, Context, RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login ,logout as auth_logout  
from django.utils.translation import ugettext_lazy as _
from blog.models import BlogPost
from django.shortcuts import render_to_response

### 
# rewrite lofin as auth_login
def _login(request, username, password):  
    ret = False  
    user = authenticate(username=username, password=password)  
    if user:  
        if user.is_active:  
            auth_login(request, user)  
            ret = True  
        else:  
            messages.add_message(request, messages.INFO, _(u'user not active'))  
    else:  
        messages.add_message(request, messages.INFO, _(u'user not found'))  
    return ret

### forms
class LoginForm(forms.Form):
    username=forms.CharField(label=_(u"username"),
                             max_length=32,
                             widget=forms.TextInput(attrs={"class":"input-block-level", "placeholder":"username",}))  
    password=forms.CharField(label=_(u"password"),
                             max_length=32,
                             widget=forms.PasswordInput(attrs={"class":"input-block-level", "placeholder":"username",})) 

###
def archive(request):
    if request.user.is_authenticated():
        user = request.user;  # get login user obj  
    else:     
        user = request.user;  # get AnonymousUser obj  

    # get all objects, ordered by timestamp
    posts = BlogPost.objects.all().order_by("-timestamp")    
    # load content in Template
    t = loader.get_template("article.html")
    c = Context({ 'posts': posts })
    return HttpResponse(t.render(c))

def user_login(request):
        template_var={"error":False,}
        
        form = LoginForm()      
        if request.method == 'POST':  
            form = LoginForm(request.POST.copy())  
        if form.is_valid():  
            _login(request, form.cleaned_data["username"], form.cleaned_data["password"])  
            return HttpResponseRedirect(reverse("archive"))
        
        template_var["form"] = form
        template_var["error"]=True
        template_var["tips"]=(u"Please sign in!")
        return render_to_response("login.html",template_var, context_instance=RequestContext(request))


# end of file