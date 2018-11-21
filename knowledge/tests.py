from django.test import TestCase
from knowledge.models import ToLink, ForthLink
# Create your tests here.


class ToForthTestCase(TestCase):

    def test_forth_delete_to_delete(self):
        """If Forth deleted so should To"""
        a = ToLink.objects.create()
        b = ForthLink.objects.create(to_link_partner=a)
        b.delete()
        self.assertFalse(a in ToLink.objects.all())

    def test_to_delete_forth_delete(self):
        """If To deleted so should Forth"""
        c = ToLink.objects.create()
        d = ForthLink.objects.create(to_link_partner=c)
        c.delete()
        self.assertFalse(d in ForthLink.objects.all())

    # def test_to_delete_forth_delete(self):
    #     """If To deleted so should Forth"""
    #     a = ToRelationEntry.objects.create()
    #     b = ForthRelationEntry.objects.create(to_relation_partner=a)
    #     a.delete()
    #     self.assertFalse(b in ForthRelationEntry.objects.all())


