from disk import Disk


class Tower(list, Disk):
    def __init__(self, name, startingNo):
        super().__init__()
        self.__name = name
        self._list = []
        for i in startingNo:
            self._list.append(Disk(i + 1))


    def add_disk(self, size):
        self.append(Disk(size))
        return self

    def subtract_disk(self, size):
        self.pop(int(Disk(size).__str__()))
        return self

    def __str__(self):
        print('Tower ', self.__name, ' :', self._list)



