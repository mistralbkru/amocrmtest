import peewee
# import datetime
from peewee import *

from conf import db

dbp = peewee.MySQLDatabase(db['db_name'], host=db['host'], user=db['user'], passwd=db['passwd'])


class MySQLModel(peewee.Model):
    class Meta:
        database = dbp


class leads(MySQLModel):
    id = IntegerField(index=True, unique=True)
    name = CharField(max_length=255, null=True)
    date_create = DateTimeField(index=True, null=True)
    date_close = DateTimeField(null=True)
    last_modified = DateTimeField(index=True, null=True)
    status_id = IntegerField(index=True, null=True)
    price = FloatField(null=True)
    responsible_user_id = IntegerField(index=True, null=True)
    account_id = IntegerField(index=True, null=True)
    tags = TextField(null=True)
    custom_fields = TextField(null=True)
    upload_time = DateTimeField(index=True, null=True)

    class Meta:
        database = dbp
        db_table = 'leads'


class notes(MySQLModel):
    id = IntegerField(index=True, unique=True)
    type = CharField(index=True, max_length=25, null=True)  # contact/lead/company/task
    element_id = IntegerField(index=True, null=True)
    element_type = IntegerField(index=True, null=True)
    note_type = IntegerField(index=True, null=True)
    created_user_id = IntegerField(index=True, null=True)
    date_create = DateTimeField(index=True, null=True)
    last_modified = DateTimeField(index=True, null=True)
    text = TextField(null=True)
    responsible_user_id = IntegerField(index=True, null=True)
    account_id = IntegerField(index=True, null=True)
    editable = BooleanField(default=True)

    class Meta:
        database = dbp
        db_table = 'notes'

if __name__ == "__main__":
    leads.create_table(fail_silently=True)
    notes.create_table(fail_silently=True)
