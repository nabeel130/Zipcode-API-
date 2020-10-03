from django.db import models
# import request

# Create your models here.
class Location(models.Model):
    zip_code = models.IntegerField()
    latitude = models.DecimalField(blank=True , max_digits=9 , decimal_places=6)
    longitude = models.DecimalField(blank=True , max_digits=9 , decimal_places=6)

    def __str__(self):
        return str(self.zip_code)


    def save(self,*args,**kwargs):
        # r = request.get(f'https://public.opendatasoft.com/api/records/1.0/search/?dataset=us-zip-code-latitude-and-longitude&q=&facet=state&facet=timezone&facet=dst')
        self.latitude = 123.456
        self.longitude = 123.456

        super().save(*args , **kwargs)