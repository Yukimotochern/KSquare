from knowledge.models import Relation, ToLink, ForthLink, Concept
from random import shuffle
from copy import deepcopy

class TreeCell:
    def __init__(self, related_string, context_ob, ob, position=None, re=False):
        self.related_string = related_string
        self.context_ob = context_ob
        self.ob = ob
        self.position = position
        self.re = re


class ConceptsGroupByRelation:
    def __init__(self, relation, related_string=""):
        self.relation = relation
        self.total_concepts = []
        self.related_string = related_string
        self.chosen_concepts = []

    def chose_one(self):
        a = self.total_concepts.pop()
        self.chosen_concepts.append(a)

    def put_back_one(self):
        a = self.chosen_concepts.pop()
        self.total_concepts.append(a)


class TreeViewModel:
    def __init__(self, main_view_concept):
        self.main_view_concept = main_view_concept
        links = []
        links.extend([a.forth_link_partner for a in list(main_view_concept.to_links.all())])
        links.extend([a.to_link_partner for a in list(main_view_concept.forth_links.all())])
        concept_group_by_relation_list = []
        shuffle(links)
        for li in links:
            found = False
            if len(concept_group_by_relation_list) != 0:
                for cgbrl in concept_group_by_relation_list:
                    if li.relation_main == cgbrl.relation:
                        found = True
                        cgbrl.total_concepts.append(li.related_concept)
                        if isinstance(li, ToLink):
                            cgbrl.related_string = li.relation_main.t_is_f
                        else:
                            cgbrl.related_string = li.relation_main.f_is_t
                        break
            if not found:
                if isinstance(li, ToLink):
                    cg = ConceptsGroupByRelation(relation=li.relation_main, related_string=li.relation_main.t_is_f)
                else:
                    cg = ConceptsGroupByRelation(relation=li.relation_main, related_string=li.relation_main.f_is_t)
                cg.total_concepts.append(li.related_concept)
                concept_group_by_relation_list.append(cg)

        tree_cell_pages = []
        while num(concept_group_by_relation_list) != 0:
            tree_cell_page = []
            page_re = get_first_none_zeros(concept_group_by_relation_list, 6)
            while num(page_re) != 0:
                for pr in page_re:
                    try:
                        pr.chose_one()
                    except IndexError:
                        pass

            for pr in page_re:
                cgbr = TreeCell(related_string=pr.related_string, context_ob=pr.relation, ob=pr.relation, re=True)
                tree_cell_page.append(cgbr)
                for tcc in pr.chosen_concepts:
                    con_in_cg = TreeCell(related_string=pr.related_string, context_ob=pr.relation, ob=tcc)
                    tree_cell_page.append(con_in_cg)
            tree_cell_pages.append(tree_cell_page)
        try:
            self.tree_cell_page = tree_cell_pages[0]
        except IndexError:
            self.tree_cell_page = None


def positioning(cells):
    if cells is None:
        return None
    re_num = 0
    co_num = 0
    co_num_by_re = [0] * 6
    re_index = -1
    for c in cells:
        if isinstance(c.ob, Relation):
            re_index += 1
            re_num += 1
        else:
            co_num += 1
            co_num_by_re[re_index] += 1
    cell_num = re_num + co_num
    space_num = 12 - cell_num
    po = ['lt', 't1', 't2', 'rt', 'r1', 'r2', 'rb', 'b2', 'b1', 'lb', 'l2', 'l1', ]
    by_sequence = False
    if re_num == 6 or re_num == 1:
        by_sequence = True
    elif re_num == 5 or re_num == 4:
        po_to_assign = iter(po)
        cell_to_assign = iter(cells)
        re_to_assign = iter(co_num_by_re)
        while True:
            try:
                next(cell_to_assign).position = next(po_to_assign)
                next(cell_to_assign).position = next(po_to_assign)
                try:
                    cr = next(re_to_assign)
                    if cr == 1 and space_num != 0:
                        for i in range(cr-1):
                            next(cell_to_assign).position = next(po_to_assign)
                        next(po_to_assign)
                        space_num -= 1
                    elif cr == 3 and space_num >= 2:
                        for i in range(cr-1):
                            next(cell_to_assign).position = next(po_to_assign)
                        for i in range(2):
                            next(po_to_assign)
                            space_num -= 1
                    elif cr == 4 and space_num >= 1:
                        for i in range(cr-1):
                            next(cell_to_assign).position = next(po_to_assign)
                        next(po_to_assign)
                        space_num -= 1
                    else:
                        for i in range(cr-1):
                            next(cell_to_assign).position = next(po_to_assign)
                except StopIteration:
                    continue
            except StopIteration:
                break
    elif re_num == 3 or re_num == 2:
        po_to_assign = iter(po)
        cell_to_assign = iter(cells)
        re_to_assign = iter(co_num_by_re)
        while True:
            try:
                cr = next(re_to_assign)
                next(cell_to_assign).position = next(po_to_assign)
                next(cell_to_assign).position = next(po_to_assign)
                try:
                    if cr == 1 and space_num > 4:
                        for i in range(cr-1):
                            next(cell_to_assign).position = next(po_to_assign)
                        for i in range(4):
                            next(po_to_assign)
                        space_num -= 4
                    elif cr == 2 and space_num > 4:
                        for i in range(cr-1):
                            next(cell_to_assign).position = next(po_to_assign)
                        for i in range(2):
                            next(po_to_assign)
                        space_num -= 2
                    elif cr == 1 and space_num > 2:
                        for i in range(cr-1):
                            next(cell_to_assign).position = next(po_to_assign)
                        for i in range(2):
                            next(po_to_assign)
                        space_num -= 2
                    elif cr == 1 and space_num > 1:
                        next(po_to_assign)
                        space_num -= 1
                    else:
                        for i in range(cr - 1):
                            next(cell_to_assign).position = next(po_to_assign)
                except StopIteration:
                    continue
            except StopIteration:
                break
    if by_sequence:
        po_to_assign = iter(po)
        for c in cells:
            c.position = next(po_to_assign)
    return cells


def num(concepts_group_by_relation):
    total = 0
    for cgbr in concepts_group_by_relation:
        total += len(cgbr.total_concepts)
    return total


def rema(concepts_group_by_relation):
    total = 0
    for cgbr in concepts_group_by_relation:
        total += len(cgbr.chosen_concepts)
    return total


def get_first_none_zeros(concepts_group_by_relation, at_most):
    number = 0
    li = []
    for cgbr in concepts_group_by_relation:
        if len(cgbr.total_concepts) != 0:
            li.append(cgbr)
            number += 1
            if number == at_most:
                break
    return li








