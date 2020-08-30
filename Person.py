class Person:  # python object representation of json person
    def __init__(self, _id, name, language, loves_shell, hobbies):
        self.__id__ = _id
        self.__nm__ = name
        self.__language__ = language
        self.__loves_shell__ = loves_shell
        self.__hobbies__ = hobbies

    def __str__(self):
        return "\nID: " + str(self.__id__) + \
               "\nName: " + str(self.__nm__) + \
               "\nFavorite Language: " + str(self.__language__) + \
               "\nLoves Shell: " + str(self.__loves_shell__) + \
               "\nHobbies: " + str(self.__hobbies__) + "\n"
