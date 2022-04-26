# pip install phonenumbers
# pip install future for making a graphical window using tkinter

import tkinter as tk
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

window = tk.Tk()
window.geometry('500x500')
window.title("one MINUTE man ")

class Buttons:

    def info(self):
        try:
            phone = phonenumbers.parse(entry.get())

            # this will print country name
            country_name = geocoder.description_for_number(phone, 'en')
            label2 = tk.Label(window, text=f"country name:{country_name}")
            label2.pack()

            # this will print service provider
            service_provider = carrier.name_for_number(phone, 'en')
            label3= tk.Label(window, text=f"service provider:{service_provider}")
            label3.pack()

            # this will print timezone
            time_zone = timezone.time_zones_for_number(phone)
            label4 = tk.Label(window, text=f"timezone:{time_zone}")
            label4.pack()

        except Exception as e:
            label5 = tk.Label(window, text=f"error:{e}")
            label5.pack()

        finally:
            label6 = tk.Label(window, text="""Thank you for using this app😁.
            We gat you
            """)
            label6.pack()


btn =Buttons()


def on_click():
    pass

number = tk.StringVar()
label1 = tk.Label(window, text="enter phone number (+xxx,xxx, xxx,xxx): ", bg="blue")
label1.pack(pady=10)

entry = tk.Entry(window, textvariable=number)
entry.pack(pady=10)

button = tk.Button(window, text="get Info", bg="green", fg="black", command=btn.info)
button.pack(pady=10)

button2 = tk.Button(window, text="delete results", bg="red", fg="black", command=on_click)
button2.pack(pady=10)

tk.mainloop()
