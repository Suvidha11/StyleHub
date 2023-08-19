from django.db import models
import uuid
from autoslug import AutoSlugField
from accounts.models import User


class base_model(models.Model):
     uid=models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
     
     class Meta:
        abstract=True
         
  
#size_varient model  
class size_varient(base_model):
    size_name=models.CharField(max_length=20) 
    
    def __str__(self):
        return self.size_name 
     
#clour_varient model 
class  colour_varient(base_model):
    colour_name=models.CharField(max_length=50) 
    
    def __str__(self):
            return self.colour_name
     
#product model
class products(base_model):
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='product_name',null=True,blank=True,unique=True)
    price=models.IntegerField()
    product_disc=models.TextField()
    image=models.ImageField(upload_to='product_image')
    size=models.ManyToManyField(size_varient)
    colour=models.ManyToManyField(colour_varient,blank=True)
    
    
