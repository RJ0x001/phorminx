import argparse

from phorminx.run import run as ph_run
from jaskier.server import jaskier_main
from jaskier.fa_server import main
from jaskier.functions import run_lyrics_search

import utils.config as config


def run_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('--username')
    parser.add_argument('--type', choices=('p', 'j'))
    parser.add_argument('--cli', choices=('y', 'n'))
    parser.add_argument('--server', choices=('flask', 'fastapi'))
    args = parser.parse_args()
    if args.username and args.type == 'p':
        ph_run(args.username)
    elif args.type == 'j' and args.cli == 'n' and args.server == 'flask':
        jaskier_main.app.run(host='0.0.0.0')
    elif args.type == 'j' and args.cli == 'y':
        run_lyrics_search()
    elif args.type == 'j' and args.cli == 'n' and args.server == 'fastapi':
        main.uvicorn.run(main.app, host=config.host, port=config.port)


if __name__ == '__main__':
    run_cli()
