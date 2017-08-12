class Song(object): # class, class, class, class not Class, not CLASS
	
	def __init__(self,lyrics): # There must has a blank space afte the "def" make sure the "_init_" is in the hightlight. anddddddd ,is __init__, not _init_
		self.geci = lyrics
		
	def sing_me_a_song(other):# i changed the previous Argument to "other"
		for line in other.geci:
			print line

happy_bday = Song(["Happy birthday to you", 
					"I don't want to get sued", 
					"So I'll stop right there"])

bulls_on_parade = Song(["They rally around the familiy", 
						"With pockets full of shells"])
						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
