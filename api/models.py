from __future__ import unicode_literals

import random

from django.db import models
from django.db.models import Min
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Epithet(models.Model):
    text = models.CharField(max_length=100)
    uses = models.IntegerField(db_index=True, default=0)

    def size(self):
        return 100  # while you can't add or remove epithets, might not use count() method.

    def __str__(self):
        return self.text


@python_2_unicode_compatible
class People(models.Model):
    epithet = models.ForeignKey(Epithet, on_delete=models.CASCADE)
    name = models.CharField(db_index=True, max_length=100)

    def __str__(self):
        return self.name

    @staticmethod
    def epithet_by_name(name):
        person = People.objects.filter(name__iexact=name)[:1]
        if person.exists():
            return person[0].epithet.text
        else:
            return People.add_name(name)

    @staticmethod
    def add_name(name):
        print(Epithet.objects.aggregate(Min('uses'))['uses__min'])
        epithets = Epithet.objects.filter(uses=Epithet.objects.aggregate(Min('uses'))['uses__min'])
        if len(epithets) == 0:  # if db table is empty
            return ''
        epithet = epithets[random.randint(0, len(epithets) - 1)]
        people = People(name=name, epithet_id=epithet.id)
        people.save()
        epithet.uses += 1
        epithet.save()
        return epithet.text
