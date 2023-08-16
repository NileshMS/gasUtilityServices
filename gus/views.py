from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Services, ServiceRequest
from django.views.generic import ListView, DetailView
from django.contrib.auth import get_user_model
User = get_user_model()


class ServicesListView(ListView):
    model = Services
    template_name = 'gus/home.html'
    context_object_name = 'services'

class ServiceDetailView(DetailView):
    model = Services
    template_name = 'gus/details.html'

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'{username} account has been created! now you are able to log in ')
            return redirect('login')
        else:
            return render(request, 'users/registration.html', {'form': form})
    else:
        form = UserRegisterForm()
        return render(request, 'users/registration.html', {'form': form})

@login_required
def requestList(request, user_id):
    if request.method == 'GET':
        user_requested_services = ServiceRequest.objects.filter(user_id=user_id)
        return render(request, 'gus/requestedSerives.html', {'user_requests': user_requested_services})
    return render(request, 'gus/requestedSerives.html', {'user_requests': user_requested_services})




