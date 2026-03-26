import logging

logging.basicConfig(level=logging.INFO)

class LogBlock:
    def __init__(self, block_name, level):
        self.block_name = block_name
        self.level = level
    
    def __enter__(self):
        if self.level == "INFO":
            logging.info(f"Entering {self.block_name}")
        elif self.level == "WARNING":
            logging.warning(f"Entering {self.block_name}")
        elif self.level == "ERROR":
            logging.error(f"Entering {self.block_name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.level == "INFO":
            logging.info(f"Exiting {self.block_name}")
        elif self.level == "WARNING":
            logging.warning(f"Exiting {self.block_name}")
        elif self.level == "ERROR":
            logging.error(f"Exiting {self.block_name}")


with LogBlock("My block", "INFO"):
    print("Doing something important")