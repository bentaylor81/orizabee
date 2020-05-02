from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from .filters import MachineFilter
from app_users.decorators import unauthenticated_user, allowed_users

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def home(request):
        context = { 
                'brands' : Brand.objects.all(),
                }
        return render(request, 'app_websites/home.html', context )

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def brand_page(request, brand_path):
        context = {
                'models' : Model.objects.filter(series__brand__path=brand_path).order_by('series__sort_order'),
                'brands' : Brand.objects.filter(path=brand_path),
                }
        return render(request, 'app_websites/brand.html', context )

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def series_page(request, brand_path, series_path):
        context = {
                'machines' : Machine.objects.filter(model__series__path=series_path).order_by('model__sort_order'),
                'series' : Series.objects.filter(path=series_path),
                }
        return render(request, 'app_websites/series.html', context )

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def model_page(request, brand_path, series_path, model_path):
        context = {
                'models' : Model.objects.filter(path=model_path),
                'machines' : Machine.objects.filter(model__path=model_path).order_by('year'),
                 }
        return render(request, 'app_websites/model.html', context )

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def machine_page(request, brand_path, series_path, model_path, machine_path):
        context = {
                'machines' : Machine.objects.filter(path=machine_path),
                'parts' : Part.objects.filter(machine__path=machine_path).order_by('ref_no'),
                'part_diagrams' : PartDiagram.objects.all(),
        }
        return render(request, 'app_websites/machine.html', context )

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def partlists_page(request, brand_path):

        machines = Machine.objects.filter(model__series__brand__path=brand_path)
        myFilter = MachineFilter(request.GET, queryset=machines)
        machines = myFilter.qs
        
        context = {
                'brands' : Brand.objects.filter(path=brand_path),
                'brand_path' : brand_path,
                'machines' : machines,
                'myFilter' : MachineFilter()
                }
        return render(request, 'app_websites/partlists.html', context )

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def assets_page(request):
        context = {
                'brands' : Brand.objects.all(),
                'machine_types' : MachineType.objects.all(),         
                }
        return render(request, 'app_websites/assets.html', context )


