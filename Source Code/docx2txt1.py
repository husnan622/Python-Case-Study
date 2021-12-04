import glob
import docx2txt

example = []
for file in glob.glob("D:\Program\*.docx"):

    my_text = docx2txt.process(file)
    example.append(my_text)

print(example)
