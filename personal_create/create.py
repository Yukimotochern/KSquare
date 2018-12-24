import re
import copy

# patterns
title_pattern = re.compile(r"(?P<title>[^@:#&＠：＃＆]+(?<! ))([:：]) *(?P<labels>.+)?")
full_link_pattern = re.compile(r"""
    [＠@]
    ((\ *(?P<title1>(?!\ )[^@:#&＠：＃＆]+(?<!\ ))\ *
    [&＆]
    \ *(?P<title2>(?!\ )[^@:#&＠：＃＆]+(?<!\ ))\ *
    [:：]?
    \ *(?P<relation1>(?!\ )[^@:#&＠：＃＆]+(?<!\ ))?\ *)
    |
    (\ *(?P<title3>(?!\ )[^@:#&＠：＃＆]+(?<!\ ))\ *
    [：:]
    \ *(?P<relation2>(?!\ )[^@:#&＠：＃＆]+(?<!\ ))\ *
    [:：]\ *(?P<title4>(?!\ )[^@:#&＠：＃＆]+(?<!\ ))\ *))
""", re.X)
half_link_pattern = re.compile(r"[＠@] *(?P<relation>(?! )[^@:#&＠：＃＆]+(?<! )) *[：:] *(?P<title>(?! )[^@:#&＠：＃＆]+(?<! )) *")
empty_link_pattern = re.compile(r"[＠@] *(?P<relation>(?! )[^@:#&＠：＃＆]+(?<! ))[:：]?\b")
hash_tag_pattern = re.compile(r"[#＃] *(?P<hash_tag>(?! )[^@:#&＠：＃＆]+(?<! ))[:：]?\b")


def expression_identify(txt):

    # title
    title_match = Title(txt)
    if title_match.found:
        return title_match

    # Full link
    full_links = FullLink(txt)
    if full_links.found:
        return full_links

    # Half link
    half_links = HalfLink(txt)
    if half_links.found:
        return half_links

    # Empty link
    empty_link_match = [r.groupdict() for r in empty_link_pattern.finditer(txt)]
    if empty_link_match:
        return EmptyLink(empty_link_match)

    # Pure Content
    return txt


class Level:

    def __init__(self):
        self.previous = None
        self.next = None
        self.open_concept = None
        self.open_links = []
        self.closed_links = []
        self.closed_concepts = []

    def add_next(self, level):
        level.previous = self
        self.next = level

    def inputs(self, ob, txt, level):

        # Get upper open levels with specificity
        upper_levels, last_open_concept, last_open_concept_level, last_open_links, \
            last_open_links_level = self.get_uppers()
        # Close open lower level
        self.close_lowers()
        # Clear current level tasks
        self.close_task()

        # Arrange current work and add to or modify upper level
        # First, classify ob by instance
        pure_text_fall_back = False
        pure_text = False
        if isinstance(ob, Title):
            # Construct Current Task
            if last_open_concept:
                index = last_open_concept.add_concept_child()
                for link in ob.links:
                    link.hierarchy = index
            self.closed_links.extend(ob.links)
            self.open_concept = TxtConcept(ob.title_txt, ob.content, ob.hash_tags)  # .title .summary .tags
            default_link = False
            if last_open_concept:
                if last_open_links:
                    if last_open_concept_level > last_open_links_level:  # Equal should not be possible
                        # Make explicit relative links
                        new_links = copy.deepcopy(last_open_links.open_links)
                        for link in new_links:
                            link.hierarchy = last_open_concept.add_concept_child()
                        self.closed_links.extend(HalfLink.make_full_links(ob.title_txt, new_links))
                    else:
                        # Make default links with hierarchy in mind
                        default_link = True
                else:
                    # Make default links with hierarchy in mind
                    default_link = True
            else:
                pass  # Do nothing
            if default_link:
                # Make default links with hierarchy in mind
                self.closed_links.append(TxtLink(
                        ob.title_txt,
                        last_open_concept.open_concept.title,
                        'default',
                        hierarchy=last_open_concept.add_concept_child()
                    )
                )
        elif isinstance(ob, FullLink):
            self.closed_links.extend(ob.links)
        elif isinstance(ob, HalfLink):
            if last_open_concept:
                ob.make_full(last_open_concept.open_concept.title)
                self.closed_links.extend(ob.links)
            else:
                pure_text_fall_back = True
        elif isinstance(ob, EmptyLink):
            if last_open_concept:
                ob.make_half(last_open_concept.open_concept.title)
                self.open_links.extend(ob.links)
            else:
                pure_text_fall_back = True
        else:
            pure_text = True
        if last_open_concept:
            if last_open_concept.open_concept.summary == "":
                front = ''
            else:
                front = '\n'
        if pure_text_fall_back:
            if last_open_concept:
                if last_open_concept_level > 1:
                    front += '\t' * (last_open_concept_level - 1)
                last_open_concept.add_concept_content(txt, front=front)
        elif pure_text:
            if last_open_links:
                if last_open_concept_level > last_open_links_level:
                    self.open_concept = TxtConcept(txt, "", None, hierarchy=last_open_concept.add_concept_child())
                    new_links = copy.deepcopy(last_open_links.open_links)
                    for link in new_links:
                        link.hierarchy = last_open_concept.add_concept_child()
                    self.closed_links.extend(HalfLink.make_full_links(txt, new_links))
                else:
                    if last_open_concept_level > 1:
                        front += '\t' * (last_open_concept_level - 1)
                    last_open_concept.add_concept_content(txt, front=front)
            else:
                if last_open_concept:
                    if last_open_concept_level > 1:
                        front += '\t' * (last_open_concept_level - 1)
                    last_open_concept.add_concept_content(txt, front=front)
                else:
                    pass

    def close_task(self):
        if self.open_concept:
            self.closed_concepts.append(self.open_concept)
            self.open_concept = None
        if self.open_links:
            self.open_links = []

    def get_uppers(self):
        upper_levels = []
        last_open_concept = None
        last_open_concept_relative_level = None
        last_open_links = None
        last_open_links_relative_level = None
        current_level = self
        relative_level = 0
        while current_level.previous:
            current_level = current_level.previous
            relative_level += 1
            if current_level.open_concept or current_level.open_links:
                if current_level.open_concept and not last_open_concept:
                    last_open_concept_relative_level = relative_level
                    last_open_concept = current_level
                    pass
                if current_level.open_links and not last_open_links:
                    last_open_links_relative_level = relative_level
                    last_open_links = current_level
                    pass
                upper_levels.append((relative_level, current_level))
        return upper_levels, last_open_concept, last_open_concept_relative_level, \
            last_open_links, last_open_links_relative_level

    def close_lowers(self):
        current_level = self
        while current_level.next:
            current_level = current_level.next
            if current_level.open_concept or current_level.open_links:
                current_level.close_task()

    def add_concept_child(self):
        self.open_concept.current_child_index += 1
        return self.open_concept.current_child_index

    def add_concept_content(self, content, front='', back=''):
        self.open_concept.summary += front + content + back


class LevelChain:

    def __init__(self):
        self.current_level = 0
        self.root_level = None
        self.levels = []
        self.add_level()

    def parse(self, text, level):
        while self.current_level < level:
            self.add_level()
        self.levels[level].inputs(expression_identify(text), text, level)

    def add_level(self):
        new_level = Level()
        cur = self.current_level
        if self.levels:
            self.levels[cur].add_next(new_level)
            self.levels.append(new_level)
            self.current_level += 1
        else:
            self.root_level = new_level
            self.levels.append(new_level)


class TxtParser:

    def __init__(self, text):
        chain = LevelChain()
        self.chain = chain
        self.text = text

    def parse(self):
        lines = self.text.split('\n')
        for line in lines:
            pattern = re.compile(r'^(?P<tabs>[\t]+)(?P<expression>.+)')
            match = pattern.match(line)
            if match:
                level = len(match.group('tabs'))
                expression = match.group('expression')
            else:
                level = 0
                expression = line
            self.chain.parse(expression, level)
        for level in self.chain.levels:
            level.close_task()
        concepts_list = []
        links_list = []
        for level in self.chain.levels:
            concepts_list.extend(level.closed_concepts)
            links_list.extend(level.closed_links)
        for concept in concepts_list:
            print(concept)
        for link in links_list:
            print(link)


class Title:

    def __init__(self, txt):
        title_match = title_pattern.match(txt)
        if not title_match:
            self.found = False
        else:
            title = title_match.group('title')
            label = title_match.group('labels')
            self.title_txt = title
            if label:
                self.links = FullLink.get_full_links(label)
                if label:
                    label = full_link_pattern.sub("", label)
                    half = HalfLink.get_full_links(title, label)
                if half:
                    self.links.extend(half)
            else:
                self.links = []
            self.content = ""
            if not label:
                self.hash_tags = []
            else:
                self.hash_tags = hash_tag_pattern.findall(label)
            self.found = True


class FullLink:

    def __init__(self, txt):
        self.links = FullLink.get_full_links(txt)
        if self.links:
            self.found = True
        else:
            self.found = False

    @classmethod
    def get_full_links(cls, txt):
        links = []
        if not txt:
            return links
        dic = [r.groupdict() for r in full_link_pattern.finditer(txt)]
        if not dic:
            return links
        for match in dic:
            t1 = match['title1']
            t2 = match['title2']
            r1 = match['relation1']
            t3 = match['title3']
            t4 = match['title4']
            r2 = match['relation2']
            if t1 and t2:
                if r1:
                    links.append(TxtLink(t1, t2, r1))
                else:
                    links.append(TxtLink(t1, t2, 'default'))
            if t3 and t4:
                if r2:
                    links.append(TxtLink(t3, t4, r2))
                else:
                    links.append(TxtLink(t3, t4, 'default'))
        return links


class HalfLink:

    def __init__(self, txt):
        self.links = HalfLink.get_half_links(txt)
        if self.links:
            self.found = True
        else:
            self.found = False

    def make_full(self, txt):
        for link in self.links:
            link.title1 = txt

    @classmethod
    def make_full_links(cls, txt, links):
        for link in links:
            link.title1 = txt
        return links

    @classmethod
    def get_full_links(cls, title1, txt):
        return cls.make_full_links(title1, cls.get_half_links(txt))

    @classmethod
    def get_half_links(cls, txt):
        links = []
        if not txt:
            return links
        dic = [r.groupdict() for r in half_link_pattern.finditer(txt)]
        if not dic:
            return links
        for match in dic:
            t = match['title']
            r = match['relation']
            if t or r:
                links.append(TxtLink(None, t, r))
        return links


class EmptyLink:

    def __init__(self, dic):
        self.links = []
        for match in dic:
            r = match['relation']
            self.links.append(TxtLink(None, None, r))

    def make_half(self, title):
        for link in self.links:
            link.title2 = title


class TxtLink:

    def __init__(self, title1, title2, relation, hierarchy=0):
        self.title1 = title1
        self.title2 = title2
        self.relation = relation
        self.hierarchy = hierarchy

    def __str__(self):
        return f"{self.title1} and {self.title2} has {self.relation} relation with hierarchy {self.hierarchy}"


class TxtConcept:

    def __init__(self, title, summary, tags, hierarchy=0):
        self.title = title
        self.summary = summary
        self.tags = tags
        self.hierarchy = hierarchy
        self.current_child_index = 0

    def __str__(self):
        return f"{self.title}: {self.summary} tags with {self.tags}"




