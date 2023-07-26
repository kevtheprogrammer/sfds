from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
import json
from django.views.generic import ListView , DetailView ,View,TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import SignUpForm,SignEditForm
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
    # form_class = ProductForm 

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["category"] = Category.objects.all() 
    #     context["form"] = ProductForm() 
    #     context["product_list_4"] = Product.objects.all()[:4] 
    #     context["order_5"] = Order.objects.all()[:7] 
    #     context["stock_5"] = StockModel.objects.all()[:7] 
    #     context["tags"] = Tag.objects.all() 
    #     return context 
    
    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST,request.FILES)
    #     if form.is_valid():
    #         instance = form.save(commit=False)
    #         instance.author = request.user 
    #         instance.save()
    #         return redirect('account:products')
    #     return redirect('account:dashboard')

class AdminAccountView(CreateView):
    model = User
    form_class = SignEditForm
    template_name = 'admin/farmers/account.html'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context["form"] = self.form_class(instance=user)
        return context 


class AdminAccountEditView(UpdateView):
    model = User
    form_class = SignEditForm
    template_name = 'admin/farmers/account-edit.html'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context["form"] = self.form_class(instance=user)
        return context 




class AdminAccountDeleteView(DeleteView):
    pass
 
# class ProductDetailView(DetailView):
#     model = Product
#     template_name = "mngmnt/prod_details.html"
#     form_class = ProductForm
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["category"] = Category.objects.all() 
#         context["form"] =  self.form_class()
#         context["forms"] = ProductForm(instance=self.get_object()) 
#         context["object_list_3"] = Product.objects.all()[:3] 
#         context["tags"] = Tag.objects.all() 
#         return context 
    
#     def post(self,request, *args, **kwargs):
#         obj = self.get_object()
#         forms = self.form_class(request.POST,request.FILES,instance=self.get_object())
#         if forms.is_valid():
#             forms.save()
#         return redirect(obj.get_absolute_url_admin())

# class OrderListView(ListView):
#     model = Order
#     template_name = "mngmnt/orders.html"
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["category"] = Category.objects.all() 
#         context["form"] = ProductForm() 
#         context["object_list_3"] = Product.objects.all()[:3] 
#         context["tags"] = Tag.objects.all() 
#         return context 

# class OrderDetailView(DeleteView):
#     model = Order
#     template_name = 'mngmnt/order_details.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["category"] = Category.objects.all() 
#         context["order_forms"] = OrderForm(instance=self.get_object()) 
#         context["object_list_3"] = Product.objects.all()[:3] 
#         context["tags"] = Tag.objects.all() 
#         return context 
    
#     def post(self, *args,**kwargs):
#         order_forms = OrderForm(self.request.POST,instance=self.get_object(), )  
#         if order_forms.is_valid():
#             order_forms.save()
#         return redirect(self.get_object().view_order_url())

# class WatchListView(ListView):
#     model = Product
#     template_name = "mngmnt/watch.html"
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["category"] = Category.objects.all() 
#         context["form"] = ProductForm() 
#         context["object_list_3"] = Product.objects.all()[:3] 
#         context["tags"] = Tag.objects.all() 
#         return context 

# class StockListView(ListView):
#     model = StockModel
#     template_name = "mngmnt/stock.html"
#     form_class = StockForm
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["category"] = Category.objects.all() 
#         context["form"] = ProductForm() 
#         context["add_stock_form"] = self.form_class() 
#         context["object_list_3"] = Product.objects.all()[:3] 
#         context["tags"] = Tag.objects.all() 
#         return context 

#     def post(self,request, *args, **kwargs):
#         add_stock_form = self.form_class(request.POST)
#         if add_stock_form.is_valid():
#             add_stock_form.save()
#         return redirect('account:stock')


# class StockDetailView(DeleteView):
#     model = StockModel
#     form_class = StockEditForm
#     template_name = 'mngmnt/stock_details.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["category"] = Category.objects.all() 
#         context["add_stock_form"] = self.form_class(instance=self.get_object()) 
#         context["object_list_3"] = Product.objects.all()[:3] 
#         context["tags"] = Tag.objects.all() 
#         return context 
    
#     def post(self,request, *args,**kwargs):
#         obj = self.get_object()
#         add_stock_form = self.form_class(request.POST,instance=obj)   
#         if add_stock_form.is_valid():
#             add_stock_form.save()
#         return redirect(obj.get_absolute_url())

