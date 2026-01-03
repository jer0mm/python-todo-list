import logging

def get_logger():
    logging.basicConfig(
        filename='test.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging
