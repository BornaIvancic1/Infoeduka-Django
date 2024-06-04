from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Kolegij, Profesor, Korisnik
from .models import Obavijest
from django.views.decorators.cache import never_cache
from datetime import date, timedelta


@never_cache
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('pocetna')
        else:
            messages.error(request, 'Invalid email or password.')
    
    return render(request, 'login.html')

@login_required
def ja_view(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'ja.html', context)

@login_required
def kolegij_view(request):
    profesori=Profesor.objects.all()
    kolegiji = Kolegij.objects.all()
    
    return render(request, 'kolegij.html', {'profesori': profesori, 'kolegiji': kolegiji})

from django.shortcuts import render, redirect
from django.utils.timezone import now

@login_required
def pocetna_view(request):
    # Retrieve latest obavijesti first
    obavijesti = Obavijest.objects.all().order_by('-publication_date')

    #kreiranje obavijest
    kolegiji = Kolegij.objects.all()
    

    return render(request, 'pocetna.html', {'obavijesti': obavijesti, 'kolegiji': kolegiji})

@login_required
def kolegij_list(request):
    kolegiji = Kolegij.objects.all()
    return render(request, 'kolegij.html', {'kolegiji': kolegiji})

@login_required
def create_obavijest(request):
    if request.method == 'POST':
        title = request.POST.get('inputNaslov')
        content = request.POST.get('inputObavijest')
        publication_date = date.today()
        expiration_date = date.today()+ timedelta(days=30)
        kolegij = request.POST.get('inputPredmet')
        obavijest = Obavijest.objects.create(title=title,
                                              content=content,
                                              publication_date=publication_date,
                                              expiration_date=expiration_date,
                                              kolegij=kolegij)
        obavijest.save()
        return redirect('http://127.0.0.1:8000/pocetna/')  # Redirect to a success page or any other desired page after saving data
    return render(request, 'pocetna.html')


@login_required
def create_profesor(request):
    if request.method == 'POST':
        first_name = request.POST.get('inputFirstName')
        last_name = request.POST.get('inputLastName')
        email = request.POST.get('inputEmail')
        password = request.POST.get('inputPassword')
        profesor_user = Korisnik.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name)
        profesor = Profesor.objects.create(profesor_user)
        profesor.save()
        
        return redirect('http://127.0.0.1:8000/kolegij/')  # Redirect to a success page or any other desired page after saving data
    return render(request, 'kolegij.html')


def create_kolegij(request):
    if request.method == 'POST':
        kolegij_naziv = request.POST.get('inputNaslov')
        profesor = request.POST.get('inputProfesor')  # Assuming this is the name of the professor

        

        if profesor:
            kolegij = Kolegij.objects.create(kolegij_naziv=kolegij_naziv, profesor=profesor)
            kolegij.save()
            return redirect('http://127.0.0.1:8000/kolegij/')  # Redirect to a success page or any other desired page after saving data
        else:
            # Handle the case where the professor was not found
            return redirect('http://127.0.0.1:8000/kolegij/')

    return render(request, 'kolegij.html')



