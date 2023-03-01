from pynimbar import loading_animation
from time import sleep


def main():
    with loading_animation("Loading step 1..."):
        sleep(2)

    with loading_animation("Loading step 2..."):
        sleep(3)
        raise Exception("Something went wrong!")

    with loading_animation("Loading step 3..."):
        sleep(3)


if __name__ == "__main__":
    main()
