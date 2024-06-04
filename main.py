#1
import random
import string

def generate_password(l):

  characters = list(string.ascii_letters + string.digits)
  random.shuffle(characters)
  password = ''.join(random.choices(characters, k=l))
  return password

def main():
  l = int(input("введите длину пароля: "))
  num_passwords = int(input("введите количество паролей: "))

  for i in range(num_passwords):
    password = generate_password(l)
    print(password)

if __name__ == "__main__":
  main()


#2
import random
def generate_schedule(num_exams, subjects):
    days_of_week = ["понедельник", "вторник", "среда", "четверг", "пятница"]
    hours = list(range(9, 15))
    minutes = ["00", 30]
    for i in range(num_exams):
        subject = random.choice(subjects)
        day = random.choice(days_of_week)
        time = f"{random.choice(hours)}:{random.choice(minutes)}"
        ticket = random.randint(1, 20)
        print(f"Экзамен по дисциплине «{subject}» состоится в {day} в {time}. Ваш счастливый билет {ticket}.")
num_exams = int(input("Введите количество экзаменов: "))
subjects = input("Введите наименование дисциплин через запятую и пробел: ").split(", ")
generate_schedule(num_exams, subjects)



#3
import datetime

days_until_exam = int(input("Введите количество дней до экзамена: "))
current_date = datetime.datetime.now()
exam_date = current_date + datetime.timedelta(days=days_until_exam)
month_name = exam_date.strftime("%B")
print(f"Экзамен состоится {exam_date.day} {month_name}.")



#4
from datetime import datetime, timedelta

def is_happy_date(date):

    dt = datetime.strptime(date, '%Y/%m/%d')
    return dt.day % 4 != 0 and dt.weekday() != 0

def find_happy_dates(start_date, n):

    happy_dates = []
    dt = datetime.strptime(start_date, '%Y/%m/%d')
    while len(happy_dates) < 3:
        dt += timedelta(days=n)
        if is_happy_date(dt.strftime('%Y/%m/%d')):
            happy_dates.append(dt.strftime('%d %B, %A'))

    return happy_dates

def main():
    start_date = input("введите исходную дату в формате YYYY/MM/DD: ")
    n = int(input("введите число n: "))

    happy_dates = find_happy_dates(start_date, n)

    print("три подходящие счастливые даты:")
    for date in happy_dates:
        print(date)

if __name__ == "__main__":
    main()


#5
import my_module

print(my_module.my_description())
print(my_module.my_function(1, 2))


#6
import my_module2

list_a = [1, 2, 3, 4, 5]
index = int(input("Введите порядковый номер значения, которое нужно удалить: "))

list_a = my_module2.remove_by_index(list_a, index)

print(list_a)



#7
import my_module3

n = int(input("Введите количество чисел: "))
numbers = []
for i in range(n):
    number = int(input("Введите число: "))
    numbers.append(number)

max_number = my_module3.max_sum_of_digits(numbers)

print("Число с максимальной суммой цифр:", max_number)



