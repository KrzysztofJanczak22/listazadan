import os
import datetime
clear = lambda: os.system('cls')
file = open("tasks.txt")
f = file.read()
f = f.split('\n')
f = [l.split(',') for l in f]
tab_task = []
file.close()
file_name = 'tasks.txt'

class Task:
    def __init__(self, id, title, date, finish, deleted):
        self.id = id
        self.title = title
        self.date = date
        self.finish = finish
        self.deleted = deleted

    def printingtask(self):
        print("ID:",self.id," tytul:",self.title," data:",self.date)


    def edittask(self):
        print("1-tytul")
        print("2-data")
        print("3-skonczone")
        choose = input("Co chcesz zmienic? ")
        if(choose=='1'):
            self.title = input("Podaj nowy tytul:")
        elif(choose=='2'):
            self.date = input("Podaj nowa date:")
            self.date = self.date.split(".")
            self.date = datetime.date(int(self.date[2]),int(self.date[1]),int(self.date[0]))
        elif (choose == '3'):
            self.finish = input("Skonczone:")


for i in range(1,len(f),1):
    string = f[i][2].split(".")
    date = datetime.date(int(string[2]),int(string[1]),int(string[0]))
    ta = Task(f[i][0], f[i][1], date, f[i][3], int(f[i][4]))
    tab_task.append(ta)


def sorttask(tab):
    print("1-Od najblizszych")
    print("2-Od najdalszych")
    choose = input("Jak sortowac:")
    i=0
    while i < len(tab)-1:
        task_1 = tab[i].date
        task_2 = tab[i+1].date
        if (choose == '1'):
            if (task_2<task_1):
                pom = tab[i]
                tab[i] = tab[i+1]
                tab[i+1] = pom
                i=0
            else: i+=1
        elif (choose == '2'):
            if (task_2>task_1):
                pom = tab[i]
                tab[i] = tab[i + 1]
                tab[i + 1] = pom
                i=0
            else: i+=1
    return tab

def printtask(tab,choose):
    clear()
    for i in range(len(tab)):
        task = tab[i]
        if (task.finish == '0' and choose == '1' and task.deleted == 0):
            task.printingtask()
        elif (task.finish == '1' and choose == '2' and task.deleted == 0):
            task.printingtask()
        elif (task.deleted == 1 and choose == '3'):
            task.printingtask()
        elif (type == '4'):
            task.printingtask()
            

def datetostring(date):
    string = str(date.day)+"."+str(date.month)+"."+str(date.year)
    return string

def savefile(file_name,tab_task):
    file = open(file_name, "w")
    file.write("0,don't delete,0,0,0\n")
    print(tab_task)
    for task in tab_task:
        if int(task.id) == len(tab_task):
            line = str(task.id) + "," + task.title + "," + datetostring(task.date) + "," + task.finish + "," + str(
                task.deleted)
        else:
            line = str(task.id) + "," + task.title + "," + datetostring(task.date) + "," + task.finish + "," + str(
                task.deleted) + "\n"
        file.write(line)
    file.close()


work = 1

while(work==1):
    print("1-Wyswietl zadania")
    print("2-Dodac zadanie")
    print("3-Usunac zadanie")
    print("4-Edytowac zadanie")
    print("5-Oznaczyc jako zakonczone")
    print("6-Zakoncz")
    choose = input("Co chcesz zrobic?")
    if(choose=='1'):
        clear()
        print("1-Nieskonczone")
        print("2-Skonczone")
        print("3-Usuniete")
        print("4-Wszystkie")
        print("5-Posortowane")
        choose_print = input("Jakie zadania chcesz wyswietlic:")
        if (choose_print == '5'):
            clear()
            tab_sort = []
            for i in range(len(tab_task)):
                tab_sort.append(tab_task[i])
            sorttask(tab_sort)
            print("1-Nieskonczone")
            print("2-Skonczone")
            print("3-Usuniete")
            print("4-Wszystkie")
            choose_as = input("Jakie zadanie wyswietlic:")
            printtask(tab_sort,choose_as)
        else: printtask(tab_task,choose_print)
    elif(choose=='2'):
        task_title = input("Podaj tytul:")
        task_date = input("Podaj date:")
        task_date = task_date.split(".")
        id = len(tab_task) + 1
        task = Task(id,task_title,datetime.date(int(task_date[2]),int(task_date[1]),int(task_date[0])),  '0',0)
        tab_task.append(task)
        savefile(file_name, tab_task)
        clear()

    elif(choose=='3'):
        id = int(input("Kto numer usunac:"))
        task = tab_task[id - 1]
        task.deleted = 1
        savefile(file_name, tab_task)
        clear()


    elif(choose=='4'):
        id = int(input("Podaj id zadania:"))
        task = tab_task[id -1]
        task.edittask()
        savefile(file_name, tab_task)
        clear()
    elif(choose=='5'):
        id = int(input("Podaj id:"))
        task = tab_task[id - 1]
        task.finish = '1'
        savefile(file_name, tab_task)
        clear()
    elif(choose=='6'):
        if not tab_task: work = 0
        else:
            savefile(file_name,tab_task)
            work = 0

