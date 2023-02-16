"""Word Finder: finds random words from a dictionary."""
from random import choice


class WordFinder:
    """ Class that accepts a File 


        Attributes:
        ______________
        file: init
              word text file
        list: init
              a list of the file
        word: init
              list of file strings without empty space      
    """
    def __init__(self, file):
        
        self.file = file
        self.list = list(open(file, "r"))
        self.words = self.strip()
        print(len(self.words))
        
    def strip(self):    
        """ takes away empty space in strings """
        list = [ w.strip() for w in self.list]
        return list
    def __repr__(self):

        return f"Word List of File: {self.file}"

    def random(self):
        """ Picks random word from file """
        return choice(self.words)
        
        

class SpecialWordFinder(WordFinder):
    def __init__(self, file):
        super().__init__(file)

    def words_only(self):
        """ returns strings without # """
        try:
            pure_words = [w for w in self.words if not w.startswith("#")]
            return choice(pure_words)
        except TypeError:
            print('Expects strings only')
        
        
         




