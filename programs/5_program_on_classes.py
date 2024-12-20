"""
Write a class 'LogProcessClass'

Requirement:
L1 = LogProcessClass(r"../log/web_server.log")
ips_list = L1.get_ips()
all_data_in_dictionary = L1.get_all()
L1.write_to_text_file(output_file_path)
"""
print("Write a class 'LogProcessClass'")
print("-"*20)
# --------------


class LogProcessClass:
    def __init__(self, log_file_path):
        # --------------
        # Reading Log File
        # --------------
        my_log_file_handle = open(log_file_path, "rb")
        self.log_file_content = my_log_file_handle.readlines()
        my_log_file_handle.close()
        #################

    def get_ips(self):
        output_list = []
        for each_line in self.log_file_content:
            if each_line.startswith(b"123"):
                sp = each_line.split()
                if len(sp) > 6:
                    # print("sp:",sp)
                    ip = sp[0]
                    ip = ip.decode()
                    output_list.append(ip)
        return output_list

    def get_all(self):
        output_dictionary = {}
        key = 0
        for each_line in self.log_file_content:
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
        return output_dictionary

    def write_to_text_file(self, output_file_path):
        my_out_file_handle = open(output_file_path, "w")
        print("IP", "PICS", sep="\t", file=my_out_file_handle)
        extracted_data_dictionary = self.get_all()
        # extracted_data_dictionary like {0:(ip, img), 1:(ip, img), 2:(ip, img)}
        # extracted_data_dictionary.values = [(ip, img), (ip, img), (ip, img)]
        for i, j in extracted_data_dictionary.values():
            print(i, j, sep="\t", file=my_out_file_handle)
        my_out_file_handle.close()


print("#"*40, end="\n\n")
################################

print("Using class")
print("-"*20)
# --------------

L1 = LogProcessClass(r"../log/web_server.log")
ips_list = L1.get_ips()
print("ips_list:", ips_list, end="\n\n")

all_records = L1.get_all()
print("all_records:", all_records, end="\n\n")

L1.write_to_text_file("class_report.txt")

print("""
Created class_report.txt, Please check
""")

print("#"*40, end="\n\n")
################################
