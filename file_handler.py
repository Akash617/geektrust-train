import controller


class File_handler:
    def __init__(self):
        self.__controller = controller.Controller()
        pass

    def read_file(self, file):
        self.__lines = file.readlines()
        self.handle(self.__lines)


    def handle(self, lines):
        # Iterate over lines in the file
        for self.__line in lines:
            # Format lines, remove the newline and split into a list
            self.__line = self.__line.replace("\n", "").split(" ")

            if self.__line[0] == "TRAIN_A":
                self.__controller.add_bogies(self.__line[2:])

            if self.__line[0] == "TRAIN_B":
                self.__controller.add_bogies(self.__line[2:])
