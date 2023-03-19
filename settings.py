import json
import logging
import sys


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


def _cls_mode_run(logger: logging.Logger, cls_mode: bool) -> bool:
    if cls_mode:
        logger.info('Shutting down the app!')
        sys.exit()
    return False


def _load_json(
    file_name: str,
    logger: logging.Logger,
    cls_mode: bool,
    encoding: str
) -> dict | None:
    logger.info('Downloading the settings file {}!'.format(file_name))
    try:
        with open(file=file_name, mode='r', encoding=encoding) as file:
            try:
                result = json.load(file)
                logger.info('File {} loaded - OK!'.format(file_name))
            except json.JSONDecodeError as error:
                logger.error('Incorrect settings file!')
                logger.error(error)
                if not _cls_mode_run(logger=logger, cls_mode=cls_mode):
                    return None
    except (FileNotFoundError, LookupError) as error:
        logger.error('Error opening the {} settings file!'.format(file_name))
        logger.error(error)
        if not _cls_mode_run(logger=logger, cls_mode=cls_mode):
            return None
    return result
