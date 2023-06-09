from django.shortcuts import render

# Create your views here.
def home(request): 
    
    return render(request,'core/home.html')

def about(request): 
    
    return render(request,'core/about.html')

def poleras(request): 
    
    return render(request,'core/poleras.html')

def pantalones(request): 
    
    return render(request,'core/pantalones.html')

def polerones(request): 
    
    return render(request,'core/polerones.html')

def registro(request): 
    
    return render(request,'core/registro.html')

def formulario_tienda(request): 
    
    return render(request,'core/formulario tienda.html')