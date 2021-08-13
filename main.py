
import sys
import os
import time
from random import randint
import traceback
import pickle
import urllib.parse as urlparse
from urllib.parse import parse_qs

C = os.path.abspath(os.path.dirname(__file__))

from selenium.webdriver.common.keys import Keys
from splinter import Browser

profile = "rust_mozprofileQtFvLF"
browser = Browser(executable_path="geckodriver.exe", profile=profile)

admin_booking = "https://admin.booking.com/hotel/hoteladmin/extranet_ng/manage/home.html?hotel_id=55319&t=1546801233&lang=fr&ses=15e42419bd2589b1a21d148f1dd32109"

browser.visit(admin_booking)

id_booking = os.path.join(C, "..", "id_booking.pkl")
with open(id_booking, "rb") as f_in:
    data = pickle.load(f_in)
    login = data["user"]
    password = data["pass"]

browser.find_by_id("loginname").fill(login)
browser.find_by_css("button.bui-button--wide > span:nth-child(1)").click()
browser.find_by_id("password").fill(password)
browser.find_by_css("button.bui-button:nth-child(3) > span:nth-child(1)").click()

input("Procédure de connexion par SMS")

# click sur réservations
browser.find_by_css("li.ext-navigation-top-item:nth-child(4)").click()

# catch "ses"
parsed = urlparse.urlparse(browser.url)
ses = parse_qs(parsed.query)["ses"][0]

def show_reservations(date_from, date_to):
    link_reservations = "https://admin.booking.com/hotel/hoteladmin/extranet_ng/manage/search_reservations.html?upcoming_reservations=1&source=nav&hotel_id=55319&lang=fr&date_type=arrival"
    getVars = { "date_from": date_from,
                "date_to": date_to,
                "ses": ses}
    return link_reservations + parse_qs.urlencode(getVars)

