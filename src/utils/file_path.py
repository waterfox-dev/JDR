import os

class FilePath:
    """
    Utilisé pour obtenir le chemin complet d'un fichier statique sur n'importe quel système d'exploitation
    """

    BASE_DIR = os.sep.join(__file__.split(os.sep)[:-3])

    @staticmethod
    def get(*args):
        """
        Exemple :  FilePath.get("assets", "images", "book.png") cela va retourner la fichier complet de book.png
        (sur windows se serait C:/Users/leopo/Documents/Programmation/JDR/JDR/assets/images/book.png)
        """
        a = 12
        return FilePath.BASE_DIR + os.sep + os.path.join(*args)