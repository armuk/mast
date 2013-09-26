#!/usr/bin/env python
# encoding: utf-8
"""
Starter_Script_With_Args.py

Created by Scott Roberts.
Copyright (c) 2013 TogaFoamParty Studios. All rights reserved.
"""

import sys, os, csv

from optparse import OptionParser
from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = os.environ.get('TWILIO_SID')
auth_token  = os.environ.get('TWILIO_TOKEN')
from_number = os.environ.get('TWILIO_NUMBER')

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

#print bcolors.OKBLUE + "Test Message" + bcolors.ENDC


def send_text(msg_text, to_number):
  send_text_debug(msg_text, to_number)

  client = TwilioRestClient(account_sid, auth_token)
  message = client.messages.create(body=msg_text, to=to_number, from_=from_number)
  print message.sid

def send_text_debug(msg_text, to_number):
    print bcolors.OKBLUE + "   Sending: " + bcolors.ENDC + msg_text + bcolors.OKBLUE + "   To: " + bcolors.ENDC + to_number + bcolors.OKBLUE +  "   From: " + bcolors.ENDC + from_number

def main():
  message_text = sys.argv[1]
  numbers_csv = sys.argv[2]

  msg_text = open(message_text, 'rb').read()

  with open(numbers_csv, 'rb') as f:
    reader = csv.reader(f)

    for row in reader:
      print bcolors.OKGREEN + "Sending to: " + bcolors.ENDC + row[0]
      send_text(msg_text, row[1])

if __name__ == "__main__":
  try:
      main()
  except KeyboardInterrupt:
      print "User aborted."
  except SystemExit:
      pass
  # except:
  #     crash()
