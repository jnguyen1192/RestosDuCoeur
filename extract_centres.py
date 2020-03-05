import os

# use dir /b /a-d to get list of centres
DIR_NAME = "data"


def extract_centres(file_name="centres.txt"):
    """
    Extract the centres from the file containing a list of centre using dir from windows cmd
    :param: filename :
    :return: list of centres
    """
    # open file
    file = open(os.path.join(DIR_NAME, file_name), "r")

    lines = file.readlines()
    file.close()

    centres = []
    for line in lines:
        if len(line.split(".doc")) > 1 and "~" not in line:
            centres.append(line.split(".doc")[0])

    print(len(centres), centres)


def main():
    print(extract_centres())


if __name__ == "__main__":
    main()
