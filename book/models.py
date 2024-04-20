from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='images/icon')
    slug = models.SlugField(max_length=100, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Categories'
    
class Service(models.Model):
    STATUS_CHOICES =(
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )
    title = models.CharField(max_length=256)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    category = models.ManyToManyField(Category, related_name='services')
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/', blank=True)
    image3 = models.ImageField(upload_to='images/', blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    available_start = models.DateField()
    available_end = models.DateTimeField(auto_now=True, editable=False)
    address = models.CharField(max_length=200)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='pending')

    @property
    def is_available(self):
        now = timezone.now()
        return self.available_start <= now < self.available_end

    def __str__(self):
        return f"{self.title} by {self.publisher}"
    
    def get_absolute_url(self):
        return reverse("book:service", args=[self.slug])
    
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # customer who booked the service
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    service_desc = models.TextField()
    location = models.CharField(max_length=256)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.user.username} - {self.service.title}"




