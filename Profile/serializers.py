from Profile.models import ProfileModel
from rest_framework import serializers 

class ProfileModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('__all__')
