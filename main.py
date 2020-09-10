#!/usr/bin/python3.7.3 -tt
# Copyright 2020 | raphix.net p.p. Auer Raphael | All Rights Reserved

from lib.butler.butler import butler

def main():
  butler.ask.step(1, "Welchen Tag haben wir heute?")
  butler.ask.step(2, "Möchten Sie fortfahren?", ["ja", "nein"])
  butler.tell.info("my info message.")
  butler.tell.warning("my warning message.")
  butler.tell.error("my error message.")
  butler.tell.success("my success message.")

if __name__ == "__main__":
  main()
