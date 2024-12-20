"""
Write function which takes log file path as an argument
extract info then return extracted info in dictionary.
Like
extracted_info = {0:(ip, img), 1:(ip, img), 2:(ip, img)}
"""

print("Log Process Function:")
print("-"*20)
# --------------


def log_process_function(log_file_path):
    """
    Function which reads log file, extract ip, pics
    then it will return extracted info in dictionary
    :param log_file_path:
    :return output_dictionary:
    """
    # --------------
    # Reading Log File
    # --------------
    my_log_file_handle = open(log_file_path, "rb")
    log_file_content = my_log_file_handle.readlines()
    my_log_file_handle.close()
    #################

    # --------------
    # Extracting Info and Returning In Dictionary
    # --------------
    # extracted_info = {0:(ip, img), 1:(ip, img), 2:(ip, img)}
    output_dictionary = {}
    key = 0
    for each_line in log_file_content:
        if each_line.startswith(b"123"):
            sp = each_line.split()
            if len(sp) > 6:
                # print("sp:",sp)
                ip = sp[0]
                ip = ip.decode()

                raw_img = sp[6]  # b'/pics/wpaper.gif'
                if raw_img.startswith(b"/pics/"):
                    img = raw_img[6:]
                    img = img.decode()
                else:
                    img = "No Image"
                each_line_tuple = (ip, img)
                output_dictionary[key] = each_line_tuple
                key += 1
    #################

    # --------------
    # Return extracted Info
    # --------------
    return output_dictionary
    #################

print("#"*40, end="\n\n")
################################

print("Calling function")
print("-"*20)
# --------------

extracted_data = log_process_function(log_file_path=r"../log/web_server.log")
print("extracted_data:", extracted_data, end="\n\n")

print("#"*40, end="\n\n")
################################
