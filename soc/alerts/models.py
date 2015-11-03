from django.db import models

class PollutantionData(models.Model):
	name = models.CharField(max_length=5)
	date = models.DateField()
	DAILY_AQI_VALUE = models.IntegerField(max_length=2)
	COUNTY_CODE = models.IntegerField(max_length=2)
	COUNTY = models.IntegerField(max_length=2)
	SITE_LATITUDE = models.FloatField(max_length=5)
	SITE_LONGITUDE = models.FloatField(max_length=5)
