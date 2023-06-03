class Movie():
    def __init__(self, id, title=None, duration=None, released=None) -> None:
        self.id = id
        self.title = title
        self.duration = duration
        self.released = released

# funcion de conversion a json
    def to_JSON(self):
        return {
            'id': self.id,
            'title': self.title,
            'duration': self.duration,
            'released': self.released
        }
