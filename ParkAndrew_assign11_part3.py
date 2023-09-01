"""
Assignment #11, Part 3
Andrew Park
"""

class Smartphone:
    def __init__(self, capacity, name):
        self.__name = name
        self.__capacity = capacity
        self.__apps = {}

    def add_app(self, appname, appsize):
        if self.get_available_space() >= appsize and not self.has_app(appname):
            self.__apps[appname] = appsize
        elif self.get_available_space() < appsize:
            print("Cannot install app, no available space")
        else:
            print("App already instaled!")

    def remove_app(self, appname):
        if self.has_app(appname):
            print("App removed: {}".format(appname))
            del self.__apps[appname]
        else:
            print("App not installed!")

    def has_app(self, appname):
        return appname in self.__apps.keys()

    def get_available_space(self):
        return self.__capacity - sum(list(self.__apps.values()))

    def report(self):
        print("Name: {}".format(self.__name))
        print("Capacity: {0} out of {1} GB".format(
            sum(list(self.__apps.values())), self.__capacity))
        print("Available space: {} GB".format(self.get_available_space()))
        print("Apps installed: {}".format(len(self.__apps.keys())))
        A = self.__apps.keys()
        A = list(A)
        A.sort()
        for i in A:
            print("* {0} is using {1} GB".format(i, self.__apps[i]))


def main():
    while True:
        size = input("Size of your new smartphone (32, 64 or 128 GB): ")
        if size not in ['32', '64', '128']:
            continue
        else:
            size = int(size)
            break
    name = input("Smartphone name: ")
    smartphone = Smartphone(size, name)
    print("Smartphone created")
    while True:
        print()
        choice = input("(r)eport, (a)dd, r(e)move or (q)uit: ")
        choice = choice.lower()
        if choice == 'r':
            smartphone.report()
        elif choice == 'a':
            appname = input("App name to add: ")
            while True:
                try:
                    appsize = int(input("App size in GB: "))
                    break
                except:
                    print("Invalid size!")
            smartphone.add_app(appname, appsize)
        elif choice == 'e':
            appname = input("App name to remove: ")
            smartphone.remove_app(appname)
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


main()
