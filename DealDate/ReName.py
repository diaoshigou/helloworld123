import os


def API():
    for number in range(51,71):
        path = "D:\\File\\"+"100"+str(number)+"\\"
        # new_path = "D:\\picture\\123\\"
        newname = 0
        for file in os.listdir(path):
            # print(file)
            # newname = newname + 1

            # if newname < 10:
            #     os.renames(path + file, path + '0100' + str(number) + '_000' + str(newname) + ".jpg")
            # elif newname >= 10 and newname < 100:
            #     os.renames(path + file, path + '0100' + str(number) + '_00' + str(newname) + ".jpg")
            # elif newname >= 100 and newname < 1000:
            #     os.renames(path + file, path + '0100' + str(number) + '_0' + str(newname) + ".jpg")
            # else:
            #     os.renames(path + file, path + '0100' + str(number) + '_' + str(newname) + ".jpg")

            # print(newname)
            os.renames(path + file, str(newname) + ".jpg")
            newname = newname + 1



def LOT():
    name = 13100005111
    path = r"D:\diku" + "\\"
    for file in os.listdir(path):
        os.renames(path + file, path + str(name) + ".jpg")
        # os.renames(path + file, path + str(name) + "-" + str(name) + ".jpg")
        name += 1

LOT()