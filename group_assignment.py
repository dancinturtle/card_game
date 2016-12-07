import random

class Card(object):
	def __init__(self, value, suit):
		self.suit = suit
		self.value = value
	def show(self):
		print str(self.value), str(self.suit)


class Deck(object):
	def __init__(self):
		self.deck = []
		self.createDeck()
	def createDeck(self):
		suits = ["diamonds", "spades", "hearts", "clubs"]
		for suit in suits:
			for value in range(1,14):
				self.deck.append(Card(value,suit))
	def showDeck(self):
		for var in self.deck:
			var.show()
	def shuffle(self):
		random.shuffle(self.deck)
	def burn(self):
		self.deck.pop()
	def count(self):
		print len(self.deck)
	def deal(self):
		# self.hand.append()
		self.deck.pop()


class Player(object):
	def __init__(self, name):
		self.name=name
		self.hand=[]


	def draw(self):
		self.hand.append(Card(card.value,card.sui))
		deal()


			# self.hand.append(draw)


	def discard(self, num):
		self.num=num
		for discard in range(0,self.num):
			self.hand.pop()



test1 = Player("joe")
deck1= Deck()
test1.draw()
print test1.hand
# print test1.hand
# deck1.showDeck()
# test1.shuffle()
# test1.count()
# test1.showDeck()
# print "((((((((((((((((("
# print test1.deck[0].suit, test1.deck[0].value
# card1 =Card(0,3)
# card1.show()
# print card1

# ===========================================
# deal = minus from list
# shuffle = random.shuffle(array)
# 	http://stackoverflow.com/questions/473973/shuffle-an-array-with-python-randomize-array-item-order-with-python
# burn = pop
# cut= ?
# count = count the amount of cards (arr.length)
# create deck =  math.random array 0-51
# show= print arr

# =============================================
