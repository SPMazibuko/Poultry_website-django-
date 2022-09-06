from django.db import models
from django.urls import reverse
from django.conf import settings

# class Appuser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='appusers')
#     USET_TYPES = (
#         ('A', 'Admin'),
#         ('C', 'Customer')
#     )
#     GENDER_CHOICES = (
#         ('M', 'MALE'),
#         ('F', 'FEMALE'),
#         ('O','OTHER')
#     )
#     user_type = models.CharField(max_length=1,choices=USET_TYPES, default='C')
#     gender = models.CharField(max_length=1,choices=GENDER_CHOICES,default='F')
#     mobile = models.PositiveIntegerField(null=True, blank=True)
#     address = models.CharField(max_length=500,null=True,blank=True)
#     city = models.CharField(max_length=250, null=True, blank=True)
#     pincode = models.PositiveIntegerField(null=True, blank=True)

#     def __str__(self):
#         return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name

class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)


# def subcategory_image(instance, filename):
#     upload_to = '{}_files/'.format(instance.category.name,instance.name)
#     ext = filename.split('.')[-1]

#     if instance.name:
#         filename = '{}_image.{}'.format(instance.name,ext)
#     return os.path.join(upload_to, filename)

# class SubCategory(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to=subcategory_image, null=True, blank=True)

#     def __str__(self):
#         return str(self.category.name)+ '-' + str(self.name)

# class Animal(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Size(models.Model):
#     subCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='subcategorySizes')
#     size = models.CharField(max_length=100)

#     def __str__(self):
#         return str(self.subCategory.name) + '-' + str(self.size)

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='images/default.png')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return self.title
