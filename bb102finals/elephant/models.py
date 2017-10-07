from django.db import models
from django.utils import timezone


# Create your models here.


class maplist(models.Model):	
	mapName = models.CharField(max_length=60, null=False)	
	mapDesc = models.TextField(null=False)	
	mapLat = models.CharField(max_length=20, null=False)
	mapLng =  models.CharField(max_length=20, null=False)	
	mapTel = models.CharField(max_length=20, null=False)
	mapAddr = models.CharField(max_length=60, null=False)

	def __str__(self):		
		return self.mapName	


class daanburglar(models.Model):	
	mapName = models.CharField(max_length=60, null=False)	
	# mapDesc = models.TextField(null=False)	
	mapLat = models.CharField(max_length=20, null=False)
	mapLng =  models.CharField(max_length=20, null=False)	
	id = models.IntegerField(null=False,primary_key=True)
	mapAddr = models.CharField(max_length=60, null=False)
	mapcityID = models.CharField(max_length=20, null=False)

	def __str__(self):		
		return self.mapName


class daanpets(models.Model):	
	mapName = models.CharField(max_length=60, null=False)	
	# mapDesc = models.TextField(null=False)	
	mapLat = models.CharField(max_length=20, null=False)
	mapLng =  models.CharField(max_length=20, null=False)	
	id = models.IntegerField(null=False,primary_key=True)
	mapAddress = models.CharField(max_length=60, null=False)
	mapcityID = models.CharField(max_length=20, null=False)

	def __str__(self):		
		return self.mapName

class daangogoro(models.Model):	
	mapName = models.CharField(max_length=60, null=False)	
	# mapDesc = models.TextField(null=False)	
	mapLat = models.CharField(max_length=20, null=False)
	mapLng =  models.CharField(max_length=20, null=False)	
	id = models.IntegerField(null=False,primary_key=True)
	mapAddress = models.CharField(max_length=60, null=False)
	mapcityID = models.CharField(max_length=20, null=False)

	def __str__(self):		
		return self.mapName

class daannoise(models.Model):	
	mapName = models.CharField(max_length=60, null=False)	
	# mapDesc = models.TextField(null=False)	
	mapLat = models.CharField(max_length=20, null=False)
	mapLng =  models.CharField(max_length=20, null=False)	
	id = models.IntegerField(null=False,primary_key=True)
	mapAddress = models.CharField(max_length=60, null=False)
	mapcityID = models.CharField(max_length=20, null=False)

	def __str__(self):		
		return self.mapName
class daantemple(models.Model):	
	mapName = models.CharField(max_length=60, null=False)	
	# mapDesc = models.TextField(null=False)	
	mapLat = models.CharField(max_length=20, null=False)
	mapLng =  models.CharField(max_length=20, null=False)	
	id = models.IntegerField(null=False,primary_key=True)
	mapAddress = models.CharField(max_length=60, null=False)
	mapcityID = models.CharField(max_length=20, null=False)

	def __str__(self):		
		return self.mapName
class daannarrowroadway(models.Model):	
	mapName = models.CharField(max_length=60, null=False)	
	# mapDesc = models.TextField(null=False)	
	mapLat = models.CharField(max_length=20, null=False)
	mapLng =  models.CharField(max_length=20, null=False)	
	id = models.IntegerField(null=False,primary_key=True)
	mapAddress = models.CharField(max_length=60, null=False)
	mapcityID = models.CharField(max_length=20, null=False)

	def __str__(self):		
		return self.mapName
class daanpolice(models.Model):	
	mapName = models.CharField(max_length=60, null=False)	
	# mapDesc = models.TextField(null=False)	
	mapLat = models.CharField(max_length=20, null=False)
	mapLng =  models.CharField(max_length=20, null=False)	
	id = models.IntegerField(null=False,primary_key=True)
	mapAddress = models.CharField(max_length=60, null=False)
	mapcityID = models.CharField(max_length=20, null=False)

	def __str__(self):		
		return self.mapName
class daanfiredepart(models.Model):	
	mapName = models.CharField(max_length=60, null=False)	
	# mapDesc = models.TextField(null=False)	
	mapLat = models.CharField(max_length=20, null=False)
	mapLng =  models.CharField(max_length=20, null=False)	
	id = models.IntegerField(null=False,primary_key=True)
	mapAddress = models.CharField(max_length=60, null=False)
	mapcityID = models.CharField(max_length=20, null=False)

	def __str__(self):		
		return self.mapName


class daanfuneral(models.Model):	
	mapName = models.CharField(max_length=60, null=False)	
	# mapDesc = models.TextField(null=False)	
	mapLat = models.CharField(max_length=20, null=False)
	mapLng =  models.CharField(max_length=20, null=False)	
	id = models.IntegerField(null=False,primary_key=True)
	mapAddress = models.CharField(max_length=60, null=False)
	mapcityID = models.CharField(max_length=20, null=False)

	def __str__(self):		
		return self.mapName
class daanmarkets(models.Model):	
	mapName = models.CharField(max_length=60, null=False)	
	# mapDesc = models.TextField(null=False)	
	mapLat = models.CharField(max_length=20, null=False)
	mapLng =  models.CharField(max_length=20, null=False)	
	id = models.IntegerField(null=False,primary_key=True)
	mapAddress = models.CharField(max_length=60, null=False)
	mapcityID = models.CharField(max_length=20, null=False)

	def __str__(self):		
		return self.mapName
class daangas(models.Model):	
	mapName = models.CharField(max_length=60, null=False)	
	# mapDesc = models.TextField(null=False)	
	mapLat = models.CharField(max_length=20, null=False)
	mapLng =  models.CharField(max_length=20, null=False)	
	id = models.IntegerField(null=False,primary_key=True)
	mapAddress = models.CharField(max_length=60, null=False)
	mapcityID = models.CharField(max_length=20, null=False)

	def __str__(self):		
		return self.mapName
			# mapUrl varchar,\
            # mapName varchar,\
            # mapAddress varchar,\
            # mapLat varchar,\
            # mapLng varchar,\
            # mapcityID varchar,\
            # mapLabel varchar,\
            # mapRent varchar,\
            # mapLandlord varchar,\
            # mapSpace varchar,\
            # mapPet varchar,\
            # mapSex varchar,\
            # mapCook varchar,\
            # mapSmoke varchar,\
class daanpets10000(models.Model):
	id = models.IntegerField(null=False,primary_key=True)	
	mapUrl = models.CharField(max_length=60, null=False)
	mapName = models.CharField(max_length=60, null=False)	
	mapAddress = models.CharField(max_length=60, null=False)
	mapLat = models.CharField(max_length=20, null=False)
	mapLng =  models.CharField(max_length=20, null=False)
	mapcityID = models.CharField(max_length=5, null=False)	
	mapLabel = models.CharField(max_length=5, null=False)	
	mapRent = models.CharField(max_length=10, null=False)	
	mapLandlord = models.CharField(max_length=60, null=False)	
	mapSpace = models.CharField(max_length=10, null=False)	
	mapPet = models.CharField(max_length=5, null=False)	
	mapSex = models.CharField(max_length=5, null=False)	
	mapCook = models.CharField(max_length=5, null=False)
	mapAvgonfood = models.CharField(max_length=5, null=False)
	mapSmoke = models.CharField(max_length=5, null=False)	
	def __str__(self):		
		return self.mapName
class daanpetsall(models.Model):
	id = models.IntegerField(null=False,primary_key=True)	
	mapUrl = models.CharField(max_length=60, null=False)
	mapName = models.CharField(max_length=60, null=False)	
	mapAddress = models.CharField(max_length=60, null=False)
	mapLat = models.CharField(max_length=20, null=False)
	mapLng =  models.CharField(max_length=20, null=False)
	mapcityID = models.CharField(max_length=5, null=False)	
	mapLabel = models.CharField(max_length=5, null=False)	
	mapRent = models.CharField(max_length=10, null=False)	
	mapLandlord = models.CharField(max_length=60, null=False)	
	mapSpace = models.CharField(max_length=10, null=False)	
	mapPet = models.CharField(max_length=5, null=False)	
	mapSex = models.CharField(max_length=5, null=False)	
	mapCook = models.CharField(max_length=5, null=False)
	mapAvgonfood = models.CharField(max_length=5, null=False)
	mapSmoke = models.CharField(max_length=5, null=False)	
	def __str__(self):		
		return self.mapName
class daanroomtest(models.Model):
	id = models.IntegerField(null=False,primary_key=True)	
	mapUrl = models.CharField(max_length=60, null=False)
	mapName = models.CharField(max_length=60, null=False)	
	mapAddress = models.CharField(max_length=60, null=False)
	mapLat = models.CharField(max_length=20, null=False)
	mapLng =  models.CharField(max_length=20, null=False)
	mapcityID = models.CharField(max_length=5, null=False)	
	mapLabel = models.CharField(max_length=5, null=False)	
	mapRent = models.CharField(max_length=10, null=False)	
	mapLandlord = models.CharField(max_length=60, null=False)	
	mapSpace = models.CharField(max_length=10, null=False)	
	mapPet = models.CharField(max_length=5, null=False)	
	mapSex = models.CharField(max_length=5, null=False)	
	mapCook = models.CharField(max_length=5, null=False)
	mapSmoke = models.CharField(max_length=5, null=False)		
	def __str__(self):		
		return self.mapName


class tucheng5km10000(models.Model):
	id = models.IntegerField(null=False,primary_key=True)	
	mapUrl = models.CharField(max_length=60, null=False)
	mapName = models.CharField(max_length=60, null=False)	
	mapAddress = models.CharField(max_length=60, null=False)
	mapLat = models.CharField(max_length=20, null=False)
	mapLng =  models.CharField(max_length=20, null=False)
	mapcityID = models.CharField(max_length=5, null=False)	
	mapLabel = models.CharField(max_length=5, null=False)	
	mapRent = models.CharField(max_length=10, null=False)	
	mapLandlord = models.CharField(max_length=60, null=False)	
	mapSpace = models.CharField(max_length=10, null=False)	
	mapPet = models.CharField(max_length=5, null=False)	
	mapSex = models.CharField(max_length=5, null=False)	
	mapCook = models.CharField(max_length=5, null=False)
	mapAvgonfood = models.CharField(max_length=5, null=False)
	mapSmoke = models.CharField(max_length=5, null=False)	
	def __str__(self):		
		return self.mapName
class tucheng3km10000(models.Model):
	id = models.IntegerField(null=False,primary_key=True)	
	mapUrl = models.CharField(max_length=60, null=False)
	mapName = models.CharField(max_length=60, null=False)	
	mapAddress = models.CharField(max_length=60, null=False)
	mapLat = models.CharField(max_length=20, null=False)
	mapLng =  models.CharField(max_length=20, null=False)
	mapcityID = models.CharField(max_length=5, null=False)	
	mapLabel = models.CharField(max_length=5, null=False)	
	mapRent = models.CharField(max_length=10, null=False)	
	mapLandlord = models.CharField(max_length=60, null=False)	
	mapSpace = models.CharField(max_length=10, null=False)	
	mapPet = models.CharField(max_length=5, null=False)	
	mapSex = models.CharField(max_length=5, null=False)	
	mapCook = models.CharField(max_length=5, null=False)
	mapAvgonfood = models.CharField(max_length=5, null=False)
	mapSmoke = models.CharField(max_length=5, null=False)	
	def __str__(self):		
		return self.mapName
class tucheng5km(models.Model):
	id = models.IntegerField(null=False,primary_key=True)	
	mapUrl = models.CharField(max_length=60, null=False)
	mapName = models.CharField(max_length=60, null=False)	
	mapAddress = models.CharField(max_length=60, null=False)
	mapLat = models.CharField(max_length=20, null=False)
	mapLng =  models.CharField(max_length=20, null=False)
	mapcityID = models.CharField(max_length=5, null=False)	
	mapLabel = models.CharField(max_length=5, null=False)	
	mapRent = models.CharField(max_length=10, null=False)	
	mapLandlord = models.CharField(max_length=60, null=False)	
	mapSpace = models.CharField(max_length=10, null=False)	
	mapPet = models.CharField(max_length=5, null=False)	
	mapSex = models.CharField(max_length=5, null=False)	
	mapCook = models.CharField(max_length=5, null=False)
	mapAvgonfood = models.CharField(max_length=5, null=False)
	mapSmoke = models.CharField(max_length=5, null=False)	
	def __str__(self):		
		return self.mapName