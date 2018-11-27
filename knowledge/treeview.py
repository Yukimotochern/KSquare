from knowledge.models import Relation, ToLink, ForthLink, Concept
from random import shuffle


class TreeCell:
    def __init__(self, related_string, context_ob, ob, position=None, re=False):
        self.related_string = related_string
        self.context_ob = context_ob
        self.ob = ob
        self.position = position
        self.re = re


class ConceptsGroupByRelation:
    def __init__(self, relation, total_concepts=[], related_string=""):
        self.relation = relation
        self.total_concepts = total_concepts
        self.related_string = related_string

    # def chose_one(self):
    #     a = self.total_concepts.pop()
    #     self.chosen_concepts.append(a)
    #
    # def put_back_one(self):
    #     a = self.chosen_concepts.pop()
    #     self.total_concepts.append(a)


class TreeViewModel:
    def __init__(self, main_view_concept):
        self.main_view_concept = main_view_concept
        links = []

        links.extend([a.forth_link_partner for a in list(main_view_concept.to_links.all())])
        links.extend([a.to_link_partner for a in list(main_view_concept.forth_links.all())])
        concept_group_by_relation_list = []
        for li in links:
            print(len(links))
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
                    cgbrl = ConceptsGroupByRelation(relation=li.relation_main, related_string=li.relation_main.t_is_f)
                else:
                    cgbrl = ConceptsGroupByRelation(relation=li.relation_main, related_string=li.relation_main.f_is_t)
                cgbrl.total_concepts.append(li.related_concept)
                concept_group_by_relation_list.append(cgbrl)
        tree_cell_pages = []
        tree_cell_page = []
        while len(concept_group_by_relation_list) != 0:
            cur_page_fill = 0
            if len(concept_group_by_relation_list) > 6:
                page_re = concept_group_by_relation_list[0:6]
            else:
                page_re = concept_group_by_relation_list
            all_cons = 0
            for pr in page_re:
                all_cons += len(pr.total_concepts)
            if all_cons == 0:
                break
            while cur_page_fill < 12 and cur_page_fill < all_cons:
                for pr in page_re:
                    if len(pr.total_concepts) == 0:
                        try:
                            concept_group_by_relation_list.remove(pr)
                        except:
                            pass
                        continue
                    cgbr = TreeCell(related_string=pr.related_string, context_ob=pr.relation, ob=pr.relation, re=True)
                    tree_cell_page.append(cgbr)
                    cur_page_fill += 1
                    for tcc in pr.total_concepts:
                        con_in_cg = TreeCell(related_string=pr.related_string, context_ob=pr.relation, ob=tcc)
                        tree_cell_page.append(con_in_cg)
                        pr.total_concepts.remove(tcc)
                        cur_page_fill += 1
            tree_cell_pages.append(tree_cell_page)
        try:
            self.tree_cell_page = tree_cell_pages[0]
        except IndexError:
            self.tree_cell_page = None

    @classmethod
    def positioning(cls, cells):
        if cells is None:
            return None
        re_num = 0
        co_num = 0
        co_num_by_re = [0] * 7
        re_index = 0
        for c in cells:
            if isinstance(c, Relation):
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
                    try:
                        cr = next(re_to_assign)
                        this_assign = 0
                    except StopIteration:
                        break
                    next(cell_to_assign).position = next(po_to_assign)
                    next(cell_to_assign).position = next(po_to_assign)
                    try:
                        if cr == 1 and space_num > 4:
                            for i in range(3):
                                next(cell_to_assign).position = next(po_to_assign)
                            space_num -= 3
                            this_assign += 3
                        elif cr == 2 and space_num > 4:
                            for i in range(2):
                                next(cell_to_assign).position = next(po_to_assign)
                            space_num -= 2
                            this_assign += 2
                        elif cr == 1 and space_num > 2:
                            for i in range(2):
                                next(cell_to_assign).position = next(po_to_assign)
                            space_num -= 2
                            this_assign += 2
                        elif cr == 1 and space_num > 1:
                            next(cell_to_assign).position = next(po_to_assign)
                            space_num -= 1
                            this_assign += 1
                        else:
                            for i in range(cr - this_assign):
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













