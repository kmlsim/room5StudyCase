from browser import Browser
from selenium import webdriver
import unittest

def before_all(context):
    context.browser = Browser()

def after_all(context):
    context.browser.close()
