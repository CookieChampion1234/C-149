from tkinter import*
import random

root=Tk()

root.geometry("500x500")
root.title("Random Friend Generator")

friend_list = ["Sophia", "Quinn", "Aranza", "Gilberto", "Emma"]
print(friend_list)

def randomFriend():
    random_no = random.randint(0,4)
    print(random_no)
    lucky_friend = friend_list[random_no]
    print("Your lucky friend is : " + lucky_friend)
    
btn = Button(root)
btn = Button(text="Who is your lucky friend?",command=randomFriend)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()