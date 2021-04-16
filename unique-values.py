import win32clipboard
import pandas as pd
from sys import argv


def main(argv):
    # get clipboard data
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()

    data = data.split()
    print(f"lines - {len(data)}")
    data = set(data)
    print(f"unique_lines - {len(data)}")


    # TODO python 3.9 or 3.10 add match case
    if len(argv) > 1:
        if '--print' in argv[1]:
            for line in data:
                print(line)
        if '--set' in argv[1]:
            # set clipboard data
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText("\n".join(data))
            win32clipboard.CloseClipboard()
        if '''--csv-info''' in argv[1]:
            csv = pd.read_clipboard()
            print(csv.info())
            
            
if __name__ == '__main__':
    main(argv)