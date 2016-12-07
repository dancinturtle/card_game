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
	def count(self):
		print len(self.deck)

	# AMY:  The burn and deal functions are the same, so consider combining them - keep it DRY (Don't Repeat Yourself)
	def burn(self):
		self.deck.pop()

	def deal(self):

		# AMY:  Consider when the deal method is called - it looks like you're using it in the Player class in its draw method. So this method better have a return back to the Player class. Remember that a function call is equal to whatever that function returns. So when the player calls the draw method, the player wants something back - it wants the card back.

		# self.deck.pop()
		#AMY: changed the above line to the one below
		return self.deck.pop()



class Player(object):
	def __init__(self, name):
		self.name=name
		self.hand=[]


	def draw(self, deckinstance):
		# AMY: Here, you're creating a brand new card and trying to access variables that you do not have (card is not known within this scope, so neither is card.value nor card.sui, and then deal() is not a method that is callable here.) What you want to do is refer to a particular deck's deal method. Here, as we're setting up our class for the player, we don't want to limit ourselves to a particular instance of the card class, so it would be best to allow the card to be passed in as a parameter. I added in deck as a parameter.
		# AMY: changing the lines below
		# self.hand.append(Card(card.value,card.sui))
		# deal()
		# AMY: altering to the lines below
		drawncard = deckinstance.deal() # whatever deck got passed in as a parameter, we'll use that deck's deal method and get back a card
		self.hand.append(drawncard) # and we'll add that drawncard to our hand
		return self #this will allow for method chaining, because the player instance itself gets returned, and the player instance has methods and attributes that can be referenced using dot notation


			# self.hand.append(draw)


	def discard(self, num):
		self.num=num
		for discard in range(0,self.num):
			self.hand.pop()



test1 = Player("joe")

deck1= Deck()
deck1.shuffle()

test1.draw(deck1).draw(deck1).draw(deck1).draw(deck1)


print "Joe's hand"
for card in test1.hand:
	#AMY: expecting 4 random cards to be printed
	print card.value, card.suit

# test1.draw()
# print test1.hand
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
