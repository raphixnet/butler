#!/usr/bin/python3.7.3 -tt
# Copyright 2020 | raphix.net p.p. Auer Raphael | All Rights Reserved

from ..util.ccolor import CColor
from ..util.ccolorizer import CColorizer

class CAsk:

  def __init__(self):
    pass

  def __formatQuestion(self, question: str, answer: [str]=None):
    if not answer:
      return "{} | ".format(question)
    return "{} [{}] | ".format(question, CColorizer.print("/".join(answer), CColor.FOREGROUNDYELLOW))

  def step(self, stepId: any, question: str, answer: [str]=None):
    if not stepId and not question:
      return
    userAnswer=""
    if not answer:
      userAnswer=input(self.__formatQuestion(question))
      return
    while userAnswer not in answer:
      userAnswer=input(self.__formatQuestion(question, answer))
