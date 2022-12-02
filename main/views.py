from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Main, TODO
from .forms import AddPeopleForm, AddTODOForm



def home(request):
    main_objects = Main.objects.all()
    todo_objects = TODO.objects.all().order_by('status')
    return render(request, 'home.html', {'main_objects': main_objects, 'todo_objects': todo_objects})

def detail(request, pk):
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
            debt_payment1 = form.cleaned_data['debt_payment1']
            debt_payment2 = form.cleaned_data['debt_payment2']
            debt_payment3= form.cleaned_data['debt_payment3']
            start_date = form.cleaned_data['start_date']
            if not start_date:
                start_date = timezone.now()
            proposal = form.cleaned_data['proposal']
            ch123 = form.cleaned_data['ch123']
            ch45 = form.cleaned_data['ch45']
            translation = form.cleaned_data['translation']
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
        print('before is valid')

        if form.is_valid():
            title = form.cleaned_data['title']
            status = form.cleaned_data['status']
            print(status)
            print(title)
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
    todaies = TODO.objects.filter(status='today', done=False)
    necessaries = TODO.objects.filter(status='necessary', done=False)
    reminds = TODO.objects.filter(status='zremind', done=False).order_by('remind_datetime')
    return render(request, 'todos_page.html', {'todaies': todaies, 'necessaries': necessaries, 'reminds': reminds})
