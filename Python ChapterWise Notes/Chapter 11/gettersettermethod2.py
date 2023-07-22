class year_graduate:
    def __init__(self, year=2045):
        self._year = year
        
    @property
    def get_year(self):
        return self._year # putting _ in front of a variable makes it private

    @get_year.setter
    def get_year(self,a):
        self._year = a
        print(a)

yg = year_graduate()
yg.get_year = 20
