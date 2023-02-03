import bot
import log_generate as lg
import time


def main():
    lg.write_data('{} {}'.format('Старт работы бота:', time.strftime('%d.%m.%y %H:%M')))
    bot.start_bot()


if __name__ == '__main__':
    main()