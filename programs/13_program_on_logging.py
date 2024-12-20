"""
logging library: to capture log
"""
print("Configure logger")
print("-"*20)
# --------------

import logging
my_logger = logging.getLogger(__name__)
logging.basicConfig(filename="my_13_program_log.log",
                    filemode="w",
                    level=logging.DEBUG,
                    format="%(levelname)s : %(asctime)s : %(filename)s : %(message)s"
                    )

print("#"*40, end="\n\n")
################################


print("Testing my_logger")
print("-"*20)
# --------------

my_logger.info("This is INFO")
my_logger.debug("This is DEBUG")
my_logger.warning("This is WARNING")
my_logger.critical("This is CRITICAL")
my_logger.error("This is ERROR")

print("""
Created below log file, 

my_13_program_log.log

please check
""")

print("#"*40, end="\n\n")
################################


print("Using my_logger")
print("-"*20)
# --------------

try:
    my_logger.info("Reached try block")
    my_logger.info("Opening file for reading")
    my_file_handle = open("xyzabc.txt", "r")
    my_logger.info("File open success")
except Exception as e:
    my_logger.info("Reached except block")
    my_logger.error(f"File reading failed, Error message is:{e}")
    my_logger.info("Stopping program execution")
    exit()
else:
    my_logger.info("Reached 'else' block")
    my_logger.info("Reading file content")
    file_content = my_file_handle.read()
    my_logger.info("File read completed")
finally:
    my_logger.info("Reached finally block")
    my_logger.info("Closing file  handle")
    try:
        my_file_handle.close()
        my_logger.info("Closing file handle success")
    except Exception as e:
        my_logger.error(f"Closing file handle failed. Error message is: {e}")
    print("""
    Created below log file, 

    my_13_program_log.log

    please check
    """)


print("#"*40, end="\n\n")
################################
