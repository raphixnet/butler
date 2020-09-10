#!/usr/bin/python3.7.3 -tt
# Copyright 2020 | raphix.net p.p. Auer Raphael | All Rights Reserved

class CColor:
  #background
  BACKGROUNDBLUE = '\u001b[44m'
  BACKGROUNDYELLOW = '\u001b[43m'
  BACKGROUNDRED = '\u001b[41m'
  BACKGROUNDGREEN = '\u001b[42m'
  BACKGROUNDBLACK = '\u001b[40m'
  #foreground
  FOREGROUNDBLACK = '\u001b[30m'
  FOREGROUNDWHITE = '\u001b[37m'
  FOREGROUNDBLUE = '\u001b[34m'
  FOREGROUNDYELLOW = '\u001b[93m'
  FOREGROUNDRED = '\u001b[31m'
  FOREGROUNDGREEN = '\u001b[32m'
  #special
  BOLD = '\u001b[1m'
  STOP_BOLD = '\u001b[21m'
  UNDERLINE = '\u001b[4m'
  STOP_UNDERLINE = '\u001b[24m'
  BLINK = '\u001b[5m'
  #reset
  RESET = '\u001b[0m'