from tkinter import *
from tkinter import messagebox
from bs4 import BeautifulSoup
import requests
import sqlite3


def add_website():
    url = website_entry.get()
    if url.strip() != "":
        try:

            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            title = soup.title.string.strip()

            conn = sqlite3.connect("websites.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO websites (url, title) VALUES (?, ?)", (url, title))
            conn.commit()
            conn.close()

            update_websites_listbox()
            website_entry.delete(0, END)
        except:
            messagebox.showerror("Помилка", "Не вдалося додати сайт.")
    else:
        messagebox.showerror("Помилка", "Введіть адресу сайту.")


def clear_database():
    if messagebox.askyesno("Підтвердження", "Ви дійсно бажаєте очистити базу даних?"):
        conn = sqlite3.connect("websites.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM websites")
        conn.commit()
        conn.close()
        # Оновлення списку сайтів
        update_websites_listbox()


def search_websites():
    keyword = keyword_entry.get()
    if keyword.strip() != "":

        results_listbox.delete(0, END)
        
        conn = sqlite3.connect("websites.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM websites")
        websites = cursor.fetchall()
        for website
