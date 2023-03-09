import threading
import time
import traceback
from contextlib import contextmanager
from typing import Iterable


@contextmanager
def loading_animation(text: str, success_msg: str = 'ok', animation_frequency: float = 0.1, break_on_error: bool = True, verbose_errors: bool = False, frames: Iterable = '|/-\\'):
    """
    A context manager that displays a loading animation while the code block is running. Can also handle errors.

    Args:
        text (str): The text to display during the animation.
        success_msg (str, optional): The text to display when the animation is done. Defaults to 'ok'.
        animation_frequency (float, optional): The frequency of the animation. Defaults to 0.1.
        break_on_error (bool, optional): Whether to break on error. Defaults to True.
        verbose_errors (bool, optional): Whether to print the error traceback. Defaults to False.
        frames (str, optional): The frames of the animation. Defaults to '|/-\\'.
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    # Define the loading animation function
    def animate():
        while getattr(threading.current_thread(), 'do_run', True):
            for c in frames:
                if getattr(threading.current_thread(), 'do_run', True):
                    print(f'\r{text} {c}', end='', flush=True)
                    time.sleep(animation_frequency)
                else:
                    break

    # Start the loading animation in a separate thread
    t = threading.Thread(target=animate)
    t.start()

    try:
        yield

    except Exception as e:
        # Stop the loading animation
        t.do_run = False
        t.join()
        print(f'\r{FAIL}{text} {e.__class__.__name__}{ENDC}')
        if break_on_error:
            raise e from e
        elif verbose_errors:
            traceback.print_exc()

    else:
        # Stop the loading animation
        t.do_run = False
        t.join()
        print(f'\r{OKGREEN}{BOLD}{text} {success_msg}{ENDC}')
