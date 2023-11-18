from classes import GameOfLife


def main() -> None:
    g = GameOfLife('input.txt')
    g.run()

if __name__ == "__main__":
    main()