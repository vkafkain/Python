question = input("File name: ")

extension = question.rsplit(".", 1)[-1].lower()

if extension == "gif" or extension == "jpg" or extension == "jpge" or extension == "png":
    print("image/"+extension)
elif extension == "pdf" or extension == "zip":
    print("application/"+extension)
elif extension == "txt":
    print("text/"+extension)
else:
    print("application/octet-stream")