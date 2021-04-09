# Вариант 7
# Создать класс Book: id, Название, Автор (ы), Издательство, Год издания,
# Количество страниц, Цена, Тип переплета.
# Функции-члены реализуют запись и считывание полей (проверка корректности).
# Создать список объектов. Вывести:
# a)	список книг заданного автора;
# b)	список книг, выпущенных после заданного года.

class book:

    # конструктор
    def __init__(self, book_id, title, author, publisher, year, pages, price, type):
        self.id = book_id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.pages = pages
        self.price = price
        self.type = type

    def get_book_id(self):
        return self.id

    def set_id(self, book_id):
        self.id = book_id

    def get_title(self):
        return self.title

    def set_name(self, title):
        self.title = title

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_publisher(self):
        return self.publisher

    def set_publisher(self, publisher):
        self.publisher = publisher

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_pages(self):
        return self.pages

    def set_pages(self, pages):
        self.pages = pages

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type


library = [
    book('1', 'Код да Винчи', 'Браун', 'АСТ', '2013', '477', '10', 'Твердый переплет'),
    book('2', 'Тень горы', 'Робертс', 'Азбука', '2017', '576', '25', 'Мягкий переплет'),
    book('3', 'Тараканы', 'Несбё', 'Иностранка', '2020', '432', '12', 'Мягкий переплет'),
    book('4', 'Атлант расправил плечи', 'Рэнд', 'Альпина Паблишер', '2020', '432', '30', 'Твердый переплет'),
    book('5', 'Мечтать не вредно', 'Шер', 'Манн, Иванов и Фербер', '2016', '352', '13',
         'Твердый переплет'),

]


def Print(self):
    return str(self.get_book_id()) + "," + self.get_title() + "," + self.get_author() + \
           "," + self.get_publisher() + "," + str(self.get_year()) + "," + str(self.get_pages()) + \
           "," + str(self.get_price()) + "," + self.get_type()


def getInfo(self):
    print(str(library[i].get_book_id()) + ") Название книги: " + library[i].get_title() + ", Автор: " + library[i].get_author() + \
          ", издательство " + library[i].get_publisher() + ", год издания: " + str(library[i].get_year()) + ", " + str(
        library[i].get_pages()) + \
          " стр., цена: " + str(library[i].get_price()) + ", тип издания: " + library[i].get_type() + ".")


# Вывести:
# a)	список книг заданного автора;
Author = input('Введите, пожалуйста, фамилию автора: \n')
i = 0
for i in range(len(library)):
    if library[i].get_author() == Author:
        print("Книги выбранного автора:")
        getInfo(i)
        i += 1

# b)	список книг, выпущенных после заданного года.
check_year = str(input('\nВведите, пожалуйста, год издания: \n'))
print("Список книг, изданных после " + str(check_year) + " года:")
for i in range(len(library)):
    if library[i].get_year() > check_year:
        getInfo(i)
        i += 1

