#!/usr/bin/python3.7.3 -tt
# Copyright 2020 | raphix.net p.p. Auer Raphael | All Rights Reserved

from .ask.cask import CAsk
from .cecho import CEcho
from .tell.ctell import CTell
from .cclean import CClean

class Butler(object):

  def __init__(self):
    pass

  @property
  def ask(self):
    return CAsk()

  @property
  def echo(self):
    return CEcho()

  @property
  def tell(self):
    return CTell()

  @property
  def clean(self):
    return CClean()

Butler=Butler()