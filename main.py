"""
Структура пакета
driver - содержит драйвера Chrome и FireFox
"""

import threading
import time

import moduls.webdriver as driver


def main():
    parser = driver.Parser()
    