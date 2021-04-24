from utils.args_parser import args
from utils.create_app import create_app

if args.name == "createapp":
    create_app(args.appname, False)
