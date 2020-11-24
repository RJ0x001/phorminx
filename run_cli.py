import argparse

from phorminx.run import run as ph_run
from jaskier.functions import run_lyrics_search


def run_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('--username')
    parser.add_argument('--type', choices=('p', 'j'))
    args = parser.parse_args()
    if args.username and args.type == 'p':
        ph_run(args.username)
    elif args.type == 'j':
        run_lyrics_search()

if __name__ == '__main__':
    run_cli()
