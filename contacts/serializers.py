from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import Contact

class ContactSerializer(ModelSerializer):

    class Meta:
        model = Contact
        fields = ['id', 'country_code', 'firstname', 'lastname', 'phone_number', 'contact_picture', 'is_favourite']