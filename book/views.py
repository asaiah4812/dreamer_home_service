from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .filters import ServiceFilter
from book.forms import BookingForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request, slug=None):
    services_filter = ServiceFilter(request.GET, queryset=Service.objects.all())
    services = services_filter.qs
    categories = Category.objects.all()
    context = {
        'services':services,
        'categories':categories
    }

    return render(request, 'book/index.html', context)
@login_required
def service_detail(request, service):
    service = get_object_or_404(Service, slug=service)
    publisher = service.publisher
    services = Service.objects.filter(publisher=publisher)
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            messages.success(request, 'Booking saved successfully')
            return redirect('book:home')
        else:
            messages.error(request, 'something went wrong')
    else:
        form = BookingForm()

    context = {
        'service':service,
        'services':services,
        'form':form
    }

    return render(request, 'book/service_detail.html', context)

def category(request, category=None):
    if category:
        services = Service.objects.filter(category__slug=category)
        category = get_object_or_404(Category, slug=category)
    else:
        services = Service.objects.all()

    context = {
        'services': services,
        'category':category
    }
        
    return render(request, 'book/categories.html', context)

def all_booking(request):
    # book = Booking
    # publisher = book.publisher
    bookings = Booking.objects.filter(user=request.user).order_by('-date')
    context = {
        'bookings':bookings,
    }
    return render(request, 'book/all_booking.html', context)

# def category_list(request)

# def booking(request):
#     form = BookingForm()
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             book = form.save(commit=False)
#             book.user = request.user
#             book.save()
#             messages.success(request, 'Book saved successfully')
#             return request('book:home')
#         else:
#             messages.error(request, 'something went wrong')
#     else:
#         form = BookingForm()

#     context = {
#         '
#     }
#     return render(request, 'book/service_detail.html', context)
