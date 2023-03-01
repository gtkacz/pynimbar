import threading
import time
from contextlib import contextmanager
import traceback


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


@contextmanager
def loading_animation(text: str, success_msg: str = 'ok', animation_frequency: float = 0.1, break_on_error: bool = False, verbose_errors: bool = False):
    # Define the loading animation function
    def animate():
        while getattr(threading.current_thread(), "do_run", True):
            for c in '|/-\\':
                if getattr(threading.current_thread(), "do_run", True):
                    print(f"\r{text} {c}", end="", flush=True)
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
        print(f"\r{bcolors.FAIL}{text} {e}{bcolors.ENDC}")
        if break_on_error:
            raise e
        elif verbose_errors:
            traceback.print_exc()
            
    else:
        # Stop the loading animation
        t.do_run = False
        t.join()
        print(f"\r{bcolors.OKGREEN}{text} {success_msg}{bcolors.ENDC}")
