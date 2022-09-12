from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField



class Category(models.Model):
    sub_category=models.ForeignKey('self',on_delete=models.CASCADE,related_name='scategory',blank=True,null=True)
    is_sub=models.BooleanField(default=False)
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering=('name',)
        verbose_name_plural='categories'
        verbose_name='category'


    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse ('product:category_view',args=[self.slug,])

class Product(models.Model):
    category=models.ManyToManyField(Category,related_name='cat_products')
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,unique=True)
    image=models.ImageField()
    description=RichTextField(config_name='awesome_ckeditor')
    price=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)



    class Meta:
        ordering=('name',)
      


    def __str__(self) -> str:
        return self.name



    def get_absolute_url(self):
        return reverse ('product:details',args=(self.id,self.slug))





