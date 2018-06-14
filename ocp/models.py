# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.db import models
from mongoengine import Document, EmbeddedDocument, fields

# Create your models here.


class Proceso(Document):
	CodigoProceso = fields.StringField()
	Cuantia = fields.DynamicField()
	CodigoEntidad = fields.StringField()
	tipoProceso  = fields.StringField()
	estadoProceso = fields.StringField()

class Entidad(Document):
	Codigo = fields.StringField()
	Nombre = fields.StringField()	

