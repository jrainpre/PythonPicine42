import sys


def print_progress_bar(iteration, total):
    """prints formated progress bar
    terminal with is hardcoded to 147 characters"""
    percent = "{0:.0f}".format(100 * (iteration / float(total)))
    filled_length = int(147 * iteration // total)
    prog_bar = '█' * filled_length + '-' * (147 - filled_length)
    sys.stdout.write(f'\r{percent}%|{prog_bar}| {iteration}/{total}')


def ft_tqdm(lst: range):
    """
    Mimics a progress bar behavior, iterating over an iterable.
    """
    total = len(lst)
    print_progress_bar(0, total)
    for i, item in enumerate(lst, 1):
        print_progress_bar(i, total)
        yield item
    print()
