
from datetime import date


class President(object):

    def __init__(self,index):
        self.num = index
        self._lname = None
        self._fname = None
        self._bdate = None
        self._ddate = None
        self._birthplace = None
        self._birth_state = None
        self._ts_date = None
        self._te_date = None
        self._party = None
        self._get_data(index)

    @staticmethod
    def _make_date(date_string):
        if date_string == "NONE":
            return date.today()
        else:
            year, month, day = date_string.split('-')
        return date(int(year), int(month), int(day))

    def _get_data(self,index):
        with open("../DATA/presidents.txt") as pfile:
            for line in pfile:
                fields = line.split(":")
                if int(fields[0]) == int(index):
                    self._lname = fields[1]
                    self._fname = fields[2]
    
                    self._birth_date = self._make_date(fields[3])
                    self._death_date = self._make_date(fields[4])

                    self._birthplace = fields[5]
                    self._birth_state = fields[6]
    
                    self._ts_date = self._make_date(fields[7])
                    self._te_date = self._make_date(fields[8])
    
                    self._party = fields[9]
    
                    break

    @property
    def last_name(self):
        return self._lname

    @property
    def first_name(self):
        return self._fname

    @property
    def birth_date(self):
        return self._birth_date

    @property
    def death_date(self):
        return self._death_date

    @property
    def birth_place(self):
        return self._birthplace

    @property
    def birth_state(self):
        return self._birth_state

    @property
    def term_start(self):
        return self._ts_date

    @property
    def term_end(self):
        return self._te_date

    @property
    def party(self):
        return self._party

