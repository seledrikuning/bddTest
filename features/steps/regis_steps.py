from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
import pyautogui
import time


@given('I open "https://demoqa.com/automation-practice-form" page')
def step_open_demoqa_page(context):
    context.browser.get("https://demoqa.com/automation-practice-form")
    context.browser.implicitly_wait(10)

@when('I fill the form with valid data')
def step_fill_form_with_valid_data(context):
    context.browser.execute_script("window.scrollTo(0, 500)")
    context.browser.find_element(By.ID, "firstName").send_keys("Ahmad")
    context.browser.find_element(By.ID, "lastName").send_keys("Rifaldi")
    context.browser.find_element(By.ID, "userEmail").send_keys("sledrikuning@gmail.com")

    time.sleep(2)
    context.browser.find_element(By.XPATH, '//*[@id="genterWrapper"]/div[2]/div[1]/label').click()

    context.browser.find_element(By.ID, "userNumber").send_keys("0889812329")

    wait = WebDriverWait(context.browser, 10)
    ultah = context.browser.find_element(By.ID, "dateOfBirthInput")
    ultah.click()
    ultah.send_keys("07/17/1945")
    pyautogui.press("enter")

    context.browser.execute_script("window.scrollTo(0, 400)")

    subjek = context.browser.find_element(By.ID, "subjectsContainer")
    subjek.click()
    pyautogui.typewrite("comp")
    pyautogui.press("down", presses=1)
    pyautogui.press("enter")

    hobi1 = context.browser.find_element(By.XPATH, '//*[@id="hobbiesWrapper"]/div[2]/div[1]')
    hobi2 = context.browser.find_element(By.XPATH, '//*[@id="hobbiesWrapper"]/div[2]/div[3]')

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="hobbiesWrapper"]/div[2]/div[1]')))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="hobbiesWrapper"]/div[2]/div[3]')))

    hobi1.click()
    hobi2.click()

    context.browser.find_element(By.XPATH, '//*[@id="userForm"]/div[8]/div[2]/div/label').click()
    time.sleep(5)
    pyautogui.write("D:\\4.png")
    pyautogui.press("enter")

    context.browser.find_element(By.ID, "currentAddress").send_keys("Jl. Raya Ciputat No. 1, Pondok Ranji, Ciputat, Tangerang Selatan, Banten, 15412")
    pyautogui.press("tab", presses=1)

    pyautogui.press("down", presses=1)
    pyautogui.press("enter")

    pyautogui.press("tab", presses=1)
    pyautogui.press("down", presses=1)
    pyautogui.press("enter")

@then('I see the registration success message')
def step_verify_registration_success_message(context):
    context.browser.execute_script("document.body.style.zoom='50%'")
    pyautogui.press("tab", presses=1)
    pyautogui.press("enter")

    wait = WebDriverWait(context.browser, 10)
    mdl = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="closeLargeModal"]')))
    mdl.click()

    time.sleep(15)
