from django.db import models

# Create your models here.
from mongoengine import Document, EmbeddedDocument, fields


class Test(Document):
    tconst = fields.StringField(required=True)
    titleType = fields.StringField(required=True)
    primaryTitle = fields.StringField(required=True)
    originalTitle = fields.StringField(required=True)
    isAdult = fields.IntField(required=True)
    startYear = fields.IntField(required=True)
    endYear = fields.StringField(required=False)
    runtimeMinutes = fields.IntField(required=False)
    genres = fields.StringField(required=True)


class Titles(Document):
    tconst = fields.StringField(required=True)
    titleType = fields.StringField(required=True)
    primaryTitle = fields.StringField(required=True)
    originalTitle = fields.StringField(required=True)
    isAdult = fields.StringField(required=True)
    startYear = fields.StringField(required=True)
    endYear = fields.StringField(required=False)
    runtimeMinutes = fields.StringField(required=False)
    genres = fields.StringField(required=True)
