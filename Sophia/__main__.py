from Sophia import *
from pyrogram import Client, filters
import os
import logging
from config import ACCESS_CODE, ACCESS_PIN

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

if __name__ == "__main__":
  Sophia.run()
  
