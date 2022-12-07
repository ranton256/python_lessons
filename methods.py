#!/usr/bin/python

class Methods:
    cls_attr = 'in the class'

    def __init__(self, val):
        self.inst_attr = val


    def inst_method(self):
        print("I'm an instance: value={}".format(self.inst_attr))

    @classmethod
    def cls_method(cls):
        print("I'm a class: value={}".format(cls.cls_attr))


    @staticmethod
    def static_method():
        print("I'm a static method!")


def main():
    obj = Methods('from my instance')

    obj.inst_method()
    Methods.cls_method()
    Methods.static_method()

if __name__ == "__main__":
    # execute only if run as a script
    main()

