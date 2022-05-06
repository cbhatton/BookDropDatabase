class Person:

    def __init__(self, person_id: int, name: str):
        self._person_id = person_id
        # self._drop_id = drop_id
        self._name = name

    @property
    def person_id(self):
        return self._person_id

    @property
    def drop_id(self):
        return self._drop_id

    @property
    def name(self):
        return self._name
