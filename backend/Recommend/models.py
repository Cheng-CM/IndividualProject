from mongoengine import Document, EmbeddedDocument, fields

# Create your models here.


class Movies(Document):
    movieId = fields.IntField(required=True)
    title = fields.StringField(required=True)
    genres = fields.StringField(required=True)

class Ratings(Document):
    userId = fields.IntField(required=True)
    movieId = fields.IntField(required=True)
    rating = fields.IntField(required=True)
    timestamp = fields.IntField(required=True)


class custom_ratings(Document):
    userId = fields.IntField(required=True)
    movieId = fields.IntField(required=True)
    rating = fields.IntField(required=True)
    timestamp = fields.IntField(required=True)


class Links(Document):
    movieId = fields.IntField(required=True)
    imdbId = fields.IntField(required=True)
    tmdbId = fields.IntField(required=True)


class Tags(Document):
    userId = fields.IntField(required=True)
    movieId = fields.IntField(required=True)
    tag = fields.StringField(required=True)
    timestamp = fields.IntField(required=True)
