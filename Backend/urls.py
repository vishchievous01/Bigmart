from django.urls import path
from Backend import views

urlpatterns = [
    path('index_page/', views.index_page, name="index_page"),
    path('category_page/', views.category_page, name="category_page"),
    path('save_category/', views.save_category, name="save_category"),
    path('display_category/', views.display_category, name="display_category"),
    path('edit_category/<int:catid>', views.edit_category, name="edit_category"),
    path('update_category/<int:catid>', views.update_category, name="update_category"),
    path('delete_category/<int:catid>', views.delete_category, name="delete_category"),
    path('login_page/', views.login_page, name="login_page"),
    path('admin_page/', views.admin_page, name="admin_page"),
    path('AdminLogout/', views.AdminLogout, name="AdminLogout"),
    path('admin/edit-image/', views.edit_admin_image, name='edit_admin_image'),
    path('dashboard_page/', views.dashboard_page, name='dashboard_page'),
    path('admin_profile_view/', views.admin_profile_view, name='admin_profile_view'),
    path('product_page/', views.product_page, name="product_page"),
    path('save_product/', views.save_product, name="save_product"),
    path('display_product/', views.display_product, name="display_product"),
    path('edit_product/<int:proid>/', views.edit_product, name="edit_product"),
    path('delete_product/<int:proid>/', views.delete_product, name="delete_product"),
    path('update_product/<int:proid>/', views.update_product, name="update_product"),
    path('contact_details', views.contact_details, name="contact_details"),
    path('delete_contact/<int:delid>/', views.delete_contact, name="delete_contact"),
]
