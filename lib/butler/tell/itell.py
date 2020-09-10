#!/usr/bin/python3.7.3 -tt
# Copyright 2020 | raphix.net p.p. Auer Raphael | All Rights Reserved

import abc

class ITell(metaclass=abc.ABCMeta):

  @abc.abstractmethod
  def info(self, msg: str): pass

  @abc.abstractmethod
  def warning(self, msg: str): pass

  @abc.abstractmethod
  def error(self, msg: str): pass

  @abc.abstractmethod
  def success(self, msg: str): pass