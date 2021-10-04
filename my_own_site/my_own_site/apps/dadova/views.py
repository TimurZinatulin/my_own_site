from .forms import UserRegistrationForm, LoginForm
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .models import Product, Cart, Review, Category


count = Cart.objects.get().products.count()


c = Category.objects.all()


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'dadova/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'dadova/register.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'dadova/login_done.html', {'user': user})
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'dadova/login.html', {'form': form})


def home(request):

	products = Product.objects.order_by('id')[:6]

	return render(request, 'base.html', {'products': products, 'count': count, 'categories': c})


def about(request):

	return render(request, 'dadova/about.html')


def all_products(request):

	products = Product.objects.all()

	return render(request, 'dadova/all_products.html', {'products': products, 'count': count, 'categories': c})


def detail(request, prod_id):

	try:
		p = Product.objects.get(id=prod_id)
	except:
		raise Http404()

	return render(request, 'dadova/detail.html', {'product': p, 'count': count, 'categories': c})


def add_to_cart(request, prod_id):

	try:
		p = Product.objects.get(id=prod_id)
		c = Cart.objects.get()
	except:
		raise Http404()

	c.products.add(p)
	return HttpResponseRedirect(reverse('dadova:detail', args=(p.id, )))


def leave_review(request, prod_id):

	try:
		p = Product.objects.get(id=prod_id)
	except:
		raise Http404()

	p.review_set.create(text=request.POST['text'])
	return HttpResponseRedirect(reverse('dadova:detail', args=(p.id, )))


def reviews(request, prod_id):

	prod_reviews = Product.objects.get(id=prod_id).review_set.all()

	return render(request, 'dadova/reviews_page.html', {'reviews': prod_reviews, 'count': count, 'categories': c})


def show_categories(request):

	c = Category.objects.all()

	return render(request, 'dadova/categories.html', {'categories': c, 'count': count})


def show_category_products(request, slug):

	try:
		c = Category.objects.get(slug=slug)
	except:
		raise Http404()

	cat_products = c.product_set.all()

	categories = Category.objects.all()

	return render(request, 'dadova/category_products.html', {'cat_products': cat_products, 'count': count, 'categories': categories});


def cart(request):

	cart_products = Cart.objects.get().products.all()
	
	return render(request, 'dadova/cart.html', {'cart_products': cart_products, 'count': count, 'categories': c})