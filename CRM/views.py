from django.http import HttpResponse, request, JsonResponse
from django.views import View
import json
from .models import User, Gender, Position, Tool, Project, QType, Question, Wizard_step, UserGroup

def index(request):
    return HttpResponse("CRM система Добромебель")

def add_proj(request):
    return HttpResponse("Добавление нового проекта")

class main_data(View):
    def get(self, request):
        data = {}
        counter = 0
        for pos in Position.objects.all():
            counter += 1
            data.update({counter:pos.caption})
        data.update({'pos_counter':counter})
        return JsonResponse(data)

class web_hook(View):
    def post(self, request):
        json_body = json.loads(request.body)
        head = json_body.get('head')
        if head == 'user_ident':
            data = {
                'msg':'Вы ещё не зарегистрированны в системе. ',
                'stat':0,
            }
            usr_id = json_body.get('ID')
            try:
                for usr in User.objects.all():
                    if str(usr_id) == str(usr.ID):
                        data = {
                            'msg':'Вы не являетесь администратором. ',
                            'stat':1,
                        }
                        try: 
                            sudo_group = UserGroup.objects.get(code = 'sudo')
                            if sudo_group in UserGroup.objects.filter(users = usr):
                                data = {
                                    'msg':'OK',
                                    'stat':100,
                                }
                        except: data = {'msg':'Не удалось определить группу администраторов', 'stat':1}
            except: 
                data = {
                    'msg':'Error! ',
                    'stat':0,
                }
        if head == 'new_user':
            usr_name = json_body.get('name')
            usr_id = json_body.get('ID')
            usr_birthdate = json_body.get('birthdate')
            usr_teleg = '@' + json_body.get('teleg')
            usr_gender = Gender.objects.get(name = 'Мужской')
            if json_body.get('gender') == 'жен':
                usr_gender = Gender.objects.get(name = 'Женский')
            counter = 0
            for pos in Position.objects.all(): 
                if counter == int(json_body.get('position')) + 1:
                    usr_position = pos
                counter += 1
            usr_caption = usr_name + ' (' + usr_teleg + ')'
            add_usr = User(
                ID = usr_id,
                caption = usr_caption,
                name = usr_name,
                birthdate = usr_birthdate,
                teleg = usr_teleg,
                gender = usr_gender,
                position = usr_position
            )
            add_usr.save()

            data = {
                'msg':'Пользователь зарегистрирован. '
            }
        return JsonResponse(data)