from logging_set_up import logger


def call_me(al: str):
    logger.debug("I'm a debug message")
    logger.info(f"I'm info {al}")
    logger.warning("I warn")
    logger.error("I'm an error...psych")
