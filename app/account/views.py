from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
import json
from django.views.generic import ListView , DetailView ,View,TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import *
from .models import User
 
class SignUpView(ListView):
    model = User
    form_class = SignUpForm
    template_name = 'registration/signup.html'

    def get(self,request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            user.is_active = True #u need to deactivate account till it is confirmed
            user.save()

            #create_custom_user_profile
            # Profile.objects.get_or_create(user=user)

            # current_site = get_current_site(request)
            # site = current_site.domain
            # subject = 'Activate Your %(site) Account'
            # message = render_to_string('registration/account_activation_email.html', {
            #     'user': user,
            #     'domain': site,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': account_activation_token.make_token(user),
            # })
            # user.email_user(subject, message)

            # messages.success(request, (''))
            # messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))

            return redirect('login')

        return render(request, self.template_name, {'form': form})

class HomeView(TemplateView):
    template_name = 'index.html'

class AdminIndexView(TemplateView):
    template_name = "admin/farmers/index.html"

class AdminAccountView(DetailView):
    model = User
    template_name = 'admin/farmers/account.html'
   
class AdminAccountEditView(DetailView):
    model = User
    form_class = UserEditForm
    template_name = 'admin/farmers/account-edit.html'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context["form"] = self.form_class(instance=user)
        return context 

    def post(self, request,*args, **kwargs ):
        form = self.form_class(request.POST,request.FILES,instance=self.get_object())
        print(form)
        if form.is_valid():
            form.save()
            return redirect(self.get_object().get_absolute_url())
        return redirect(self.get_object().get_edit_url())

class AdminAccountDeleteView(DeleteView):
    pass

class UserDevices(ListView):
    model = Controller
    form_class = AddDeviceForm
    template_name = 'admin/farmers/devices.html'

    def get(self,request, *args, **kwargs):
        usr_id = self.request.user.id
        context= {
            'active_objects' : Controller.objects.filter(client__id=usr_id,is_active=True ),
            'inactive_objects' : Controller.objects.filter(client__id=usr_id,is_active=False),
            'form' : self.form_class()
        }
        return render(request, self.template_name,context)

    def post(self, request, *args, **kwargs):
        usr_id = self.request.user.id
        objects = Controller.objects.filter(client__id=usr_id)
        form = self.form_class(request.POST)
        if form.is_valid():

            device = form.save(commit=False)
            device.client = self.request.user
            device.save()
            return redirect('account:devices')
        return redirect('account:devices')



