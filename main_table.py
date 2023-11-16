import tabula
import json
import csv

# Read the PDF file
tables = tabula.read_pdf("pdf/HIGH COURT DIRECTORY PDF 2023 (1).pdf", pages='3-177')

def remove_empty_strings(list1):
  return list(filter(lambda x: x != '', list1))

def list_content_dicts_to_csv(list_of_content_dicts, filename):
  with open(filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=list_of_content_dicts[0].keys())
    writer.writeheader()
    for content_dict in list_of_content_dicts:
      writer.writerow(content_dict)

res = []
err = []
for i, table in enumerate(tables):
    d = table.to_dict()
    if d.get("Name") and d.get("Address") and d.get("Mob. & Email"):
        name_list = str.replace(d["Name"][0], "-", ";").split(";")
        address_list = str.replace(d["Address"][0], "--", ";").split(";")
        mobile_list = str.replace(d["Mob. & Email"][0], "-", ";").split(";")

        name_list = remove_empty_strings(name_list)
        address_list = remove_empty_strings(address_list)
        mobile_list = remove_empty_strings(mobile_list)

        # print(name_list)
        # print(address_list)
        # print(mobile_list)

        # print("matched.. index", i)
        for index, name in enumerate(name_list):
            mob = None
            addr = None
            try:
               mob = mobile_list[index]
            except:
               pass
            try:
               addr = address_list[index]
            except:
               pass
            data_dict = {}
            data_dict["name"] = name
            data_dict["address"] = addr
            data_dict["mobile"] = mob
            res.append(data_dict)
    else:
        err.append(d)
        print("## error=", i)
        
# with open("1.json", 'w') as f:
#    json.dump(res, f, indent=4)

list_content_dicts_to_csv(res, "output.csv")

# with open("e.json", 'w') as f:
#    json.dump(err, f, indent=4)
