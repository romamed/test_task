from django.http import HttpResponse
from django.shortcuts import render
from .models import Person
from .models import Document
from django.core.paginator import Paginator
import main.generation as gen

def main(request):
    
    person = Person.objects.all()
    doc_list = Document.objects.filter(type="P")
    
    #passport = []
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