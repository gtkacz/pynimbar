import threading
import time
import traceback
from contextlib import contextmanager


@contextmanager
def loading_animation(text: str, success_msg: str = 'ok', animation_frequency: float = 0.1, break_on_error: bool = False, verbose_errors: bool = False, frames: str = '|/-\\', time_it: bool = False, time_it_live: bool = False):
    """
    A context manager that displays a loading animation while the code block is running and optionally times the execution of the code block, with an option to print the live execution time.

    Args:
        text (str): The text to display during the animation.
        success_msg (str, optional): The text to display when the animation is done. Defaults to 'ok'.
        animation_frequency (float, optional): The frequency of the animation. Defaults to 0.1.
        break_on_error (bool, optional): Whether to break on error. Defaults to False.
        verbose_errors (bool, optional): Whether to print the error traceback. Defaults to False.
        frames (str, optional): The frames of the animation. Defaults to '|/-\\'.
        time_it (bool, optional): Whether to time the execution of the code block. Defaults to False.
        time_it_live (bool, optional): Whether to print the live execution time of the code block. Defaults to False.
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

    def animate():
        start_time = time.time() if time_it or time_it_live else None
        while getattr(threading.current_thread(), 'do_run', True):
            for c in frames:
                if getattr(threading.current_thread(), 'do_run', True):
                    elapsed_time = f' {time.time() - start_time:.2f}s' if time_it_live and start_time is not None else ''
                    print(f'\r{text} {c}{elapsed_time}', end='', flush=True)
                    time.sleep(animation_frequency)
                else:
                    break

    if time_it and time_it_live:
        raise ValueError("You can't use both 'time_it' and 'time_it_live' at the same time.")
    
    t = threading.Thread(target=animate)
    t.start()

    start_time = time.time() if (time_it or time_it_live) else None

    try:
        yield

    except Exception as e:
        if e.__class__ is KeyboardInterrupt:
            t.do_run = False
            t.join()
            raise e

        t.do_run = False
        t.join()
        
        error_msg = str(e)
        
        if (time_it or time_it_live) and start_time is not None:
            elapsed_time = time.time() - start_time
            error_msg += f" (elapsed time: {elapsed_time:.2f} seconds)"

        print(f"\r{FAIL}{text} {error_msg}{ENDC}")

        if break_on_error:
            raise e

        elif verbose_errors:
            traceback.print_exc()

    else:
        t.do_run = False
        t.join()

        if (time_it or time_it_live) and start_time is not None:
            elapsed_time = time.time() - start_time
            success_msg += f" (elapsed time: {elapsed_time:.2f} seconds)"

        print(f"\r{OKGREEN}{text} {success_msg}{ENDC}")
