import logging

logging.basicConfig(filename="history.log", level=logging.INFO)

def log_user_request(request, result):
    logging.info(f"Request: {request}, Result: {result}")