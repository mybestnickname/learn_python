def main():

    updater = Updater(config.token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text, handleMessage))
  
    # log all errors
    dp.add_error_handler(error)

    updater.start_polling(network_delay=3)

    updater.idle()


if __name__ == '__main__':
    logging.info('Bot started')
    main()