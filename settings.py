import logging


def _get_logger(log: bool, handler: str) -> logging.Logger:
    file_log = logging.FileHandler('Logfile.log', encoding='UTF-8')
    console_out = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    settings_logger = logging.getLogger('settings_logger')
    settings_logger.removeHandler(file_log)
    settings_logger.removeHandler(console_out)
    if log:
        settings_logger.setLevel(logging.INFO)
    else:
        settings_logger.setLevel(logging.CRITICAL)
        return settings_logger
    if 'c' in handler:
        console_out.setFormatter(formatter)
        settings_logger.addHandler(console_out)
    if 'f' in handler:
        file_log.setFormatter(formatter)
        settings_logger.addHandler(file_log)
    return settings_logger
