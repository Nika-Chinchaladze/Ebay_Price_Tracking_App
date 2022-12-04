from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pyperclip
from Ebay_Class import EbayPrice
from Json_Class import JsonDealer
from Gmail_Class import SendEmail

HEAD_FONT = ("Helvetica", 17, "bold")
LB_FONT = ("Helvetica", 12, "bold")
EN_FONT = ("Helvetica", 12, "normal")


class TrackEbay:
    def __init__(self, window):
        self.window = window
        self.window.title("Track Prices")
        self.window.geometry("1000x650")
        self.window.configure(bg="lavender")
        # friend classes:
        self.ebay_tool = EbayPrice()
        self.json_tool = JsonDealer()
        # extra variables:
        self.entered_link = StringVar()
        self.entered_name = StringVar()
        self.chosen_product = StringVar()
        self.chosen_price = StringVar()
        self.to_person = StringVar()
        self.subject_person = StringVar()
        # data contain variables:
        self.combo_box_items = []

        # heading:
        self.head_label = Label(self.window, text="Track Ebay Prices with One Click", font=HEAD_FONT, justify="center",
                                bd=1, highlightthickness=1, relief=RIDGE, bg="lavender")
        self.head_label.place(x=10, y=5, width=980, height=50)

        # image:
        used_image = Image.open("IMG/ebay.png")
        used_photo = ImageTk.PhotoImage(used_image)
        self.ebay_label = Label(self.window, image=used_photo, highlightthickness=1, bg="lavender")
        self.ebay_label.image = used_photo
        self.ebay_label.place(x=180, y=60, width=640, height=256)

        # =============================== top frame ================================== #
        self.top_frame = Frame(self.window, bd=1, highlightthickness=1, relief=RIDGE, bg="lavender")
        self.top_frame.place(x=10, y=320, width=980, height=80)

        self.link_label = Label(self.top_frame, text="Link", font=LB_FONT, justify="center", bd=1,
                                highlightthickness=1, relief=RIDGE, bg="pale goldenrod")
        self.link_label.place(x=5, y=5, width=120, height=30)

        self.link_entry = Entry(self.top_frame, font=EN_FONT, textvariable=self.entered_link)
        self.link_entry.place(x=130, y=5, width=678, height=30)

        self.name_label = Label(self.top_frame, text="Product Name", font=LB_FONT, justify="center", bd=1,
                                highlightthickness=1, relief=RIDGE, bg="pale goldenrod")
        self.name_label.place(x=5, y=40, width=120, height=30)

        self.name_entry = Entry(self.top_frame, font=EN_FONT, textvariable=self.entered_name,
                                justify="center")
        self.name_entry.place(x=130, y=40, width=335, height=30)

        self.save_button = Button(self.top_frame, text="Save Information", justify="center", font=LB_FONT,
                                  bd=1, highlightthickness=1, relief=RIDGE, bg="teal", fg="white smoke",
                                  highlightbackground="medium sea green", command=self.save_method)
        self.save_button.place(x=473, y=40, width=335, height=30)

        refresh_image = Image.open("IMG/ref.png")
        refresh_photo = ImageTk.PhotoImage(refresh_image)
        self.refresh_button = Button(self.top_frame, image=refresh_photo, justify="center", font=LB_FONT,
                                     bd=1, highlightthickness=1, relief=RIDGE, bg="alice blue",
                                     command=self.refresh_method)
        self.refresh_button.image = refresh_photo
        self.refresh_button.place(x=815, y=5, width=155, height=65)

        # =============================== left frame ================================== #
        self.left_frame = Frame(self.window, bd=1, highlightthickness=1, relief=RIDGE, bg="lavender")
        self.left_frame.place(x=10, y=405, width=485, height=230)

        self.product_label = Label(self.left_frame, text="Choose Product", font=LB_FONT, justify="center", bd=1,
                                   highlightthickness=1, relief=RIDGE, bg="gainsboro")
        self.product_label.place(x=5, y=5, width=235, height=30)

        self.product_box = ttk.Combobox(self.left_frame, justify="center", font=LB_FONT,
                                        textvariable=self.chosen_product)
        self.product_box.place(x=245, y=5, width=230, height=30)

        self.price_label = Label(self.left_frame, text="Enter Your Price", font=LB_FONT, justify="center", bd=1,
                                 highlightthickness=1, relief=RIDGE, bg="gainsboro")
        self.price_label.place(x=5, y=40, width=235, height=30)

        self.price_entry = Entry(self.left_frame, font=EN_FONT, textvariable=self.chosen_price,
                                 justify="center")
        self.price_entry.place(x=245, y=40, width=230, height=30)

        self.search_button = Button(self.left_frame, text="Search Product's Current Price", justify="center",
                                    font=LB_FONT,
                                    bd=1, highlightthickness=1, relief=RIDGE, bg="dark sea green",
                                    fg="white smoke", command=self.search_method)
        self.search_button.place(x=5, y=80, width=470, height=30)

        self.output_label = Label(self.left_frame, text="", font=LB_FONT, justify="center", bd=1,
                                  highlightthickness=1, relief=RIDGE)
        self.output_label.place(x=5, y=120, width=470, height=65)

        self.copy_button = Button(self.left_frame, text="Copy Link", justify="center", font=LB_FONT, bd=1,
                                  highlightthickness=1, relief=RIDGE, bg="salmon",
                                  command=self.copy_method)
        self.copy_button.place(x=5, y=190, width=100, height=30)

        self.copied = Label(self.left_frame, text="", font=LB_FONT, justify="center", bd=1,
                            highlightthickness=1, relief=RIDGE, bg="light gray")
        self.copied.place(x=110, y=190, width=364, height=30)

        # =============================== right frame ================================== #
        self.right_frame = Frame(self.window, bd=1, highlightthickness=1, relief=RIDGE, bg="lavender")
        self.right_frame.place(x=500, y=405, width=490, height=230)

        self.to_label = Label(self.right_frame, text="To:", font=LB_FONT, justify="center", bd=1,
                              highlightthickness=1, relief=RIDGE)
        self.to_label.place(x=5, y=5, width=50, height=30)

        self.to_entry = Entry(self.right_frame, font=EN_FONT, textvariable=self.to_person,
                              justify="center")
        self.to_entry.place(x=115, y=5, width=364, height=30)

        self.subject_label = Label(self.right_frame, text="Subject:", font=LB_FONT, justify="center", bd=1,
                                   highlightthickness=1, relief=RIDGE)
        self.subject_label.place(x=5, y=40, width=100, height=30)

        self.subject_entry = Entry(self.right_frame, font=EN_FONT, textvariable=self.subject_person,
                                   justify="center")
        self.subject_entry.place(x=115, y=40, width=364, height=30)

        self.text_entry = Text(self.right_frame, font=EN_FONT)
        self.text_entry.place(x=5, y=80, width=473, height=100)

        self.send_button = Button(self.right_frame, text="Send Message", justify="center", font=LB_FONT,
                                  bd=1, highlightthickness=1, relief=RIDGE, bg="royal blue", fg="white smoke",
                                  command=self.send_method)
        self.send_button.place(x=5, y=190, width=230, height=30)

        self.close_button = Button(self.right_frame, text="Close Application", justify="center", font=LB_FONT,
                                   bd=1, highlightthickness=1, relief=RIDGE, bg="coral",
                                   command=self.close_method)
        self.close_button.place(x=248, y=190, width=230, height=30)

    # ============================= FUNCTIONALITY ================================== #
    def close_method(self):
        self.window.destroy()

    def save_method(self):
        try:
            self.json_tool.append_jason(product_name=self.entered_name.get(), link=self.entered_link.get())
            messagebox.showinfo(title="feedback", message="information has been saved!")
        except FileNotFoundError:
            self.json_tool.create_json()

    def refresh_method(self):
        self.product_box["values"] = self.json_tool.get_product_names()
        self.entered_link.set("")
        self.entered_name.set("")
        self.chosen_price.set("")
        self.copied.config(text="", bg="light gray")
        self.output_label.config(text="", bg="light gray")
        self.text_entry.delete("1.0", END)
        self.subject_person.set("")

    def search_method(self):
        address = self.json_tool.get_product_link(product_name=self.chosen_product.get())
        price = self.ebay_tool.get_current_price(product_link=address)
        if float(self.chosen_price.get()) >= float(price):
            self.output_label.config(bg="light green", text=f"Good News, This {self.chosen_product.get()} is available "
                                                            f"for - ${price}!")
        else:
            self.output_label.config(bg="tomato", text=f"Bad News, This {self.chosen_product.get()} is available only "
                                                       f"for - ${price}!")

    def copy_method(self):
        product_link = self.json_tool.get_product_link(product_name=self.chosen_product.get())
        pyperclip.copy(product_link)
        self.copied.config(text="URL Has Been Copied!", bg="khaki")

    def send_method(self):
        send_tool = SendEmail(
            receiver=self.to_person.get(),
            subject=self.subject_person.get(),
            body=self.text_entry.get("1.0", END)
        )
        send_tool.send_mail()
        messagebox.showinfo(title="feedback", message="message has been send!")


def launch_app():
    app = Tk()
    TrackEbay(app)
    app.mainloop()


if __name__ == "__main__":
    launch_app()
