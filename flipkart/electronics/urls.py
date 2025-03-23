from django.urls import path
from electronics import views

urlpatterns = [
    path('product/', views.product_detail, name="product_detail"),
    path('update/<int:id>', views.update_product, name='update_product'),
    path("delete_product/<int:id>/", views.delete_product, name="delete_product"),
<<<<<<< HEAD
=======

>>>>>>> aee1c01f7da304bc88bb1521251d8b687b9a59a6
]