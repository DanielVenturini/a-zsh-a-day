import json
import argparse
from sys import exit


# get the command line arguments
def arguments():
    description = 'Change the `oh-my-zsh` theme automatically every day using the `anacron`'

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--theme', '-t', action="store_true", help='show the `ZSH_THEME` currently in use')

    return parser.parse_args()


# --theme/-t
def theme(zshday_file):
    zshday_obj = json.load(zshday_file)
    theme_number = zshday_obj['theme_of_day']
    theme_day = zshday_obj['themes'][theme_number]
    print(theme_day)


# verify args
def verify_args(zshrc_file, zshday_file):
    # if a arg was used, don't return
    used_args = False
    args = arguments()

    if args.theme:
        theme(zshday_file)
        used_args = True

    if used_args:
        exit(0)
