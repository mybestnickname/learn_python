def main():

    updater = Updater(TELEGRAM_API_KEY)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    updater.start_polling(network_delay=3)
    updater.idle()


if __name__ == '__main__':
    logging.info('Bot started')
    main()