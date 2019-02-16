from django.http import HttpResponse
from django.shortcuts import render
from .models import Person
from .models import Document
from django.core.paginator import Paginator
import main.generation as gen

def main(request):
    person = Person.objects.all()
    
    if request.method == 'POST':
        if 'but' in request.POST:
            if not request.POST['Name'] == '':
                person = person.filter(name=request.POST['Name'])
            
            if not request.POST['Birthday_from'] == '':
                person = person.filter(birthday__gte=request.POST['Birthday_from'])
            
            if not request.POST['Birthday_to'] == '':
                person = person.filter(birthday__lte=request.POST['Birthday_to'])
            
            if not request.POST['Gender'] == 'Male or Female':
                person = person.filter(gender=request.POST['Gender'])
            
            if not request.POST['Phone'] == '':
                person = person.filter(phone='+'+request.POST['Phone'])
            
            if not request.POST['Study_start_from'] == '':
                person = person.filter(startday__gte=request.POST['Study_start_from'])
            
            if not request.POST['Study_start_to'] == '':
                person = person.filter(startday__lte=request.POST['Study_start_to'])
            
            if not request.POST['Study_end_from'] == '':
                person = person.filter(startday__gte=request.POST['Study_end_from'])
            
            if not request.POST['Study_end_to'] == '':
                person = person.filter(startday__lte=request.POST['Study_end_to'])
            
            if not request.POST['Group'] == '':
                person = person.filter(group=request.POST['Group'])
            
            if not request.POST['University'] == '':
                person = person.filter(university=request.POST['University'])
            
            doc_list = []
            for item in person:
                try:
                    temp = Document.objects.get(person_id=item, type="P")
                    doc_list.append(temp)
                except:
                    pass
    else:
        doc_list = Document.objects.filter(type="P")
    
    data = []
    for item in person:
        flag = False
        for obj in doc_list:
            if item.id == obj.person_id.id:
                flag = True
                data.append([item, obj.number])
                break
        if not flag:
            data.append([item, 'no available'])
    
    paginator = Paginator(data, 15)
    page = request.GET.get('page')
    list = paginator.get_page(page)
    
    context = {'list': list}
    
    return render(request, 'main/main.html', context)

def search(request):
    
    return render(request, 'main/search.html')

def ajax_handler(request):
    """
    Generate 10 persons into data base.
    """
    if request.method == 'POST':
        try:
            code = request.POST['code']
        except:
            code = 0
        
        if code == '1':
            list = gen.generate(10)
            
            for item in list:
                person = Person(
                    name=item[0][0], 
                    birthday=item[0][1],
                    gender=item[0][2],
                    phone=item[0][3],
                    startday=item[0][4],
                    endday=item[0][5],
                    group=item[0][6],
                    university=item[0][7]
                )
                person.save()
            
                for i in range(1, len(item)):
                    print(i)
                    print(item)
                    document = Document(
                        number=item[i][0],
                        person_id=person,
                        issue_date=item[i][1],
                        type=item[i][2],
                        scan=item[i][3]
                    )
                    document.save()
            
            message = "Done"
        else:
            message = "Error1"
    else:
        message = "Error2"
    
    return HttpResponse(message)