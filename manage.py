# from utils.args_parser import args
from utils.create_app import create_app
import uvicorn


# if args.name == "createapp":
#     create_app(args.appname, False)



if __name__=="__main__":
    try:
        uvicorn.run("core.main:app", host="127.0.0.1",
                    port=8000, log_level="info", reload=True)
    except Exception as e:
        print(e)
