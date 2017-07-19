def_auth_data = {
    'auth_api_key': '10ff349e1cbd8de126924b6eecfc61bd',
    'auth_email': 'vlad.korpusov@mail.ru',
    'auth_domain': 'new596d0be6580de.amocrm.ru',
}

amo_auth_url = 'https://developers.amocrm.ru/rest_api/#auth'
amo_leads_url = 'https://developers.amocrm.ru/rest_api/leads_list.php'
amo_notes_url = 'https://developers.amocrm.ru/rest_api/notes_list.php'

date_from = {'IF-MODIFIED-SINCE': 'Mon, 01 May 2017 00:00:00'}

limit_rows = 500

# 'status': '142', #'Успешно реализовано', 'sort': 10000
# 'status': '15636931', #  'name': 'Согласование договора', 'sort': 60,
# 'status': 15636928  # , 'name': 'Принимают решение', 'pipeline_id': 688405, 'sort': 50,
statuses = {142, 15636931, 15636928}

db_local = {'db_name': 'amocrmtest',
      'host': '192.168.1.1',
      'user': 'amocrmtest',
      'passwd': 'pWPwz4PuXsV7mF89'}

db_remote = {'db_name': 'amocrmtest',
            'host': '192.158.28.170',
            'user': 'amocrmtest',
            'passwd': 'pWPwz4PuXsV7mF89'}

db = db_local
# db = db_remote

R = {'response': {'server_time': 1500405472, 'pipelines': {'688405': {'id': 688405, 'value': 688405, 'statuses': {
    '15636931': {'id': 15636931, 'name': 'Согласование договора', 'pipeline_id': 688405, 'sort': 60, 'color': '#ffcccc',
                 'editable': 'Y'},
    '15636967': {'id': 15636967, 'name': 'Открыто КП', 'pipeline_id': 688405, 'sort': 40, 'color': '#fffeb2',
                 'editable': 'Y'},
    '15636928': {'id': 15636928, 'name': 'Принимают решение', 'pipeline_id': 688405, 'sort': 50, 'color': '#ffcc66',
                 'editable': 'Y'},
    '142': {'id': 142, 'name': 'Успешно реализовано', 'pipeline_id': 688405, 'editable': 'N', 'color': '#CCFF66',
            'sort': 10000},
    '143': {'id': 143, 'name': 'Закрыто и не реализовано', 'pipeline_id': 688405, 'editable': 'N', 'color': '#D5D8DB',
            'sort': 11000},
    '15636925': {'id': 15636925, 'name': 'Переговоры', 'pipeline_id': 688405, 'sort': 20, 'color': '#ffff99',
                 'editable': 'Y'},
    '15636964': {'id': 15636964, 'name': 'Отправлено КП', 'pipeline_id': 688405, 'sort': 30, 'color': '#fffeb2',
                 'editable': 'Y'},
    '15636922': {'id': 15636922, 'name': 'Первичный контакт', 'pipeline_id': 688405, 'sort': 10, 'color': '#99ccff',
                 'editable': 'Y'}}, 'sort': 1, 'label': 'Воронка', 'name': 'Воронка', 'leads': 497, 'is_main': True}},
                  'colors': ['#fffeb2', '#fffd7f', '#fff000', '#ffeab2', '#ffdc7f', '#ffce5a', '#ffdbdb', '#ffc8c8',
                             '#ff8f92', '#d6eaff', '#c1e0ff', '#98cbff', '#ebffb1', '#deff81', '#87f2c0', '#f9deff',
                             '#f3beff', '#ccc8f9', '#eb93ff', '#f2f3f4', '#e6e8ea']}}

l = {'response': {'leads': [
    {'closest_task': 0, 'deleted': 0, 'main_contact_id': 8682431, 'status_id': '142', 'date_create': 1500304565,
     'created_user_id': '1609816', 'linked_company_id': '',
     'tags': [{'name': 'импорт_17072017_2214', 'id': 69505, 'element_type': 2}], 'name': 'Заявка с сайта',
     'custom_fields': [], 'group_id': 0, 'price': '50000', 'id': '2115887', 'pipeline_id': 688405,
     'account_id': '15636916', 'date_close': 1500318965, 'last_modified': 1500318965, 'responsible_user_id': '1609816'},
    {'closest_task': 0, 'deleted': 0, 'main_contact_id': 8682391, 'status_id': '142', 'date_create': 1500316211,
     'created_user_id': '1609816', 'linked_company_id': '',
     'tags': [{'name': 'импорт_17072017_2214', 'id': 69505, 'element_type': 2}], 'name': 'Заявка с сайта mat.capital',
     'custom_fields': [], 'group_id': 0, 'price': '', 'id': '2115843', 'pipeline_id': 688405, 'account_id': '15636916',
     'date_close': 1500318980, 'last_modified': 1500318980, 'responsible_user_id': '1609816'}],
                  'server_time': 1500405745}}
