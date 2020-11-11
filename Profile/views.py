from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response


from Profile.models import ProfileModel
from Profile.serializers import ProfileModelSerializers

class ProfileModelView(APIView):
    def post (self,request, format=None):
        serializer = ProfileModelSerializers(data= request.data, context = {'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response('Error')
    def get(self,request):
        profile = ProfileModel.objects.all()
        profile_json = ProfileModelSerializers(profile,many=True)
        return Response(profile_json.data)
    
# Create your views here.
