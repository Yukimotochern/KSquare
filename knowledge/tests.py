from django.test import TestCase
from knowledge.models import ToRelationEntry, ForthRelationEntry
# Create your tests here.


class ToForthTestCase(TestCase):

    def test_forth_delete_to_delete(self):
        """If Forth deleted so should To"""
        a = ToRelationEntry.objects.create()
        b = ForthRelationEntry.objects.create(to_relation_partner=a)
        b.delete()
        self.assertFalse(a in ToRelationEntry.objects.all())

    def test_to_delete_forth_delete(self):
        """If To deleted so should Forth"""
        c = ToRelationEntry.objects.create()
        d = ForthRelationEntry.objects.create(to_relation_partner=c)
        c.delete()
        self.assertFalse(d in ForthRelationEntry.objects.all())

    # def test_to_delete_forth_delete(self):
    #     """If To deleted so should Forth"""
    #     a = ToRelationEntry.objects.create()
    #     b = ForthRelationEntry.objects.create(to_relation_partner=a)
    #     a.delete()
    #     self.assertFalse(b in ForthRelationEntry.objects.all())


