#!/usr/bin/env python
# encoding: utf-8
"""
Starter_Script_With_Args.py

Created by Scott Roberts.
Copyright (c) 2013 TogaFoamParty Studios. All rights reserved.
"""

from optparse import OptionParser

'''
# Setup Logging
import logging
logger = logging.getLogger('default')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# Setup logging to file
fh = logging.FileHandler('default.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
# Setup logging to console
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)
# Setup logging to syslog
import logging.handlers
sh = logging.handlers.SysLogHandler()
sh.setLevel(logging.DEBUG)
logger.addHandler(sh)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
'''

'''
# Setup Text Colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

print bcolors.OKBLUE + "Test Message" + bcolors.ENDC
'''

def foo():
    return "foo function called"

def bar():
    return "bar function called"

def main():
    parser = OptionParser(usage="usage: %prog [options] filepath")
    parser.add_option("-f", "--foo",
                      action="store",
                      type="string",
                      dest="foo_dest",
                      default=None,
                      help="You picked option foo!")
    parser.add_option("-b", "--bar",
                      action="store",
                      type="string",
                      dest="bar_dest",
                      default=None,
                      help="You picked option bar!")

    (options, args) = parser.parse_args()

    #Uncomment to enforce at least one final argument
    #if len(args) != 1:
        #parser.error("You didn't specify a target path.")
        #return False

    if options.foo_dest:
      print foo()
    else:
      print "Foo Dest: Blank"

    if options.bar_dest:
      print bar()
    else:
      print "Bar Dest: Blank"

    return True

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print "User aborted."
    except SystemExit:
        pass
    except:
        crash()
