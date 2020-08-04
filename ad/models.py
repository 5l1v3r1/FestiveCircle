from django.db import models
from PIL import Image as PILImage
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model as user_model
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO,StringIO
User = user_model()

class Location(models.Model):

	city = models.CharField( max_length=100)
	area = models.CharField( max_length=100)
	street = models.CharField( max_length=100)
	latitude = models.CharField( max_length=100)
	longitude = models.CharField( max_length=100)

	class Meta:
		verbose_name = "Location"
		verbose_name_plural = "Locations"

	def __str__(self):
		return '%s, %s, %s' % (self.street, self.area, self.city)

	def get_absolute_url(self):
		return reverse("Location_detail", kwargs={"pk": self.pk})

class Detail(models.Model):

	hotel_rating_choices  = (
		(1,1),
		(2,2),
		(3,3),
		(4,4),
		(5,5),
	)
	stat = (
		("Pending", "Pending"),
		("Active", "Active"),
		("Deactive", "Deactive"),
		("Expire", "Expire"),
	)
	
	title = models.CharField(max_length=100)
	loction_id = models.ForeignKey(Location, verbose_name="Location", on_delete=models.CASCADE)
	postDate = models.DateTimeField(default=timezone.now)
	featured = models.BooleanField(default=False)
	description = models.TextField()
	rating = models.IntegerField(choices=hotel_rating_choices, default=1)
	views = models.IntegerField(default=0)
	status = models.CharField( choices=stat, max_length=50, default="Active")
	expiryDate = models.DateTimeField()
	
	class Meta:
		verbose_name = "Detail"
		verbose_name_plural = "Details"

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("Detail_detail", kwargs={"pk": self.pk})


def upload_location(instance, filename):
    return "%s/%s/%s/%s" % ('Ads',instance.detail_id.loction_id.city,instance.detail_id.title, filename)


class images(models.Model):

	title = models.CharField(max_length=100)
	detail_id = models.ForeignKey(Detail, verbose_name="Detail", on_delete=models.CASCADE)
	image = models.ImageField(upload_to=upload_location,
							null=True,
							blank=True,
							default='model/def.jfif'
							)
	class Meta:
		verbose_name = "Image"
		verbose_name_plural = "Images"

	def save(self, *args, **kwargs):
		if self.image:
			img = PILImage.open( BytesIO( self.image.read() ) )
			width, height = 811, 608
			img.thumbnail( (width, height), PILImage.ANTIALIAS )
			save_buff = BytesIO()
			img2 = PILImage.open('media/watermark.png')
			img2.convert('RGBA')
			img.convert('RGBA')
			img.paste(img2, (0, 20), img2)

			img.save( save_buff,format='JPEG', optimize=True, quality=100)
			self.image = InMemoryUploadedFile( save_buff, 'ImageField', "%s" %self.title, 'image/jpeg',save_buff.__le__,  None )
		super( images, self ).save( *args, **kwargs )




class Venue(models.Model):

	STATUS_CHOICES = (
		("Banquet Hall", "Banquet Hall"),
		("Marquee", "Marquee"),
		("Hotel Hall", "Hotel Hall"),
		("Farmhouse", "Farmhouse"),
		("Lawn", "Lawn")
	)
	author =models.ForeignKey(User, on_delete=models.CASCADE)
	detail_id = models.ForeignKey(Detail, verbose_name="Detail", on_delete=models.CASCADE)
	sitting_capacity = models.IntegerField()
	category = models.CharField(choices=STATUS_CHOICES,max_length=50, default="Banquet Hall") 
	parking_capacity = models.IntegerField()
	air_conditioner = models.BooleanField(default=False, blank=True, null=True)
	heater = models.BooleanField(default=False, blank=True, null=True)
	dj_system = models.BooleanField(default=False, blank=True, null=True)
	wifi = models.BooleanField(default=False, blank=True, null=True)
	bridal_room = models.BooleanField(default=False, blank=True, null=True)
	valet_parking = models.BooleanField(default=False, blank=True, null=True)
	decoration = models.BooleanField(default=False, blank=True, null=True)
	generator = models.BooleanField(default=False, blank=True, null=True)
	outside_catering = models.BooleanField(default=False, blank=True, null=True)
	outside_dj = models.BooleanField(default=False, blank=True, null=True)
	outside_decoration = models.BooleanField(default=False, blank=True, null=True)
	bridal_makeup = models.BooleanField(default=False, blank=True, null=True)
	

	class Meta:
		verbose_name = "Venue"
		verbose_name_plural = "Venues"

	def get_absolute_url(self):
		return reverse("_detail", kwargs={"pk": self.pk})

class VenuePrice(models.Model):

	venue_id = models.ForeignKey(Venue, verbose_name="Venue", on_delete=models.CASCADE)
	per_guest = models.IntegerField(blank=True, null=True)
	heater = models.IntegerField(blank=True, null=True)
	dj_system = models.IntegerField(blank=True, null=True)
	decoration = models.IntegerField(blank=True, null=True)
	wifi = models.IntegerField(blank=True, null=True) 
	bridal_room = models.IntegerField(blank=True, null=True) 
	valet_parking = models.IntegerField(blank=True, null=True) 
	outside_catering = models.IntegerField(blank=True, null=True)
	air_conditioner = models.IntegerField(blank=True, null=True)
	generator = models.IntegerField(blank=True, null=True)
	outside_dj = models.IntegerField(blank=True, null=True)
	outside_decoration = models.IntegerField(blank=True, null=True)
	bridal_makeup = models.IntegerField(blank=True, null=True)
	class Meta:
		verbose_name = "Venue Price"
		verbose_name_plural = "Venue Prices"
	def get_absolute_url(self):
		return reverse("VenuePrice_detail", kwargs={"pk": self.pk})

class Dish_Menu(models.Model):

	venue_id = models.ForeignKey(Venue, verbose_name="Venue", on_delete=models.CASCADE)
	title = models.CharField( max_length=100)
	description = models.TextField()
	price = models.IntegerField()

	class Meta:
		verbose_name = "Dish Menu"
		verbose_name_plural = "Dish Menus"

	def __str__(self):
		return str(self.price)

	def get_absolute_url(self):
		return reverse("Dish_Menu_detail", kwargs={"pk": self.pk})


class contact(models.Model):
	detail_id = models.ForeignKey(Detail, verbose_name="Detail", on_delete=models.CASCADE)
	name = models.CharField( max_length=30,blank=True, null=True)
	phone = models.CharField( max_length=30,blank=True, null=True)	





