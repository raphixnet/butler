#!/usr/bin/python3.7.3 -tt
# Copyright 2020 | raphix.net p.p. Auer Raphael | All Rights Reserved

from .ccolor import CColor

class CColorizer():
  def __init__(self):
    pass

  @staticmethod
  def print(string: str, backgroundColor: str='', foregroundColor: str=''):
    if not backgroundColor and not foregroundColor:
      return "{}".format(string)
    if backgroundColor and not foregroundColor:
      return "{}{}{}".format(backgroundColor, string, CColor.RESET)
    if foregroundColor and not backgroundColor:
      return "{}{}{}".format(foregroundColor, string, CColor.RESET)
    return "{}{}{}{}".format(backgroundColor, foregroundColor, string, CColor.RESET)