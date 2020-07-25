#!/usr/bin/env python

from selenium import webdriver
import time
import sympy


def main():
    link = "https://isthisprime.com/game/"

    driver = webdriver.Firefox()
    driver.get(link)

    # get start button
    start_button = driver.find_element_by_css_selector("button")

    # start the game
    start_button.click()

    # get the yes and no buttons
    yes_button = driver.find_element_by_id("yes")
    no_button = driver.find_element_by_id("no")

    # get the time element
    time_span = driver.find_element_by_id("time")

    # get the number to select whether it is prime or not
    number_span = driver.find_element_by_id("n")

    # get current time
    current_time = float(time_span.text)

    # use the while loop so that time gets displayed at the end of game, instead
    # of continuing
    while current_time > 0.1:
        number = int(number_span.text)

        # click yes if prime, no otherwise
        if sympy.isprime(number):
            yes_button.click()
        else:
            no_button.click()

        # update time
        current_time = float(time_span.text)

if __name__ == "__main__":
    main()
