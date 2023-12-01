
#Serializers are basically used to convert complex data to native Python datatypes that can then be easily rendered 
#into JSON(Which we are going to use in React#

#for connecting front to backend

from rest_framework import serializers 
from . models import *
  
class ReactSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = React 
        fields = ['name', 'detail']

        