from tkinter import *
import tkinter.font as font
from tkinter import messagebox


def hebbian(entry):
    learning_entry = []
    weight = []
    learned_ratio = (open("./predict.txt", "r+")).read()

    if len(learned_ratio) == 0:
        first_entry = [0] * 26  # In Java by using for-loop
        read_dataset = (open("./dataset.txt")).readlines()  # Inorder ro iterate lines

        for a in read_dataset:
            temp = [int(z) for z in a.split(',')[:-1]]
            if a.split(',')[-1] == "1\n":
                temp.append(1)
            else:
                temp.append(-1)
            learning_entry.append(temp)

        numerator = 0
        for test in learning_entry:
            for d in range(len(test) - 1):
                first_entry[d] += test[d] * test[-1]  # w(new) = x * y + w(old)
                numerator = numerator + 1
            weight.append(first_entry)

        list_entry = list()
        for test_weight, test in zip(weight, learning_entry):
            integral, numerator1 = 0, 0
            for z, f in zip(test_weight[:-1], test[:-1]):
                integral = integral + (z * f)
                numerator1 = numerator1 + 1

            if (integral >= 0 and test[-1] == 1 and numerator1 == len(test) - 1) or (
                    integral < 0 and test[-1] == -1 and numerator1 == len(
                    test) - 1) and test_weight != list_entry:
                list_entry = test_weight
                (open("./predict.txt", "a+")).write(",".join(str(s1) for s1 in test_weight))

    else:
        total = 0
        for i1, j1 in zip(learned_ratio.split(',')[:-1], entry):
            total += int(i1) * int(j1)

        if total >= 0:
            print("Well, the shape is  X")
        elif total < 0:
            print("Well, the shape is  O")
        else:
            print("Sorry", "Try again")


def output_data():  # Gotten data by GUI
    entry_array = [e.get() for e in my_arr]
    array_list = []
    for t in entry_array:
        if t == 0:
            array_list.append(-1)
        else:
            array_list.append(t)
    if str_var.get() == "":
        hebbian(entry_array)  # call first function

    # Gotten the label
    elif str_var.get().upper() == "X": 
        array_list.append(1)
        open("./dataset.txt", "a+").write(",".join(str(q) for q in array_list) + "\n")
        messagebox.showwarning("Well", "Your data saved.")  # print

    elif str_var.get().upper() == "O":
        array_list.append(-1)
        open("./dataset.txt", "a+").write(",".join(str(r) for r in array_list) + "\n")
        messagebox.showwarning("Well", "Your data saved.")  # print

    else:
        messagebox.showwarning("Fail", "Invalid letter")  # print


gui = Tk()
gui.configure(background="blue3")
gui.geometry("375x375")
gui.title("hebb learning algorithm")
str_var = StringVar()

my_arr = [IntVar(), IntVar(), IntVar(), IntVar(), IntVar(),
          IntVar(), IntVar(), IntVar(), IntVar(), IntVar(),
          IntVar(), IntVar(), IntVar(), IntVar(), IntVar(),
          IntVar(), IntVar(), IntVar(), IntVar(), IntVar(),
          IntVar(), IntVar(), IntVar(), IntVar(), IntVar()]

Checkbutton(gui, text="", variable=my_arr[0], height=2, width=2, background="blue3").grid(row=1, column=0)
Checkbutton(gui, text="", variable=my_arr[1], height=2, width=2, background="blue3").grid(row=1, column=1)
Checkbutton(gui, text="", variable=my_arr[2], height=2, width=2, background="blue3").grid(row=1, column=2)
Checkbutton(gui, text="", variable=my_arr[3], height=2, width=2, background="blue3").grid(row=1, column=3)
Checkbutton(gui, text="", variable=my_arr[4], height=2, width=2, background="blue3").grid(row=1, column=4)
Checkbutton(gui, text="", variable=my_arr[5], height=2, width=2, background="blue3").grid(row=2, column=0)
Checkbutton(gui, text="", variable=my_arr[6], height=2, width=2, background="blue3").grid(row=2, column=1)
Checkbutton(gui, text="", variable=my_arr[7], height=2, width=2, background="blue3").grid(row=2, column=2)
Checkbutton(gui, text="", variable=my_arr[8], height=2, width=2, background="blue3").grid(row=2, column=3)
Checkbutton(gui, text="", variable=my_arr[9], height=2, width=2, background="blue3").grid(row=2, column=4)
Checkbutton(gui, text="", variable=my_arr[10], height=2, width=2, background="blue3").grid(row=3, column=0)
Checkbutton(gui, text="", variable=my_arr[11], height=2, width=2, background="blue3").grid(row=3, column=1)
Checkbutton(gui, text="", variable=my_arr[12], height=2, width=2, background="blue3").grid(row=3, column=2)
Checkbutton(gui, text="", variable=my_arr[13], height=2, width=2, background="blue3").grid(row=3, column=3)
Checkbutton(gui, text="", variable=my_arr[14], height=2, width=2, background="blue3").grid(row=3, column=4)
Checkbutton(gui, text="", variable=my_arr[15], height=2, width=2, background="blue3").grid(row=4, column=0)
Checkbutton(gui, text="", variable=my_arr[16], height=2, width=2, background="blue3").grid(row=4, column=1)
Checkbutton(gui, text="", variable=my_arr[17], height=2, width=2, background="blue3").grid(row=4, column=2)
Checkbutton(gui, text="", variable=my_arr[18], height=2, width=2, background="blue3").grid(row=4, column=3)
Checkbutton(gui, text="", variable=my_arr[19], height=2, width=2, background="blue3").grid(row=4, column=4)
Checkbutton(gui, text="", variable=my_arr[20], height=2, width=2, background="blue3").grid(row=5, column=0)
Checkbutton(gui, text="", variable=my_arr[21], height=2, width=2, background="blue3").grid(row=5, column=1)
Checkbutton(gui, text="", variable=my_arr[22], height=2, width=2, background="blue3").grid(row=5, column=2)
Checkbutton(gui, text="", variable=my_arr[23], height=2, width=2, background="blue3").grid(row=5, column=3)
Checkbutton(gui, text="", variable=my_arr[24], height=2, width=2, background="blue3").grid(row=5, column=4)

# Inorder to make GUI responsive
n_rows = 5
n_columns = 5
for i in range(n_rows):
    for j in range(n_columns):
        gui.grid_rowconfigure(i, weight=1)
        gui.grid_columnconfigure(j, weight=1)

my_font = font.Font(size=14, family='Arial')
my_font1 = font.Font(size=11, family='Arial')
my_font2 = font.Font(size=11, family='Arial')
label1 = Label(gui, text="select your pattern", foreground="white", background="blue3")
label1.grid(row=0, column=0, columnspan=5)
label1.grid_rowconfigure(0, weight=1)
label1.grid_columnconfigure(1, weight=1)
label1['font'] = my_font

label2 = Label(gui, text="choose", foreground="white", background="blue3")
label2.grid(row=6, column=0, columnspan=5)
label2.grid_rowconfigure(6, weight=1)
label2.grid_columnconfigure(0, weight=1)
label2['font'] = my_font1

entry1 = Entry(gui, text="", textvariable=str_var, width=8, background="light cyan")
entry1.grid(row=6, column=2, columnspan=5)
entry1.grid_rowconfigure(6, weight=1)
entry1.grid_columnconfigure(3, weight=1)

button1 = Button(gui, text="شروع یادگیری", command=output_data, width=18, background="dark orange")
button1.grid(row=7, column=0, columnspan=5)
button1.grid_rowconfigure(7, weight=1)
button1.grid_columnconfigure(1, weight=1)
button1['font'] = my_font

label3 = Label(gui, text="by : Sina Razi", foreground="white", font=0.5, background="blue3")
label3.grid(row=8, column=0, columnspan=5)
label3.grid_rowconfigure(8, weight=1)
label3.grid_columnconfigure(0, weight=1)
label3['font'] = my_font1
# Inorder to make GUI responsive

mainloop()
