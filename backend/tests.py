from django.test import TestCase
from models import Coordenadas, Point, Lugares, Ciudades
from django.db.models import F,Q

#list
# empresa = Empresas(ciudad=['La Serena','Coquimbo'])
# empresa.save()

# save
# Coordenadas(lugar_id="5823dcea9478400ffc5d0ee1", location=Point(latitude='0.0',longtitude='0.0')).save()

#read
# coor = Coordenadas.objects.raw_query({'location' : {"latitude" : 0,"longtitude" : 0}})
#print coor

# coor = Coordenadas.objects.filter(id="5823e55894784013eba23d3c").first()
# print coor.location

#update
# coor = Coordenadas.objects.filter(id="5823e55894784013eba23d3c").first()
# coor.location = Point(latitude='-29.983333',longtitude='-70.683333')
# coor.save()

# Lugares(nombre_espanol="Mamalluca", categoria_id='5824dd839478400f4e000dac',ciudad=Ciudades(nombre_espanol='Vicuña')).save()

# lugar = Lugares.objects.filter(id="5824de939478400fd82b9661").first()
# lugar.ciudad=Ciudades(nombre_espanol='Vicuña', pais_id='5824e19b947840100290769e')
# lugar.save()

lugar = Lugares.objects.filter(id="582f717a9478400faf64ecef").first()
lugar.location = Point(latitude='-29.983333',longtitude='-70.683333')
lugar.save()
