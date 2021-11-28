from django.urls import path
from .views import ContactsDetailView, Contactslist

urlpatterns = [
    path('', Contactslist.as_view()),
    path('<int:id>', ContactsDetailView.as_view()),
]
