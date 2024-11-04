from rest_framework.generics import *
from api.models import *
from .serializers import *
from rest_framework import permissions

# Test Api
class TestApiView(ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Test.objects.all()
    serializer_class = Testserializer
class TestApiCreate(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Test.objects.all()
    serializer_class = Testserializer
class TestApiUpdate(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Test.objects.all()
    serializer_class = Testserializer