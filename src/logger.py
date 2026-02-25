import os
from datetime import datetime
import logging

logFile = os.path.join(os.getcwd(),'logs',datetime.now().strftime('%d_%m_%Y'),f"log_{datetime.now().strftime('%H_%M_%S')}.log")

LOG_PATH = os.path.join(os.getcwd(),'logs',datetime.now().strftime('%d_%m_%Y'))
os.makedirs(LOG_PATH,exist_ok=True)

logging.basicConfig(

    filename=logFile,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
