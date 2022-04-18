import logging


def setup_logger(log_name, level=logging.DEBUG):
    """path: app_spider/logs/{}.log"""
    log_handle = logging.getLogger(log_name)
    if not log_handle.handlers:
        formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
        fileHandler = logging.FileHandler("./logs/{}.log".format(log_name), mode='a')
        fileHandler.setFormatter(formatter)
        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(formatter)

        log_handle.setLevel(level)
        log_handle.addHandler(fileHandler)
        log_handle.addHandler(streamHandler)


appname = "zhihuSpider"
setup_logger(appname)
log_writer = logging.getLogger(appname)
