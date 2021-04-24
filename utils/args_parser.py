import argparse

parser = argparse.ArgumentParser(
    description='Command line interface for the fastapi template generation')
parser.add_argument('name', action='store')
parser.add_argument('appname', action='store')

args = parser.parse_args()
