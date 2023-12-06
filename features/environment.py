from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
import pyautogui
import time


def before_scenario(context, scenario):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()


def after_scenario(context, scenario):
    context.browser.quit()