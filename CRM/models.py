import code
from logging import PercentStyle
from unicodedata import name
from django.db import models
from datetime import datetime

class Bot_config(models.Model):
    bot_name = models.CharField(verbose_name = 'Наименование бота', max_length=50)
    tgbot_token = models.CharField(verbose_name = 'Telegram API токен', max_length=50)
    start_message = models.TextField(verbose_name = 'Текст приветственного сообщения на команду "/start"')
    def __str__(self):
        return self.bot_name

class Client_contact(models.Model):
    KITCHEN_TYPES = [
        ('U', 'Не определился'),
        ('C', 'Угловая'),
        ('P', 'П образная'),
        ('L', 'Прямая'),
        ('I', 'Островная'),
    ]
    caption = models.CharField(verbose_name = 'Текст записи', max_length = 150)
    name = models.CharField(verbose_name = 'Имя клиента', max_length = 50, default = 'Потенциальный клиент')
    phone = models.CharField(verbose_name = 'Номер телефона', max_length = 50)
    kitchen_type = models.CharField(verbose_name = 'Тип кухни', max_length = 2, choices = KITCHEN_TYPES, default = 'U')
    material = models.CharField(verbose_name = 'Материал фасада', max_length=50, default = 'Помогите выбрать')
    due_done = models.CharField(verbose_name = 'Когда планирует заказывать', max_length=50, default = 'Просто интересуюсь')
    pay_type = models.CharField(verbose_name = 'Оплата', max_length=50, default = 'Картой')
    present = models.CharField(verbose_name = 'Выбранный подарок', max_length=50)
    def __str__(self):
        return self.caption

class Gender(models.Model):
    name = models.CharField(max_length = 10)
    code = models.CharField(max_length = 10)
    def __str__(self):
        return self.name

class Inflow_base(models.Model):
    name = models.CharField(max_length = 50)
    code = models.CharField(max_length = 10)
    def __str__(self):
        return self.name

class Fund(models.Model):
    name = models.CharField(max_length = 50)
    code = models.CharField(max_length = 10)
    percent = models.FloatField(default = 0, verbose_name = 'Процент')
    base = models.ForeignKey(Inflow_base, verbose_name = 'Основа начисления', on_delete = models.CASCADE, blank = True, default = None)
    def __str__(self):
        return self.name

class Function(models.Model):
    name = models.CharField(max_length = 50)
    code = models.CharField(max_length = 10)
    fund = models.ForeignKey(Fund, verbose_name = "Из фонда", on_delete = models.CASCADE, blank = True, default = None)
    inflow = models.ForeignKey(Inflow_base, verbose_name = "или на основе", on_delete = models.CASCADE, blank = True, default = None)
    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length = 50)
    code = models.CharField(max_length = 10)
    caption = models.CharField(max_length = 200, verbose_name = "Наименование")
    description = models.CharField(max_length = 500, verbose_name = "Описание")
    functions = models.ManyToManyField(Function, verbose_name = "Функции", default = None, blank = True)
    def __str__(self):
        return self.name

class User(models.Model):
    ID = models.CharField(max_length=150, default = '')
    caption = models.CharField(max_length = 200, editable = False)
    name = models.CharField(max_length = 200, verbose_name = "Имя Фамилия")
    birthdate = models.CharField(max_length = 20, verbose_name = "Дата рождения")
    teleg = models.CharField(max_length = 200, verbose_name = "Телеграм")
    gender = models.ForeignKey(Gender, verbose_name = "Пол", on_delete = models.CASCADE, default = 0)
    position = models.ForeignKey(Position, verbose_name = "Должность", on_delete = models.CASCADE, default = 0)
    def __str__(self):
        return self.caption

class UserGroup(models.Model):
    name = models.CharField(max_length = 200, verbose_name = "Название группы")
    code = models.CharField(max_length = 10)
    description = models.CharField(max_length = 500, verbose_name = "Описание")
    users = models.ManyToManyField(User, verbose_name = "Пользователи", blank = True)
    def __str__(self):
        return self.name

class Status_type(models.Model):
    name = models.CharField(max_length = 50)
    code = models.CharField(max_length = 10)
    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length = 50)
    code = models.CharField(max_length = 10)
    stat_type = models.ForeignKey(Status_type, verbose_name = "тип статуса", on_delete = models.CASCADE)
    def __str__(self):
        return self.name

class Resources_type(models.Model):
    caption = models.CharField(max_length = 50, verbose_name = "Наименование")
    def __str__(self):
        return self.caption

class Resource(models.Model):
    caption = models.CharField(max_length = 50, verbose_name = "Наименование")
    dimention = models.CharField(max_length = 20, verbose_name = "Единицы измерения")
    r_type = models.ForeignKey(Resources_type, verbose_name = "Тип", on_delete = models.CASCADE)
    price = models.FloatField(default = 0, verbose_name = "Цена за единицу")
    def __str__(self):
        return self.caption

class Tool(models.Model):
    caption = models.CharField(max_length = 200, verbose_name = "Наименование")
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 500, verbose_name = "Описание")
    diler_price = models.FloatField(default = 0, verbose_name = "Закупочная стоимость")
    riental_price = models.FloatField(default = 0, verbose_name = "Итоговая стоимость")
    def __str__(self):
        return self.name

class Project(models.Model):
    caption = models.CharField(max_length = 200, verbose_name = "Наименование проекта")
    description = models.CharField(max_length = 500, default = '', verbose_name = "Описание проекта")
    name = models.CharField(max_length = 200, verbose_name = "Отображаемое имя проекта")
    pub_date = models.DateTimeField(default = datetime.now, verbose_name = "Создан")
    manager = models.ForeignKey(User, verbose_name = "Ответственный", on_delete = models.CASCADE, default = 0)
    designerless = models.BooleanField(default = False, verbose_name = "Промо 10% (не дизайнерский)")
    discount = models.FloatField(default = 0, verbose_name = "Дополнительная скидка, %")
    map_price = models.FloatField(default = 0, verbose_name = "МРЦ")
    construct = models.BooleanField(default = False, verbose_name = "Сборка")
    shipping = models.BooleanField(default = False, verbose_name = "Доставка")
    up_shipping = models.BooleanField(default = False, verbose_name = "Подъем")
    additional_tools = models.ManyToManyField(Tool, verbose_name = "Дополнительная техника")
    total_price = models.FloatField(default = 0, verbose_name = "Итоговая стоимость")
    def __str__(self):
        return self.name

class QType(models.Model):
    name = models.CharField(max_length = 200, verbose_name = "Наименование типа")
    code = models.CharField(max_length = 10, verbose_name = "Код типа")
    def __str__(self):
        return self.name

class Question(models.Model):
    name = models.CharField(max_length = 200, verbose_name = "Наименование вопроса")
    text = models.CharField(max_length = 1000, verbose_name = "Текст вопроса")
    q_type = models.ForeignKey(QType, verbose_name = "Тип вопроса", on_delete = models.CASCADE, default = 0)
    def __str__(self):
        return self.name

class Wizard_step(models.Model):
    name = models.CharField(max_length = 200, verbose_name = "Наименование шага")
    title = models.CharField(max_length = 500, verbose_name = "Заголовок")
    descriptor = models.CharField(max_length = 1000, verbose_name = "Дескриптор")
    order = models.IntegerField(default = 1, verbose_name = "Порядковый номер")
    qustions = models.ManyToManyField(Question, verbose_name = "Вопросы")
    def __str__(self):
        return self.name