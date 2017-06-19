#Uses a builder to emulate a flowchart in the console. It references PurchaseFlowchart.png.
#Inspired by an old school assignment.

#Decision() class contains the possible outcomes of the decision at each juncture
class Decision():
	def __init__(self, question, yes, no):
		self.question = question
		self.yes = yes
		self.no = no
	def answer(self, ans):
		ans = ans.lower()
		if ans == 'y':
			return self.yes
		elif ans == 'n':
			return self.no

def ask(dec):
	ans = str(raw_input(dec.question))
	nextThing = dec.answer(ans)
	#If the result of the decision leads to another decision, recurse,
	#otherwise, print the result
	if isinstance(nextThing, Decision):
		ask(nextThing)
	else:
		print nextThing

#Creates all the decision instances
def build():
	XG200 = "Buy the XG200 model."
	XG100 = "Buy the XG100 model."
	XG300 = "Buy the XG300 model."
	ZR100 = "Buy the ZR100 model."
	ZR200 = "Buy the ZR200 model."
	ZR300 = "Buy the ZR300 model."
	jump = Decision('Do you like to jump? (y/n) ', ZR300, ZR200)
	expertSki = Decision('Are you an expert? (y/n) ', jump, ZR200)
	skiBefore = Decision('Have you gone skiing before? (y/n) ', expertSki, ZR100)
	downhill = Decision('Do you want to buy downhill skis? (y/n) ', skiBefore, 'Try skiing someday.')
	goFast = Decision('Do you like to go fast? (y/n) ', XG300, XG200)
	expertBoard = Decision('Are you an expert? (y/n) ', goFast, XG200)
	boardBefore = Decision('Have you snowboarded before? (y/n) ', expertBoard, XG100)
	begin = Decision('Do you want to buy a snowboard? (y/n) ', boardBefore, downhill)
	ask(begin)

build()