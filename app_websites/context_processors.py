from .models import *

def header(request):
    context = { 
        'machine_types' : MachineType.objects.all(),
    }
    return ( context )