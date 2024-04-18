import logging
import os

log_directory = "reports"
log_file = "test.log"

if not os.path.exists(log_directory):
    os.makedirs(log_directory)
    logging.info(f"Directory '{log_directory}' was created.")
else:
    logging.info(f"Directory '{log_directory}' already exists.")


# Create a custom logger
logger = logging.getLogger('TestLogger')
logger.setLevel(logging.INFO)

# Create handlers
log_path = os.path.join(log_directory, log_file)
f_handler = logging.FileHandler(log_path)
f_handler.setLevel(logging.INFO)

# Create formatters and add it to handlers
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(f_handler)

