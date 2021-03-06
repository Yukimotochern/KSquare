from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete
from django.contrib.auth.models import User
from tagging.registry import register
import knowledge
from datetime import datetime
from users.models import CustomUser
# Create your models here.


class Concept(models.Model):
    id = models.AutoField(primary_key=True)
    _title = models.CharField(max_length=100)
    summary = models.CharField(max_length=300, null=True)
    content = models.TextField(null=True)
    create_time = models.DateTimeField(null=True)
    modify_time = models.DateTimeField(null=True)
    owner = models.ForeignKey('users.CustomUser', null=True, on_delete=models.CASCADE, related_name='created_concepts')
    editors = models.ManyToManyField('users.CustomUser', related_name='editable_concepts')
    viewers = models.ManyToManyField('users.CustomUser', related_name='viewable_concepts')
    public = models.BooleanField(default=True)
    click_number = models.IntegerField(default=0, null=False)

    def __str__(self):
        return self._title

    def __eq__(self, other):
        return self.id == other.id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value.strip(" ")

    @classmethod
    def create(cls, title=''):
        cls.objects.create(_title=title)


class Link(models.Model):
    id = models.AutoField(primary_key=True)
    relation = models.ForeignKey('Relation', on_delete=models.CASCADE, related_name='links', null=True)
    to_concept = models.OneToOneField('Concept', on_delete=models.CASCADE, related_name='to_link', null=True)
    forth_concept = models.OneToOneField('Concept', on_delete=models.CASCADE, related_name='forth_link', null=True)

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return f"{self.to_concept.title} -> {self.forth_concept.title} {self.relation.t_is_f} @ {self.relation.title}"


class Relation(models.Model):
    id = models.AutoField(primary_key=True)
    _title = models.CharField(max_length=30)
    content = models.TextField()
    color = models.CharField(max_length=10, null=True)
    is_sym = models.BooleanField
    # To is Forth's ...
    t_is_f = models.CharField(max_length=30, null=True)
    # Forth is To's ...
    f_is_t = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self._title

    def __eq__(self, other):
        return self.id == other.id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value.strip(" ")


class ToLink(models.Model):
    id = models.AutoField(primary_key=True)
    relation_main = models.ForeignKey(Relation, on_delete=models.CASCADE, null=True)
    related_concept = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name='to_links', null=True)

    def __str__(self):
        return f"{self.relation_main.title}: {self.related_concept.title} " \
               f"-> {self.forth_link_partner.related_concept.title}"


class ForthLink(models.Model):
    id = models.AutoField(primary_key=True)
    relation_main = models.ForeignKey(Relation, on_delete=models.CASCADE, null=True)
    related_concept = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name='forth_links', null=True)
    to_link_partner = models.OneToOneField(ToLink, on_delete=models.CASCADE, related_name='forth_link_partner'
                                           , null=True)

    def __str__(self):
        return f"{self.relation_main.title}: {self.related_concept.title} " \
               f"<- {self.to_link_partner.related_concept.title}"

# To and Forth are linked. One deleted also another.


@receiver(post_delete, sender=ForthLink)
def post_delete_to_link(sender, instance, *args, **kwargs):
    try:
        instance.to_link_partner
    except knowledge.models.ToLink.DoesNotExist:
        return
    if instance.to_link_partner:
        instance.to_link_partner.delete()


# @receiver(post_delete, sender=ToRelationEntry)
# def post_delete_forth_relation_entry(sender, instance, *args, **kwargs):
#     if instance.forth_relation_partner:  # just in case user is not specified
#         instance.forth_relation_partner.delete()


def get_or_create_by_title(cls, title_in=""):
    title_in = title_in.strip(" ")
    try:
        ob = cls.objects.get(_title=title_in)
    except cls.DoesNotExist:
        ob = cls.objects.create()
        ob.title = title_in
        ob.save()
    return ob


register(Concept)
register(Relation)
register(ToLink)
register(ForthLink)
register(Link)

















