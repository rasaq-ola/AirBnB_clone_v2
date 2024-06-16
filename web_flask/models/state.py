class State(BaseModel, Base):
    # existing methods ...

    @property
    def cities(self):
        """Return list of City objects related to this State"""
        from models import storage
        from models.city import City
        city_list = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
