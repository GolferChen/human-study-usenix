
import os
import pandas as pd

html_path = "index.html"
writer = open(html_path, "w")
writer.write("<!DOCTYPE html>" + "\n")
writer.write("<html>" + "\n")
writer.write("<head>" + "\n")
writer.write("    <title>audios</title>" + "\n")
writer.write("</head>" + "\n")
writer.write("<body>" + "\n")


dir_names = ['clean', 'QFA2SR', 'white-box', 'VC']
for dir_name in dir_names:
    for text in os.listdir(dir_name):
        text_dir = os.path.join(dir_name, text)
        for spk_id in os.listdir(text_dir):
            spk_dir = os.path.join(text_dir, spk_id)
            for name in os.listdir(spk_dir):
                url = "{}/{}/{}/{}".format(dir_name, text, spk_id, name)
                item = "    <embed src='" + url + "'/>\n"
                writer.write(item)

dir_names = ['task-1-concentration']
for dir_name in dir_names:
    for spk_id in os.listdir(dir_name):
        spk_dir = os.path.join(dir_name, spk_id)
        for name in os.listdir(spk_dir):
            url = "{}/{}/{}".format(dir_name, spk_id, name)
            item = "    <embed src='" + url + "'/>\n"
            writer.write(item)

writer.write("</body>" + "\n")
writer.write("</html>" + "\n")
writer.close()