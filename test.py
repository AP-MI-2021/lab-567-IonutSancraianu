import os

file = open(r"C:\Users\Chuckie\PycharmProjects\lab-567-IonutSancraianu\Domain\cufarul cu comori", "r+")
if os.stat(r"C:\Users\Chuckie\PycharmProjects\lab-567-IonutSancraianu\Domain\cufarul cu comori").st_size == 0:
    print("e gol")
else:
    print(os.stat(r"C:\Users\Chuckie\PycharmProjects\lab-567-IonutSancraianu\Domain\cufarul cu comori").st_size)