import random
from datetime import date

class Person():
    """
    Genarate data in Person table.
    """
    def generate(self, number=1):
        """
        Unite all fields into list.
        """
        list = []
        
        name = self.name(number)
        birthdate = self.birthdate(number)
        phone_number = self.phone_number(number)
        start_end_day = self.start_end_day(birthdate)
        group = self.group(number)
        university = self.university(number)
        
        object = Document()
        document_list = object.generate(number, birthdate)
        
        # index of a document_list
        k = 0
        for i in range(0, number):
            temp = []
            temp.append([
                name[i][0],
                birthdate[i],
                name[i][1],
                phone_number[i],
                start_end_day[i][0],
                start_end_day[i][1],
                group[i],
                university[i]
            ])
            
            while document_list[k][1] == i:
                temp.append([
                    document_list[k][0],
                    document_list[k][2],
                    document_list[k][3],
                    document_list[k][4]
                ])
                k = k + 1
                if k == len(document_list):
                    break
            
            list.append(temp)
                
        return list
        
    def name(self, number):
        """
        Gender, names and surnames generation.
        """
        male_number = random.randint(number*2//5, number*3//5+1)
        result_list = []
            
        with open("student_app/static/surnames.txt", "r") as s_file:
            surnames = s_file.readlines()
                
            with open("student_app/static/male_names.txt") as m_file:
                m_names = m_file.readlines()
                for i in range(0, male_number):
                    rand1 = random.randint(0, 99)
                    rand2 = random.randint(0, 99)
                    result_list.append([m_names[rand1].rstrip()+" "+surnames[rand2].rstrip(), 'M'])
                
            with open("student_app/static/female_names.txt") as f_file:
                f_names = f_file.readlines()
                for i in range(0, number - male_number):
                    rand1 = random.randint(0, 99)
                    rand2 = random.randint(0, 99)
                    result_list.append([f_names[rand1].rstrip()+" "+surnames[rand2].rstrip(), 'F'])
        
        random.shuffle(result_list)
        
        return result_list
    
    def birthdate(self, number):
        """
        Birthdate generation.
        """
        birthdate = []
        for i in range(0, number):
            birthdate.append(
                date(
                    year=random.randint(1960, 2000),
                    month=random.randint(1, 12),
                    day=random.randint(1, 28)
                )
            )
        
        return birthdate
    
    def phone_number(self, number):
        """
        Phone number generation.
        """
        phone_number = []
        for i in range(0, number):
            if random.randint(0, 19) == 0:
                phone_number.append("-")
            else:
                phone_number.append(
                    "+1"
                    +str(random.randint(200, 999))
                    +str(random.randint(200, 999))
                    +str(random.randint(0, 9))
                    +str(random.randint(0, 9))
                    +str(random.randint(0, 9))
                    +str(random.randint(0, 9))
                )
        
        return phone_number
    
    def start_end_day(self, birthdate):
        """
        Start day and end day of education generation.
        """
        start_end_date = []
        for item in birthdate:
            step = 2000 - item.year
            rand1 = date(
                year=random.randint(2018-step, 2018),
                month=9,
                day=1
            )
            rand2 = date(
                year=rand1.year+random.randint(4, 6),
                month=5,
                day=31
            )
            # start_end_date = ([startday, endday], ...)
            start_end_date.append([rand1, rand2])
        
        return start_end_date
    
    def group(self, number):
        """
        Group generation.
        """
        group = []
        for i in range(0, number):
            group_name = ''
            for j in range(0, random.randint(3, 5)):
                # symbol: 0 - number, 1 - lowercase, 2 - uppercase
                symbol = random.randint(0,3)
                # ASCII: 0 - 48, 9 - 57, 'a' - 97, 'z' - 122, 'A' - 65, 'Z' - 90
                if symbol == 0:
                    group_name += chr(random.randint(48, 57))
                elif symbol == 1:
                    group_name += chr(random.randint(97, 122))
                else:
                    group_name += chr(random.randint(65, 90))
            group.append(group_name)
        
        return group
    
    def university(self, number):
        """
        University generation.
        """
        university = []
        with open("student_app/static/universities.txt") as u_file:
            u_names = u_file.readlines()
            for i in range(0, number):
                university.append(u_names[random.randint(0, 99)].rstrip())
        
        return university

class Document():
    """
    Generate data in Document table.
    """
    def generate(self, number, birthdate):
        """
        Unite all fields into list.
        """
        list = self.type(number)
        number_list = self.number(len(list))
        date_list = self.issue_date(list, birthdate)
        scan_list = self.scan(number_list)
        
        for i in range(0, len(list)):
            temp = list.pop(i)
            list.insert(i, [number_list[i], temp[0], date_list[i], temp[1], scan_list[i]])
        
        return list
            
    
    def number(self, number):
        """
        Document number generation.
        The list has unique items, if 0 < number < 10000.
        In practice the number may be a bit larger.
        """
        res_list = []
        k = 10000
        
        for i in range(0, number):
            num = ''
            temp = str(k)
            k = k + random.randint(1, 3)
            num += str(random.randint(0, 9))
            num += temp[0]
            num += str(random.randint(0, 9))
            num += temp[1]
            num += str(random.randint(0, 9))
            num += temp[2]
            num += temp[3]
            num += str(random.randint(0, 9))
            num += temp[4]
            
            res_list.append(num)
        
        random.shuffle(res_list)
        
        return res_list
    
    def issue_date(self, list, birthdate):
        """
        Issue date generation.
        """
        date_list = []
        
        for i in range(0, len(list)):
            step = 2000 - birthdate[list[i][0]].year
            rand = date(
                year=random.randint(2018-step, 2018),
                month=random.randint(1, 12),
                day=random.randint(1, 28)
            )
            date_list.append(rand)
        
        return date_list
    
    def type(self, number):
        """
        Document type generation.
        Also generate number of documents for each person.
        """
        res_list = []
        
        for i in range(0, number):
            # Each person have 1, 2 or 3 documents. Generate number for each person.
            amount = random.randint(1, 3)
            if amount == 1:
                temp = [random.choice(['P', 'S', 'B'])]
            elif amount == 2:
                temp = ['P', 'S', 'B']
                temp.remove(random.choice(['P', 'S', 'B']))
            else:
                temp = ['P', 'S', 'B']
            
            for item in temp:
                res_list.append([i, item])
                
        return res_list
    
    def scan(self, number_list):
        """
        Scan location generation.
        """
        res_list = []
        
        for item in number_list:
            res_list.append('/static/documents/'+item+'.pdf')
        
        return res_list
        
object = Person()
generate = object.generate