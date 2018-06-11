from copier import Copier
from database import Database
from printer import Printer
from keyboard import Keyboard
from scanner import Scanner


class Client(object):

    @staticmethod
    def main():
        copier = Copier()
        keyboard = Keyboard()
        scanner = Scanner()
        printer = Printer()
        database = Database()
        copier.copy(scanner, database)


if __name__ == "__main__":
    Client.main()
