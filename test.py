from selenium import webdriver
from selenium.webdriver import ActionChains
from tabulate import tabulate
import time

PATH = "/usr/local/bin/"
driver = webdriver.Chrome(PATH)

driver.set("https://www.goodreads.com/choiceawards/best-fiction-books-2022")

time.sleep(3)

print("\n")