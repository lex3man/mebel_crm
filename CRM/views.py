from datetime import datetime
from pickle import NONE
from unicodedata import name
from django.http import HttpResponse, request, JsonResponse
from django.views import View
import json
from .models import User, Gender, Position, UserGroup, Tool, Project, Bot_config

def index(request):
    return HttpResponse("CRM система Добромебель")

def add_proj(request):
    return HttpResponse("Добавление нового проекта")

class main_data(View):
    def get(self, request):
        data = {}

        positions = {}
        counter = 0
        for pos in Position.objects.all():
            counter += 1
            positions.update({counter:pos.caption})
        positions.update({'pos_counter':counter})
        data.update({'positions':positions})

        tools = {}
        counter = 0
        for tool in Tool.objects.all():
            counter += 1
            tools.update({counter:tool.caption})
        tools.update({'tool_counter':counter})
        data.update({'tools':tools})

        projects = {}
        counter = 0
        for project in Project.objects.all():
            counter += 1
            project_details = {}
            attr_count = 0
            for field in Project._meta.get_fields():
                attr_count += 1
                ser_data = json.dumps(field.value_from_object(project), separators=(',', ':'), ensure_ascii = False, default = str)
                project_details.update({field.verbose_name:ser_data})
            projects.update({counter:project_details})
        projects.update({'projects_counter':counter})
        projects.update({'attr_counter':attr_count})
        data.update({'projects':projects})

        return JsonResponse(data)

class web_hook(View):
    def post(self, request):
        json_body = json.loads(request.body)
        head = json_body.get('head')

        if head == 'bot_config':
            get_bot_name = json_body.get('bot_name')
            get_config = Bot_config.objects.get(bot_name = get_bot_name)
            data = {
                'TOKEN':get_config.tgbot_token,
                'Start_message':get_config.start_message
            }
        
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

        if head == 'new_proj':
            try: proj_manager = User.objects.get(ID = json_body.get('manager'))
            except: proj_manager = NONE
            get_tools = str(json_body.get('additional_tools')).replace(' ', '')
            tools = get_tools.split(',')
            add_proj = Project(
                caption = json_body.get('name'),
                description = json_body.get('description'),
                name = json_body.get('caption'),
                manager = proj_manager,
                pub_date = datetime.now(),
                discount = 0,
                map_price = float(json_body.get('total_price')),
                total_price = float(json_body.get('total_price')) * 2.7
            )
            add_proj.save()
            if json_body.get('designerless') == 1:
                add_proj.designerless = True
                add_proj.total_price = (float(json_body.get('total_price')) * 2.7) * 0.9
            if json_body.get('construct') == 1:
                add_proj.construct = True
            if json_body.get('shipping') == 1:
                add_proj.shipping = True
            if json_body.get('up_shipping') == 1:
                add_proj.up_shipping = True
            if get_tools is not 0:
                counter = 1
                for tool in Tool.objects.all():
                    if str(counter) in tools:
                        add_proj.additional_tools.add(tool)
                    counter += 1
            add_proj.save()
            data = {'msg':'Проект успешно добавлен'}

        return JsonResponse(data)