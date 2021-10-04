from . import views
from django.urls import path


app_name = 'dadova'
urlpatterns = [
	path('register/', views.register, name='register'),
	path('login/', views.user_login, name='login'),
	path('', views.home, name='home'),
	path('all_products/', views.all_products, name='all_products'),
	path('<int:prod_id>/', views.detail, name='detail'),
	path('<int:prod_id>/add_to_cart/', views.add_to_cart, name='add_to_cart'),
	path('<int:prod_id>/leave_review/', views.leave_review, name='leave_review'),
	path('reviews/<int:prod_id>/', views.reviews, name='reviews'),
	path('categories/', views.show_categories, name='categories'),
	path('category/<str:slug>/', views.show_category_products, name='show_category_products'),
	path('cart/', views.cart, name='cart'),
	path('about/', views.about, name='about'),
]