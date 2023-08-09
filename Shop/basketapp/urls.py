from django.urls import path

from basketapp.views import basket_add, basket_edit, basket_remove, ordered

app_name = 'basket'

urlpatterns = [
    path('add/<int:book_id>/', basket_add, name='basket_add'),
    path('edit/<int:basket_id>/<int:quantity>/', basket_edit, name='basket_edit'),
    path('remove/<int:basket_id>', basket_remove, name='basket_remove'),
    path('ordered/', ordered, name='ordered'),
]
