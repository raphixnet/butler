#!/usr/bin/python3.7.3 -tt
# Copyright 2020 | raphix.net p.p. Auer Raphael | All Rights Reserved

from lib.butler.butler import Butler 

def main():
  Butler.ask.step("Welchen Tag haben wir heute?", mandatory=True)  
  Butler.ask.step("Möchten Sie fortfahren?", ["yes", "no"])
  Butler.tell.info("my info message.")
  Butler.tell.warning("my warning message.")
  Butler.tell.error("my error message.")
  Butler.tell.success("my success message.")

if __name__ == "__main__":
  main()
