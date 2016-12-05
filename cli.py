"""
Description: Module show simple implementation of command line interface
"""

__author__ = "pratik khandge"
__copyright__ = ""
__credits__ = ["pratik khandge"]
__license__ = ""
__version__ = "0.1"
__maintainer__ = "pratik"
__email__ = "pratik.khandge@gmail.com"
__status__ = "Developement"

# python imports
import cmd
import sys


class Service(cmd.Cmd):
    """
    Description: Simple command processor example.
    """
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = 'cmd> '
        self.services = ['mongodb', 'tinydb']

    def preloop(self):
        """Initialization before prompting user for commands.
           Despite the claims in the Cmd documentation, Cmd.preloop() is not a stub.
        """
        cmd.Cmd.preloop(self)   # sets up command completion
        self._hist    = []      # No history yet

    def postloop(self):
        """Take care of any unfinished business.
           Despite the claims in the Cmd documentaion, Cmd.postloop() is not a stub.
        """
        cmd.Cmd.postloop(self)   ## Clean up command completion
        print "Exiting..."

    def do_start(self, line):
        """
        Description: service started
        """
        if line in self.services:
            print "service started..."
        else:
            print "unknow service {}".format(line)
        self._hist.append("start")

    def do_stop(self, line):
        """
        Description: service stopped
        """
        if line in self.services:
            print "service stopped..."
        else:
            print "unknow service"
        self._hist.append("start")

    def do_quit(self, line):
        """
        Description: command line exit
        """
        sys.exit(1)

    def do_hist(self, args):
        """
        Description: Print a list of commands that have been entered
        """
        for record in self._hist:
            print record

    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    Service().cmdloop()