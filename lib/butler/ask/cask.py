#!/usr/bin/python3.7.3 -tt
# Copyright 2020 | raphix.net p.p. Auer Raphael | All Rights Reserved

from ..util.ccolor import CColor
from ..util.ccolorizer import CColorizer
from ..util.constants import BUTLERCONSTANT
import uuid

class CAsk:

  __stepid=None

  def __init__(self):
    self.__stepid=uuid.uuid1().hex

  def __formatQuestion(self, question: str, answer: [str]=None, mandatory: bool=False):
    if answer:
      return "{} {} [{}] | ".format(CColorizer.print(BUTLERCONSTANT.STRINGS.MANDATORY, CColor.FOREGROUNDRED), question, CColorizer.print("/".join(answer), CColor.FOREGROUNDYELLOW))
    if mandatory:
      return "{} {} | ".format(CColorizer.print(BUTLERCONSTANT.STRINGS.MANDATORY, CColor.FOREGROUNDRED), question)
    return "{} {} {} | ".format(CColorizer.print(BUTLERCONSTANT.STRINGS.OPTIONAL, CColor.FOREGROUNDBLUE), question, BUTLERCONSTANT.STRINGS.SKIPWITHENTER)

  def step(self, question: str, answer: [str]=None, mandatory: bool=False):
    if not question:
      return
    userAnswer=""
    if answer: #questions with answers are always mandatory
      while userAnswer not in answer:
        userAnswer=input(self.__formatQuestion(question, answer, mandatory))
      return userAnswer.strip()
    while mandatory:
      userAnswer=input(self.__formatQuestion(question, answer, mandatory))
      if userAnswer.strip():
        mandatory=False
        return userAnswer.strip()
    return input(self.__formatQuestion(question, answer, mandatory)).strip()
