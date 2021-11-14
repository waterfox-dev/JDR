import os



class FilePath:
    """
    Used to get the full path of a static file on any OS
    """

    BASE_DIR = os.sep.join(__file__.split(os.sep)[:-3])

    @staticmethod
    def get(*args):
        """
        :exemple: FilePath.get("assets", "images", "logo.png") will return the full path to logo.png
        (on windows something like c:/Program Files/Evarinya/assets/images/logo.png)
        """
        a = 12
        return FilePath.BASE_DIR + os.sep + os.path.join(*args)