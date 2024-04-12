import logging
import logging.handlers

def setup_logging(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        file_handler_yn=True,
        stream_handler_yn=True,
        timed_rotating_when='W6',
        timed_rotating_interval=1,
        timed_rotating_backup_count=10,
        log_file='app.log', 
        log_level=logging.INFO):

    # 루트 로거 설정
    logger = logging.getLogger()
    logger.setLevel(log_level)

    formatter = logging.Formatter(format)

    if file_handler_yn:
        file_handler = logging.handlers.TimedRotatingFileHandler(
            log_file, 
            when=timed_rotating_when, 
            interval=timed_rotating_interval,
            backupCount=timed_rotating_backup_count
            )
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    if stream_handler_yn:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(log_level)
        stream_handler.setFormatter(formatter)

        logger.addHandler(stream_handler)


def init():

    from core.config import Config
    config = Config().get_config()

    log_params = {
        'format': config['logging']['format'], 
        'file_handler_yn': config['logging']['file_handler_yn'], 
        'stream_handler_yn': config['logging']['stream_handler_yn'], 
        'timed_rotating_when': config['logging']['timed_rotating_when'], 
        'timed_rotating_interval': config['logging']['timed_rotating_interval'], 
        'timed_rotating_backup_count': config['logging']['timed_rotating_backup_count'], 
        'log_file': config['logging']['log_file'], 
        'log_level': eval(config['logging']['log_level']), 
    }

    setup_logging(**log_params)