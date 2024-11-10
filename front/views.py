from django.http import HttpResponseRedirect,HttpResponse,Http404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import LoginView
from .models import Price
from . import forms


# Create your views here.
def index_page(request):
    price = Price.objects.all()
    context = {
        'price':price
    }
    return render(request, 'index.html',context)

def SignPage(request):

    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse('Your passwords do not Match !!!')
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()

        return HttpResponseRedirect('login')
        

    return render(request, 'signup.html')


class CustomLoginView(LoginView):
    def form_valid(self,form):

        response = super().form_valid(form)

        if self.request.user.groups.filter(name='editor').exists():
            return redirect('details')
        else:
            return redirect('index')



@user_passes_test(lambda u: u.groups.filter(name='editor').exists(), login_url='/index')

def form_page(request):

    form = forms.AddPrice()

    context = {
        'form':form
    }

    if request.method == 'POST':
        form = forms.AddPrice(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/details')

    else:
        form = forms.AddPrice()
       
    return render(request, 'form.html', context)


# admin page for showing services
@user_passes_test(lambda u: u.groups.filter(name='editor').exists(), login_url='/index')

def details(request):

    # delete = Price.objects.get(id=id).delete()
    context = {
            'items': Price.objects.all(),
        }
               
    return render(request, 'details.html',context)
   
def update(request,id):
    item = Price.objects.get(id=id)
    if request.method == 'POST':
        form = forms.AddPrice(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('details')
    else:
        form = forms.AddPrice(instance=item)

    context = {
        'form':form
    }

    return render(request,'update.html',context)

def delete(request,id):
    # models.Movie.objects.get(pk=id).delete()
    try:
        price = Price.objects.get(id=id)
    except:
        raise Http404('Service does not exist')
    price.delete() 

    return HttpResponseRedirect('/details')