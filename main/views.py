import os

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Main, TODO
from .forms import AddPeopleForm, AddTODOForm, Updata

from .updatefile import update


def home(request):
    main_objects = Main.objects.all()
    if request.method == "POST":
        if request.POST.get("todo", None):
            pk_todo = request.POST.get("todo", '')
            TODO.objects.filter(pk=pk_todo).update(done=True)
        if request.POST.get("delete", None):
           pk_delete = request.POST.get("delete", None)
           TODO.objects.get(pk=pk_delete).delete()

    todo_objects = TODO.objects.filter(done=False).order_by('status')
    job_dones = TODO.objects.filter(done=True).order_by('status')
    context = {
        'main_objects': main_objects,
        'todo_objects': todo_objects,
        'job_dones': job_dones,
    }
            
    return render(request, 'home.html', context=context)

def detail(request, pk):
    if request.method == "POST":
        form = Updata(request.POST, request.FILES)
        if form.is_valid():
            if len(request.POST) == 3:
                if request.POST.get("field", None):
                    field = request.POST.get("field", None)
                    Main.objects.filter(pk=pk).update(field=field)
                elif request.POST.get("university", None):
                    university = request.POST.get("university", None)
                    Main.objects.filter(pk=pk).update(university=university)
                elif request.POST.get("doctor_adviser", None):
                    doctor_adviser = request.POST.get("doctor_adviser", None)
                    Main.objects.filter(pk=pk).update(doctor_adviser=doctor_adviser)
                elif request.POST.get("title", None):
                    title = request.POST.get("title", None)
                    Main.objects.filter(pk=pk).update(title=title)
                elif request.POST.get("rac", None):
                    rac = request.POST.get("rac", None)
                    Main.objects.filter(pk=pk).update(RAC=rac)
                elif request.POST.get("representative", None):
                    representative = request.POST.get("representative", None)
                    Main.objects.filter(pk=pk).update(representative=representative)
            if len(request.FILES) == 1:
                query = Main.objects.get(pk=pk)
                if request.FILES.get("debt_payment1", None):
                    # update(request.FILES.get("debt_payment1", None), name, family)
                    query.debt_payment1 = request.FILES['debt_payment1']
                    query.save()
                elif request.FILES.get("debt_payment2", None):
                    query.debt_payment1 = request.FILES['debt_payment2']
                    query.save()
                elif request.FILES.get("debt_payment3", None):
                    query.debt_payment1 = request.FILES['debt_payment3']
                    query.save()
                elif request.FILES.get("proposal", None):
                    query.debt_payment1 = request.FILES['proposal']
                    query.save()
                elif request.FILES.get("ch123", None):
                    query.debt_payment1 = request.FILES['ch123']
                    query.save()
                elif request.FILES.get("ch45", None):
                    query.debt_payment1 = request.FILES['ch45']
                    query.save()



            
    people_detail = get_object_or_404(Main, pk=pk)
    return render(request, 'detail.html', {'people': people_detail})

def add_people(request):
    if request.method == "POST":

        form = AddPeopleForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            family = form.cleaned_data['family']
            field = form.cleaned_data['field']
            university = form.cleaned_data['university']
            title  = form.cleaned_data['title']
            doctor_adviser = form.cleaned_data['doctor_adviser']
            money = form.cleaned_data['money']
            debt_payment1 = request.FILES.get("debt_payment1")
            debt_payment2 = request.FILES.get("debt_payment2")
            debt_payment3 = request.FILES.get("debt_payment3")
            start_date = form.cleaned_data['start_date']
            if not start_date:
                start_date = timezone.now()
            proposal = form.cleaned_data['proposal']
            ch123 = form.cleaned_data['ch123']
            ch45 = form.cleaned_data['ch45']
            translation = request.FILES.get("translation")
            rac = form.cleaned_data['RAC']
            representative = form.cleaned_data['representative']
            description = form.cleaned_data['description']
            main_object = Main.objects.create(
                                name=name,
                                family=family,
                                field=field,
                                university=university,
                                title=title,
                                doctor_adviser=doctor_adviser,
                                money=money,
                                debt_payment1=debt_payment1,
                                debt_payment2=debt_payment2,
                                debt_payment3=debt_payment3,
                                start_date=start_date,
                                proposal=proposal,
                                ch123=ch123,
                                ch45=ch45,
                                translation=translation,
                                RAC=rac,
                                representative=representative,
                                description=description,
                            )
            main_object.save()
            return redirect('/')
    else:
        form = AddPeopleForm()
    return render(request, 'add_people.html', {'form': form})

def add_todo(request):
    if request.method == 'POST':
        form = AddTODOForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            status = form.cleaned_data['status']
            if status == 'zremind':
                remind_datetime = form.cleaned_data['remind_datetime']
            else:
                remind_datetime = timezone.now()
            description = form.cleaned_data['description']
            todo = TODO.objects.create(title=title, 
                                       status=status, 
                                       description=description, 
                                       remind_datetime=remind_datetime
                                       )
            todo.save()
            return redirect('/')
    else:
        form = AddTODOForm()
    return render(request, 'add_todo.html', {'form': form})

def todos_page(request):
    if request.method == "POST":
        if request.POST.get("todo", None):
            pk_todo = request.POST.get("todo", '')
            TODO.objects.filter(pk=pk_todo).update(done=True)
        if request.POST.get("delete", None):
           pk_delete = request.POST.get("delete", None)
           TODO.objects.get(pk=pk_delete).delete()
           
    todaies = TODO.objects.filter(status='today', done=False)
    necessaries = TODO.objects.filter(status='necessary', done=False)
    reminds = TODO.objects.filter(status='zremind', done=False).order_by('remind_datetime')
    return render(request, 'todos_page.html', {'todaies': todaies, 'necessaries': necessaries, 'reminds': reminds})