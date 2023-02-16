"""Python serial number generator."""

class SerialGenerator:

    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=100):
        self.start = start

    def __repr__(self):
        return f"Serial Number starts at:{self.start}"

    def generate(self):
        """ It increases the Serial Number by 1 """
        self.start += 1
        return  self.start

    def reset(self):
        """ It resets the Serial Number to 100 """
        self.start = 100
        return self.start
