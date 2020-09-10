#!/usr/bin/python3.7.3 -tt
# Copyright 2020 | raphix.net p.p. Auer Raphael | All Rights Reserved

#butler.tell.info("my info message.")
#butler.tell.warning("my warning message.")
#butler.tell.error("my error message.")
#butler.tell.success("my success message.")

from ..util.ccolor import CColor
from ..util.ccolorizer import CColorizer
from .itell import ITell
from datetime import datetime

class CTell(ITell):
  def __init__(self):
    pass

  def __timestamp(self):
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

  def __smily(self, smilyId):
    if smilyId is "INFO":
      return "\U0001F64B"
    if smilyId is "WARNING":
      return "\U0001F633"
    if smilyId is "ERROR":
      return "\U0001F648"
    if smilyId is "SUCCESS":
      return "\U0001F603"

  def __printStatus(self, statusId: str):
    if statusId.strip() == "INFO":
      return CColorizer.print("[INFO]", CColor.BACKGROUNDBLUE, CColor.FOREGROUNDBLACK)
    if statusId.strip() == "WARNING":
      return CColorizer.print("[WARNING]", CColor.BACKGROUNDYELLOW, CColor.FOREGROUNDBLACK)
    if statusId.strip() == "ERROR":
      return CColorizer.print("[ERROR]", CColor.BACKGROUNDRED, CColor.FOREGROUNDBLACK)
    if statusId.strip() == "SUCCESS":
      return CColorizer.print("[SUCCESS]", CColor.BACKGROUNDGREEN, CColor.FOREGROUNDBLACK)

  def info(self, msg: str):
    print("{} {} [{}] {}".format(self.__printStatus("INFO"), self.__smily("INFO"), self.__timestamp(), msg.strip()))

  def warning(self, msg: str):
    print("{} {} [{}] {}".format(self.__printStatus("WARNING"), self.__smily("WARNING"), self.__timestamp(), msg.strip()))

  def error(self, msg: str):
    print("{} {} [{}] {}".format(self.__printStatus("ERROR"), self.__smily("ERROR"), self.__timestamp(), msg.strip()))

  def success(self, msg: str):
    print("{} {} [{}] {}".format(self.__printStatus("SUCCESS"), self.__smily("SUCCESS"), self.__timestamp(), msg.strip()))

