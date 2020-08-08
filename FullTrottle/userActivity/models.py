from mongoengine import Document, fields

class User(Document):
    user_id = fields.StringField(required=True)
    real_name = fields.StringField(required=True)
    tz = fields.StringField(required=True)

class ActivityPeriod(Document):
    user_id = fields.StringField(required=True)
    start_time = fields.StringField(required=True)
    end_time = fields.StringField(required=True)

