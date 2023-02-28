from tkinter import *
import random
root=Tk()
root.title("Country Capitals")
root.geometry("500x500")

enter_country = Entry(root)
enter_country.place(relx = 0.5, rely = 0.2, anchor = CENTER)
enter_capital = Entry(root)
enter_capital.place(relx = 0.5, rely = 0.3, anchor = CENTER)
display_country_list = Label(root)
display_capital_list = Label(root)
display_random_country_list = Label(root)
display_random_capital_list = Label(root)
country_list = []
capital_list = []

def Country_City_List():
    country = enter_country.get()
    country_list.append(country)
    display_country_list["text"] = "Country Name:" + str(country_list)
    capital = enter_capital.get()
    capital_list.append(capital)
    display_Capital_list["text"] = "City Name:" + str(capital_list)
    
def Random_Country_City():
    length1 = len(country_list)
    random_number1 = random.randint(0, length1 - 1)
    random_country = country_list[random_number1]
    display_random_country_list["text"] = "Random Country :" + str(random_country)
    
    length2 = len(capital_list)
    random_number2 = random.randint(0, length2 - 1)
    random_capital = capital_list[random_number2]
    display_random_capital_list["text"] = "Random Capital :" + str(random_capital)

btn = Button(root, text = " Display Country And City Name ", command = Country_City_List , bg ="Royal Blue", fg ="White") 
btn.place(relx = 0.5, rely = 0.4 , anchor = CENTER) 
display_country_list.place(relx = 0.5, rely = 0.5 , anchor = CENTER) 
display_capital_list.place(relx = 0.5, rely = 0.6 , anchor = CENTER) 
btn2 = Button(root, text = " Display Country And City Name Randomly", command = Random_Country_City,bg ="Royal Blue", fg ="White") 
btn2.place(relx = 0.5, rely = 0.7 , anchor = CENTER) 
display_random_country_list.place(relx = 0.5, rely = 0.8 , anchor = CENTER) 
display_random_capital_list.place(relx = 0.5, rely = 0.9 , anchor = CENTER) 
root.mainloop()