from towers_of_hanoi import TowersOfHanoi


def main():
    print("Towers of Hanoi\n===============")
    for i in range(3, 25):
        game = TowersOfHanoi(i)
        game.play()
        print("Moving ", i, " completed in ", game.get_num_of_moves(), " moves!")


main()
