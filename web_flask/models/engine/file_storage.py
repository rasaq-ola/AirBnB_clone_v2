class FileStorage:
    # existing methods ...

    def close(self):
        """Call reload method for deserializing the JSON file to objects"""
        self.reload()
