lines = open("FileIO_input.txt").readlines()
with  open("FileIO_output.txt", "w") as ofile:
    ofile.writelines(reversed(lines))

