
from something_to_call import call_me
from logging_set_up import logger, exception_traceback_to_string

if __name__ == "__main__":

    logger.debug('This message should go to the debug log file only')
    logger.info('So should this')
    call_me(al='Al')
    logger.warning('And this, too')
    logger.error('And non-ASCII stuff, too, like Øresund and Malmö')
    some_list = [1, 2]
    try:
        some_thing = some_list[3]
    except Exception as e:
        # logger.critical(str(e))
        # logger.critical(e.__repr__())
        logger.critical(exception_traceback_to_string(e))
        raise e
    logger.info("There should've been an exception thrown already!")
