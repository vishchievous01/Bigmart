from django.urls import path
from WebApp import views

urlpatterns = [
    path('', views.homepage, name="Home"),
    path('About/', views.aboutpage, name="About"),
    path('Contactpage/', views.contactpage, name="contactpage"),
    path('Our_Products_Category/', views.ourproducts_cat, name="ourproducts_cat"),
    path('Our_products/', views.ourproducts, name="Our_products"),
    path('save_contact/', views.save_contact, name="save_contact"),
    path('filtered_products/<cat_name>/', views.filtered_products, name="filtered_products"),
    path('single_product/<int:pro_id>/', views.single_product, name="single_product"),
    path('categories_page/', views.categories_page, name="categories_page"),
    path('registration_page/', views.registration_page, name="registration_page"),
    path('save_user/', views.save_user, name="save_user"),
    path('Userlogin/', views.Userlogin, name="Userlogin"),
    path('Userlogout/', views.Userlogout, name="Userlogout"),
    path('AddCart/', views.AddCart, name="AddCart"),
    path('CartPage/', views.CartPage, name="CartPage"),
    path('delete_item/<int:p_id>/', views.delete_item, name="delete_item"),
    path('userloginpage/', views.userloginpage, name="userloginpage"),
    path('checkoutpage/', views.checkoutpage, name="checkoutpage"),
    path('paymentpage/', views.paymentpage, name="paymentpage"),
    path('subscribe/', views.subscribe, name="subscribe"),
    path('saveorder/', views.saveorder, name="saveorder"),

]
