import tkinter as tk
import translink_sfu
from PIL import Image, ImageTk

# START tkinter
root= tk.Tk()
root.title("SFU VAN-BUR TRAVEL")
root.geometry("720x480")
root.resizable(False,False)

# ADD bg image
bg_bur = ImageTk.PhotoImage(Image.open("data/map_bur.png")) # IMAGE FROM GOOGLE MAP
bg_van = ImageTk.PhotoImage(Image.open("data/map_van.png")) # IMAGE FROM GOOGLE MAP
bg_image = tk.Label(root, image = bg_bur)
bg_image.place(x=0, y=0)

# BUTTON with TXT
van_to_bur = True


def change_direction():
    global van_to_bur
    label_bur.place_forget()
    label_van.place_forget()
    if van_to_bur:
        van_to_bur = False
        btn_dir['text'] = 'SFU: Bur -> Van'
        bg_image.configure(image=bg_van)
        bg_image.image = bg_van
    else:
        van_to_bur = True
        btn_dir['text'] = 'SFU: Van -> Bur'
        bg_image.configure(image=bg_bur)
        bg_image.image = bg_bur


btn_dir = tk.Button(root, text="SFU: Van -> Bur", bg="#CC0633", fg="white",
                font=('helvetica', 9, 'bold'), command=change_direction)
btn_dir.place(x=0, y=0)

# ESTIMATE interval label
# label_bur = tk.Label(root, text="", bg="#FFFFFF", width=5,height=5)
label_bur = tk.Label(root, text="", bg="#FFFFFF", wraplength=70)
label_van = tk.Label(root, text="", bg="#FFFFFF", wraplength=70)
# pack()
# pack_forget()
# label_bur.place(x=272, y=160)
# label_van.place(x=260, y=260)


# BUTTON for calculate
def cal_estimate():
    global van_to_bur
    if van_to_bur:
        # Eastbound W Hastings St @ Granville St
        soup = translink_sfu.get_data(51374)
        bus_lst = translink_sfu.time_to_leave(soup)
        print(bus_lst)
        for bus in bus_lst:
            if bus['bus_num'] == 'R5':
                label_bur.place(x=272, y=160)
                time_left = bus['bus_time']
                interval = f"[{time_left+42},{time_left+62}] minutes"
                label_bur.config(text = interval)
    else:
        # SFU Transportation Centre @ Bay 1
        soup = translink_sfu.get_data(53096) # 60015 is exact but not working 22 Aug. 15
        bus_lst = translink_sfu.time_to_leave(soup)
        print(bus_lst)
        for bus in bus_lst:
            if bus['bus_num'] == 'R5':
                label_van.place(x=260, y=260)
                time_left = bus['bus_time']
                interval = f"[{time_left+42},{time_left+62}] minutes"
                label_van.config(text = interval)



btn_cal = tk.Button(root, text="CALCULATE", bg="#CC0633", fg="white",
                font=('helvetica', 9, 'bold'), command=cal_estimate)
btn_cal.place(x=620, y=0)


# REQUIRED
root.mainloop()