from django.test import TestCase
from .create import TxtParser
# Create your tests here.


class TestParser(TestCase):

#     def test_identify_pattern(self):
#         text = '天空：'
#         a = TxtParser(text)
#         a.parse()
#         self.assertTrue(True)
#     #
#     def test_identify_pattern1(self):
#         text = '天空：\n藍藍的天空'
#         a = TxtParser(text)
#         a.parse()
#         self.assertTrue(True)
#     #
#     def test_identify_pattern2(self):
#         text = '天空：\n\t藍藍的天空'
#         a = TxtParser(text)
#         a.parse()
#         self.assertTrue(True)
#
#     def test_identify_pattern3(self):
#         text = '@我：同義字：吾'
#         a = TxtParser(text)
#         a.parse()
#         self.assertTrue(True)
#
    # def test_identify_pattern4(self):
    #     text = '天空：＃我 ＠同義：蒼芎\n\t藍藍的天空'
    #     a = TxtParser(text)
    #     a.parse()
    #     self.assertTrue(True)

#
    # def test_identify_pattern5(self):
    #     text = '天空：#HAHA #AHA@同義：蒼芎 ＃121ㄅ\n\t@反義\n\t\t地板'
    #     a = TxtParser(text)
    #     a.parse()
    #     self.assertTrue(True)
#
#     def test_identify_pattern6(self):
#         text = '天空： \n\t@反義\n\t\t地板\n\t\t土地\n\t\tdd'
#         a = TxtParser(text)
#         a.parse()
#         self.assertTrue(True)
#
#     def test_identify_pattern7(self):
#         text = '天空： @a&b ＠Ａ：Ｂ：Ｃ ＠a:cc:b\n'
#         a = TxtParser(text)
#         a.parse()
#         self.assertTrue(True)
#
#     def test_identify_pattern8(self):
#         text = """brief:
# 	meaning1: @ see also: brevity
# 		continuing for a short time
# 		@ example:
# 			We stopped by Alice’s house for a brief visit.
# 			Let’s keep this conversation brief; I have a plane to catch.
# 	phrase1:
# 		a brief period/moment/spell etc
# 		@ example:
# 			Greene spent a brief time at Cambridge."""
#         a = TxtParser(text)
#         a.parse()
#         self.assertTrue(True)
# #
#     def test_identify_pattern9(self):
#         text = '我:\n\tistom\n你：\n\t不是我'
#         a = TxtParser(text)
#         a.parse()
#         self.assertTrue(True)

    def test_identify_pattern9(self):
        text = """catastrophe:
	a terrible event in which there is a lot of destruction, suffering, or death
	@同義字：
		disaster:
			a sudden event such as a flood, storm, or accident which causes great damage or suffering
disaster:
	@collocation:
		disaster for
	@thesaures：
		accident :
			an event in which a vehicle is damaged and often someone is hurt:
		crash:
			a serious accident in which a vehicle hits something else:
		wreck:
			American English an accident in which a car or train is badly damaged:"""
        a = TxtParser(text)
        a.parse()
        self.assertTrue(True)
    pass





