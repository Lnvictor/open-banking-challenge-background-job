from mongoengine import Document, StringField


class Participant(Document):
    organization_id = StringField()
    organization_name = StringField()
    discovery_url = StringField()
