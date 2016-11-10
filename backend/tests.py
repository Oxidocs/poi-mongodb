from django.test import TestCase
from models import Coordenadas, Point
from django.db.models import F,Q

# save
# Coordenadas(lugar_id="5823dcea9478400ffc5d0ee1", location=Point(latitude='0.0',longtitude='0.0')).save()

#read
# coor = Coordenadas.objects.raw_query({'location' : {"latitude" : 0,"longtitude" : 0}})
#print coor

coor = Coordenadas.objects.filter(id="5823e55894784013eba23d3c").first()
print coor.location

#update
coor = Coordenadas.objects.filter(id="5823e55894784013eba23d3c").first()
coor.location = Point(latitude='-29.983333',longtitude='-70.683333')
coor.save()