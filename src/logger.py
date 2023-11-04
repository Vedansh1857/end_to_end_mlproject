import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_PATH = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(LOG_PATH,exist_ok=True)
LOG_FILE_PATH = os.path.join(LOG_PATH,LOG_FILE)

# The getcwd() will return the current working directory i.e. "D:\end_to_end_mlproject" & os.makedirs will make a folder named "logs" in that directory only, consisting of log files named with a naming convention as mentioned in the "LOG_FILE" variable.

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
