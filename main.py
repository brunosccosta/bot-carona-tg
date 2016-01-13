import sys
import time
import bot

def main():
    TOKEN = sys.argv[1]
    b = bot.Bot(TOKEN)

    print 'Listening ...'
    b.notifyOnMessage(run_forever=True)

if __name__ == '__main__':
    main();
