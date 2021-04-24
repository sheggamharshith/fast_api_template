import os
from .loggin_config import setup_logging


logger = setup_logging()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_general_folder_schema():
    """ 
    This function is to generata general app folder schema 
    """

    dir_schema = {
        "folders": ["models", "seralizer", "test"],
        "default_file_in_folder": ["__init__.py"],
        "files_base": ["urls.py", "__init__.py"]
    }

    return dir_schema


def create_app(app: str, root: bool) -> "directory":
    """
    This will create a neccessary app folder for the porjects

    Args:
    ------
    app: Provide the app/folder name
    root: (True) will create a folder named apps if not present
          (False) will not generate  any root folder apps 

    """
    if root:
        os.mkdir(BASE_DIR + "/apps")

    # general checks
    assert os.path.exists(
        BASE_DIR+"/apps"), "error there is no app folder please create it"
    assert not os.path.exists(
        BASE_DIR+f"/apps/{app}"), f"there is already a app/folder registred with name {app}"

    # creating the directory
    try:
        os.mkdir(BASE_DIR+f"/apps/{app}")
        app_base_dir = BASE_DIR+f"/apps/{app}"
        schema = get_general_folder_schema()

        # creating a basic files in the root folder
        for file in schema.get('files_base'):
            os.mknod(app_base_dir+f"/{file}")

        # rest of the folders
        for folder in schema.get("folders"):
            os.makedirs(app_base_dir+f"/{folder}")
            for default_file in schema.get("default_file_in_folder"):
                os.mknod(app_base_dir+f"/{folder}/{default_file}")

        logger.info(f"successfully created app {app} ")

    except Exception as e:
        logger.error(f"{e.args[0]}")
        print(e)


if __name__ == "__main__":
    try:
        create_app("app2", False)
    except Exception as e:
        logging.error(f'{e.args[0]}')
