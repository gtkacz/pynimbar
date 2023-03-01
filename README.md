# pynimbar

`pynimbar` is a Python package that provides a simple and customizable loading animation for console-based applications. The package allows you to create loading animations with custom text, as well as adjust the animation speed and style.

## Installation

You can install `pynimbar` using pip:
```sh
pip install pynimbar
```

## Usage
`pynimbar` provides a context manager that allows you to use the loading animation as a context manager. This can be useful if you want to ensure that the loading animation is automatically stopped when an error occurs or when your code finishes executing. For example:
```py
from pynimbar import loading_animation
from time import sleep

with loading_animation('Processing data...'):
    sleep(5)
```

## Customization
You can customize the appearance and behavior of the loading animation using the following parameters:
- `text` (str): The text to display during the animation.
- `success_msg` (str, optional): The text to display when the animation is done. Defaults to `'ok'`.
- `animation_frequency` (float, optional): The frequency of the animation. Defaults to `0.1`.
- `break_on_error` (bool, optional): Whether to break on error. Defaults to `False`.
- `verbose_errors` (bool, optional): Whether to print the error traceback. Defaults to `False`.
- `frames` (str, optional): The frames of the animation. Defaults to `'|/-\\'`.

## Contributing
If you have any suggestions or improvements for pynimbar, feel free to submit a pull request or open an issue on the [GitHub repository](https://github.com/gtkacz/pynimbar). We appreciate any feedback or contributions!