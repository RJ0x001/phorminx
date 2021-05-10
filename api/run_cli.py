import argparse

from phorminx.run import run as ph_run
from jaskier.server import jaskier_main
from jaskier.functions import run_lyrics_search


def run_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('--username')
    parser.add_argument('--type', choices=('p', 'j'))
    parser.add_argument('--cli', choices=('y', 'n'))
    args = parser.parse_args()
    if args.username and args.type == 'p':
        ph_run(args.username)
    elif args.type == 'j' and args.cli == 'n':
        jaskier_main.app.run()
    elif args.type == 'j' and args.cli == 'y':
        run_lyrics_search()


if __name__ == '__main__':
    # run_cli()
    jaskier_main.app.run(host='0.0.0.0')
