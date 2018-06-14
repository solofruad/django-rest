# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework_mongoengine import viewsets as meviewsets
from ocp.models import Proceso
from ocp.serializers import ProcesoSerializer
from ocp.models import Entidad
from ocp.serializers import EntidadSerializer


class getCodigoProceso(meviewsets.ModelViewSet):
	serializer_class = ProcesoSerializer

	def get_queryset(self):
		pid = self.request.query_params.get('pid')
		queryset = Proceso.objects.filter(CodigoProceso=pid)
		return queryset


class getTipoProceso(meviewsets.ModelViewSet):
	serializer_class = ProcesoSerializer

	def get_queryset(self):
		tipo = self.request.query_params.get('tipo')
		queryset = Proceso.objects.filter(tipoProceso=tipo)
		return queryset


class getEntidadProceso(meviewsets.ModelViewSet):
	serializer_class = ProcesoSerializer

	def get_queryset(self):
		print("entidad")
		entidad = self.request.query_params.get('entidad')
		codigo_entidad = Entidad.objects.filter(Nombre=entidad)
		codigo = codigo_entidad[0].Codigo
		print(codigo)
		queryset = Proceso.objects.filter(CodigoEntidad=codigo)
		return queryset




class getListProceso(meviewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    lookup_field = 'id'
    queryset = Proceso.objects.all()
    serializer_class = ProcesoSerializer

