from tower import Tower
from disk import Disk


class TowersOfHanoi:

    def __init__(self, num_disks):
        self.__num_disks = num_disks
        self.__num_of_moves = 0
        self.__towers = [Tower('A'), Tower('B'), Tower('C')]
        for i in range(num_disks):
            self.__towers[0].append(Disk(num_disks - i))

    def get_num_of_moves(self):
        return self.__num_of_moves

    def move_disks(self, num_disks_to_move, beg_tow, aux_tow, end_tow):
        if num_disks_to_move == 1:
            beg_tow.move(end_tow)
            self.__num_of_moves += 1
            self.display_towers()
        else:
            self.move_disks(num_disks_to_move - 1, beg_tow, end_tow, aux_tow)
            self.move_disks(1, beg_tow, aux_tow, end_tow)
            self.move_disks(num_disks_to_move - 1, aux_tow, beg_tow, end_tow)

    def play(self):
        self.move_disks(self.__num_disks, self.__towers[0], self.__towers[2], self.__towers[1])

    def display_towers(self):
        if self.__num_disks == 5:
            i = self.get_num_of_moves()
            if i == self.get_num_of_moves():
                print('Towers:\n', self.__towers[0], '\n', self.__towers[1], '\n', self.__towers[2], '\n')
