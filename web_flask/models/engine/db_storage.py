class DBStorage:
    # existing methods ...

    def close(self):
        """Close the working SQLAlchemy session"""
        self.__session.remove()
