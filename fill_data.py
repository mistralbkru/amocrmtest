from requests import Session
from _datetime import datetime
from conf import def_auth_data, date_from, limit_rows, statuses, amo_auth_url, amo_leads_url, amo_notes_url
from models import leads, notes


def auth(auth_api_key, auth_email, auth_domain):
    payload = {
        'USER_LOGIN': auth_email,
        'USER_HASH': auth_api_key,
        'type': 'json',
    }
    s = Session()
    s.headers.update(date_from)
    r = s.post('https://{}/private/api/auth.php'.format(auth_domain), data=payload)
    # print(r.status_code)
    # print(r.headers)
    # print(r.text)
    if '<auth>true</auth>' in r.text:
        return s


def get_leads(s, offset, status, auth_domain):
    payload = {
        'limit_rows': limit_rows,
        'limit_offset': offset,
        'status': status,
    }
    r = s.get('https://{}/private/api/v2/json/leads/list'.format(auth_domain), params=payload)
    return r


def fill_leads(s, upload_time, auth_domain):
    # clear table
    q = leads.delete()
    q.execute()
    for status in statuses:
        offset = 0
        while offset >= 0:
            r = get_leads(s, offset, status, auth_domain)
            print('{} - {}'.format(r.url, r.status_code))
            # print(r.status_code)
            # print(r.headers)
            # print(r.text)
            if not len(r.text):
                break
            offset += limit_rows
            leads_result = r.json()['response'].get('leads')
            for lead in leads_result:
                leads.create(
                    id=lead['id'],
                    name=lead['name'],
                    date_create=datetime.fromtimestamp(lead['date_create']),
                    date_close=datetime.fromtimestamp(lead['date_close']),
                    last_modified=datetime.fromtimestamp(lead['last_modified']),
                    status_id=lead['status_id'],
                    price=lead['price'] if lead['price'] else 0,
                    responsible_user_id=lead['responsible_user_id'],
                    account_id=lead['account_id'],
                    tags=lead['tags'],
                    custom_fields=lead['custom_fields'],
                    upload_time=upload_time,
                )


def get_notes(s, offset, status, notes_type, auth_domain):
    payload = {
        'type': notes_type,
        'limit_rows': limit_rows,
        'limit_offset': offset,
        'status': status,
    }
    r = s.get('https://{}/private/api/v2/json/notes/list'.format(auth_domain), params=payload)
    return r


def fill_notes(s, upload_time, auth_domain):
    notes_type = 'lead'
    # clear table
    q = notes.delete()
    q.execute()
    for status in statuses:
        offset = 0
        while offset >= 0:
            r = get_notes(s, offset, status, notes_type, auth_domain)
            print('{} - {}'.format(r.url, r.status_code))
            # print(r.url)
            # print(r.status_code)
            # print(r.headers)
            # print(r.text)
            if not len(r.text):
                break
            offset += limit_rows
            notes_result = r.json()['response'].get('notes')
            for note in notes_result:
                try:
                    notes.create(
                        id=note['id'],
                        type=notes_type,
                        element_id=note['element_id'],
                        element_type=note['element_type'],
                        note_type=note['note_type'],
                        created_user_id=note['created_user_id'],
                        date_create=datetime.fromtimestamp(note['date_create']),
                        last_modified=datetime.fromtimestamp(note['last_modified']),
                        text=note['text'],
                        responsible_user_id=note['responsible_user_id'],
                        account_id=note['account_id'],
                        editable=note['editable'],
                        upload_time=upload_time,
                    )
                except Exception as e:
                    print('Exception: ' + str(e))


def get_pipelines(s, auth_domain):
    r = s.get('https://{}/private/api/v2/json/pipelines/list'.format(auth_domain))
    print(r.url)
    print(r.status_code)
    print(r.headers)
    print(r.json())


def get_data(auth_api_key=def_auth_data['auth_api_key'], auth_email=def_auth_data['auth_email']):
    upload_time = datetime.now()
    auth_domain = def_auth_data['auth_domain']
    s = auth(auth_api_key, auth_email, auth_domain)
    # get_pipelines(s, auth_domain)
    fill_leads(s, upload_time, auth_domain)
    # fill_notes(s, upload_time, auth_domain)


if __name__ == "__main__":
    get_data()
