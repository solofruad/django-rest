from rest_framework_mongoengine import serializers
from ocp.models import Proceso, Entidad


class ProcesoSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Proceso        
        fields = '__all__'    


class EntidadSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Entidad        
        fields = '__all__'    