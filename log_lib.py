import logging
import os

log_directory = "reports"
log_file = "test.log"

if not os.path.exists(log_directory):
    os.makedirs(log_directory)
    print(f"Directory '{log_directory}' was created.")
else:
    print(f"Directory '{log_directory}' already exists.")


# Create a custom logger
logger = logging.getLogger('TestLogger')
logger.setLevel(logging.DEBUG)

# Create handlers
log_path = os.path.join(log_directory, log_file)
f_handler = logging.FileHandler(log_path)
f_handler.setLevel(logging.DEBUG)

# Create formatters and add it to handlers
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(f_handler)

