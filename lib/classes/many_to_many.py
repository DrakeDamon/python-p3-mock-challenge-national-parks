class NationalPark:
    all = []
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Must be a string")
        if not len(name) >= 3:
            raise ValueError("Name must be at least 3 characters long")
        self._name = name
        

    @property
    def name(self):
        if hasattr(self, '_name'):
            return self._name
        raise ValueError("Cannot change the name of the national_park")
    
    




    def trips(self):
      return [trip for trip in Trip.all if trip.national_park == self]

    
    def visitors(self):
        park_trips = self.trips()
        return list(set([trip.visitor for trip in park_trips]))
    def total_visits(self):
        park_trips = self.trips()
        return len(park_trips)   
    def best_visitor(self):
        park_trips = self.trips()
        count_dict = {}
        for trip in park_trips:
            count_dict[trip.visitor] = count_dict.get(trip.visitor, 0) + 1

        return max(count_dict, key=count_dict.get)


class Trip:
    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date
    

    @start_date.setter
    def start_date(self, value):
        if not isinstance(value, str):
            raise ValueError("Must be a valid date")
        if not len(value) >= 7:
            raise ValueError("Must be greater than or equal to 7 characters")
        if not value.endswith(("st", "nd", "rd", "th")):
            raise ValueError("Date must end with st, nd, rd, or th")
        self._start_date = value
        

    @property
    def end_date(self):
        return self._end_date
    

    @end_date.setter
    def end_date(self, value):
        if not isinstance(value, str):
            raise ValueError("Must be a valid date")
        if not len(value) >= 7:
            raise ValueError("Must be greater than or equal to 7 characters")
        if not value.endswith(("st", "nd", "rd", "th")):
            raise ValueError("Date must end with st, nd, rd, or th")
        self._end_date = value
    


class Visitor:

    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Must be a string")
        if not 1 <= len(value) <= 15:
            raise ValueError("Name must be between 1 and 15 characters long")
        self._name = value
    
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    def national_parks(self):
        park_trips = self.trips()
        return list(set([trip.national_park for trip in park_trips]))

    
    def total_visits_at_park(self, park):
        pass