from rest_framework import serializer
from rest_framework import item

class itemSerializer(Serializers.ModelSerializer):
    class Meta:
        model =item
        fields=('oil','gas','brine')

    fields ='__all__'
