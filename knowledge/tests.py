from django.test import TestCase
from knowledge.models import ToLink, ForthLink, Link, Concept
from django.db import IntegrityError, transaction
import time
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

    # def test_concept_unique(self):
    #     """Catch non-unique error inside transaction"""
    #     a = None
    #     b = None
    #
    #     @transaction.atomic
    #     def create_two():
    #         global a, b
    #         with transaction.atomic():
    #             a = Concept.objects.create(_title='try')
    #             b = Concept.objects.create(_title='try')
    #     try:
    #         create_two()
    #     except IntegrityError as e:
    #         self.assertTrue('unique constraint' in e.args[0])
    #         self.assertTrue(a is None)

    def test_create_concept(self):
        a = Concept.objects.create(_title='try')
        a.modify_time = time.time()
        self.assertTrue(a in Concept.objects.all())


