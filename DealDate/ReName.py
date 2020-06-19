import os


def API():
    for number in range(51,71):
        path = "D:\\File\\"+"100"+str(number)+"\\"
        # new_path = "D:\\picture\\123\\"
        newname = 0
        for file in os.listdir(path):
            # print(file)
            newname = newname + 1
            if newname < 10:
                os.renames(path + file, path + '0100' + str(number) + '_000' + str(newname) + ".jpg")
            elif newname >= 10 and newname < 100:
                os.renames(path + file, path + '0100' + str(number) + '_00' + str(newname) + ".jpg")
            elif newname >= 100 and newname < 1000:
                os.renames(path + file, path + '0100' + str(number) + '_0' + str(newname) + ".jpg")
            else:
                os.renames(path + file, path + '0100' + str(number) + '_' + str(newname) + ".jpg")

            # print(newname)



def LOT():
    name = 13100000000
    path = r"D:\picture\diku\diku" + "\\"
    for file in os.listdir(path):
        os.renames(path + file, path + str(name) + "-" + str(name) + ".jpg")
        name += 1

LOT()