from copier import Copier
from keyboard import Keyboard
from scanner import Scanner


class Client(object):

    @staticmethod
    def main():
        copier = Copier()
        keyboard = Keyboard()
        # scanner = Scanner()
        copier.copy(keyboard)


if __name__ == "__main__":
    Client.main()
