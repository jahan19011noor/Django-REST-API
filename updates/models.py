import json
from django.conf import settings
from django.core.serializers import serialize
from django.db import models

def upload_update_image(instance, filename):
    return "updates/{user}/{filename}".format(user=instance.user, filename=filename)

class UpdateQuerySet(models.QuerySet):
    # def serialize(self):
    #     qs = self
    #     return serialize('json', qs, fields=('user', 'content', 'image'))

    def serialize(self):
        qs = self
        # obj_list = serialize('json', qs, fields=('user', 'content', 'image'))
        final_array = []

        # json loads -> returns an object from a string representing a json object.
        # json dumps -> returns an string representing a json object from an object.
        # load and dump -> read/write from/to file instead of string

        for obj in qs:
            # obj is not a string but an object of type <class 'updates.models.Update'>
            print type(obj)
            print "obj.serialize(): "   # serialize() converts obj to string
            print obj.serialize()
            print type(obj.serialize())

            # obj.serialize() is a string and so is passed to json.loads()
            struct = json.loads(obj.serialize())
            print "struct: "
            print struct
            print type(struct)
            final_array.append(struct)

        return json.dumps(final_array)


class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model, using=self._db)

class Update(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL)
    content     = models.TextField(blank=True, null=True)
    image       = models.ImageField(upload_to=upload_update_image, blank=True, null=True)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = UpdateManager()

    def __str__(self):
        return self.content or ""

    def serialize(self):
        # json loads -> returns an object from a string representing a json object.
        # json dumps -> returns an string representing a json object from an object.
        # load and dump -> read/write from/to file instead of string

        json_data = serialize("json", [self,], fields=('user', 'content', 'image'))
        print "json_data: "
        print json_data
        print type(json_data)

        # json_data is already string so can be passed to json.loads()
        struct = json.loads(json_data)  #[{}]
        print struct
        # [{u'pk': 1, u'model': u'updates.update',
        #   u'fields': {u'content': u'This is the test content for update 1', u'image': u'updates/jahan/images.png',
        #               u'user': 1}}]

        data = json.dumps(struct[0]['fields'])
        return data