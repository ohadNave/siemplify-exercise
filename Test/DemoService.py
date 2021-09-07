from subprocess import call
import pickle
import base64
import sys
import subprocess
import json


class Service(object):

    def __init__(self, path="DemoScript.py"):
        self.path = path

    def run(self, conf_file):
        sub = subprocess.Popen(["py", "{}".format(self.path)], stdin=conf_file, shell=True)
        sub.communicate()[0]

        # sub = subprocess.Popen(["py", "{}".format(self.path)], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        # sub.communicate(input=base64.encodebytes(pickle.dumps(data)))

        # sub.stdin.write(base64.encodebytes(pickle.dumps(data)))
        # sub.stdin.write(base64.encodebytes(pickle.dumps("hello")))
        # sub.stdin.write(base64.encodebytes(pickle.dumps(data)))

        # If you will not write any more to the child.
        # call(["py","{}".format(self.path)], stdin= conf_file , shell=True)


if __name__ == "__main__":
    s = Service()

    conf_file = open('config1.txt')

    s.run(conf_file)
