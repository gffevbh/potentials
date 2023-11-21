
class Pair:

    def __init__(self, first_elem, second_elem):
        self._first_elem = first_elem
        self._second_elem = second_elem

    @property
    def first_elem(self):
        return self._first_elem

    @first_elem.setter
    def first_elem(self, first_elem):
        self._first_elem = first_elem

    @property
    def second_elem(self):
        return self._second_elem

    @second_elem.setter
    def second_elem(self, second_elem):
        self._second_elem = second_elem
