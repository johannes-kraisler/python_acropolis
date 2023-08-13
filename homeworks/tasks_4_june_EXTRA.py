"""1. Запросите у пользователя имя и месячную зарплату в долларах и выведите
их годовую зарплату в тысячах долларов.
Например: «Мишель», «12345» → «Годовая зарплата Мишель составляет
148 тыс. долларов».
"""
def salary ():
    name=input("What is your name?")
    salary=input("What is your salary per month?")
    annual_salary=int(salary)*12
    print("The annual salary of {} is {}".format(name,annual_salary))
    
#salary()


"""2. Запросите целое число и выведите «True», если это четное число в
диапазоне от 100 до 999, в противном случае - «False».
 """  

def numbers():
    number=int(input("What is your fav number from 100 to 999?"))
    if number %2==0 and 100<=number<=999:
        print(True)
    else: 
        print(False)
#numbers()        
 


"""3. В качестве входящих данных возьмем целое число; Предположим, что это
число от 101 до 999, а его последняя цифра не равна нулю.
Выведите обратное число.
Например: 256 → 652.  """

def numbers_2():
    number=input("What is your fav number from 101 to 999?")
    if 101<=int(number)<=999 and number[-1]!=0:
        new_number=number[::-1]
        print(new_number)
    else:
        print("Try again")
#numbers_2()
  
    
"""4. Запросите два целых числа и выведите:
a. Их сумму
b. Их разность
c. Произведение
d. Результат деления первого на второе
e. Остаток от деления первого на второе
f. «True», если первое число больше или равно второму, иначе «False»."""

def numbers_3():
    
    number_1=int(input("What is your 1 fav number?"))
    number_2=int(input("What is your 2 fav number?"))

    print (number_1, number_2)

    sum_numbers=number_1+number_2
    print(sum_numbers)

    difference=number_1-number_2
    print(difference)

    multiplication=number_1*number_2
    print(multiplication)

    division=number_1/number_2
    print(division)

    remainder=number_1%number_2
    print(remainder)

    if number_1>=number_2:
        print (True)
    else: 
        print (False)
        
        
#numbers_3()

