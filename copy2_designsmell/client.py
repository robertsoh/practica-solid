from copier import Copier


class Client(object):

    @staticmethod
    def main():
        copier = Copier()
        copier.copy()


if __name__ == "__main__":
    Client.main()
