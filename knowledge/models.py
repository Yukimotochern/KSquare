from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete
import knowledge
# Create your models here.


class Concept(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    content = models.TextField()
    click_number = models.IntegerField(default=0, null=False)


class Relation(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    content = models.TextField()
    color = models.CharField(max_length=10, null=True)
    is_sym = models.BooleanField


class ToRelationEntry(models.Model):
    id = models.AutoField(primary_key=True)
    relation_main = models.ForeignKey(Relation, on_delete=models.CASCADE, null=True)
    related_concept = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name='relation_to', null=True)
    # Forth is To's ...
    f_is_t = models.CharField(max_length=30, null=True)


class ForthRelationEntry(models.Model):
    id = models.AutoField(primary_key=True)
    relation_main = models.ForeignKey(Relation, on_delete=models.CASCADE, null=True)
    related_concept = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name='relation_forth', null=True)
    to_relation_partner = models.OneToOneField(ToRelationEntry, on_delete=models.CASCADE,
                                               related_name='forth_relation_partner', null=True)
    # To is Forth's ...
    t_is_f = models.CharField(max_length=30, null=True)


# To and Forth are linked. One deleted also another.
@receiver(post_delete, sender=ForthRelationEntry)
def post_delete_to_relation_entry(sender, instance, *args, **kwargs):
    try:
        instance.to_relation_partner
    except knowledge.models.ToRelationEntry.DoesNotExist:
        return
    if instance.to_relation_partner:  # just in case user is not specified
        instance.to_relation_partner.delete()

# @receiver(post_delete, sender=ToRelationEntry)
# def post_delete_forth_relation_entry(sender, instance, *args, **kwargs):
#     if instance.forth_relation_partner:  # just in case user is not specified
#         instance.forth_relation_partner.delete()

