from random import randint
from time import sleep

from pynimbar.src import loading_animation


def main():
    def pre(txt: str):
        randomizer = randint(1, 10)

        with loading_animation(txt, break_on_error=False):
            sleep(randomizer//2)

            if 1 <= randomizer <= 3:
                0 / 0

    LINES = 5

    inputs = [f'Loading {i+1}' for i in range(LINES)]

    list(map(pre, inputs))


if __name__ == "__main__":
    main()
