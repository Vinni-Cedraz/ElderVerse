#!/usr/bin/env python3
from elder_bot import ElderBot
import sys
sys.path.append('/home/myuser/truElderVerse/apps/ms-elder/src/application/usecases')
from short_verse import short_verse


def main():
    chatbot = ElderBot(short_verse)
    chatbot.run()


if __name__ == "__main__":
    main()
