
from behave import *
from browser import Browser
import unittest


# Scenario: User is able to enter on room5 website

@given(u'the room5 website')
def step_impl(context):
    context.browser.visit('/')

@When(u'the user enter on it')
def step_impl(context):
    context.browser.find_by_class_name('single-header')
    context.browser.find_by_id('content')
    context.browser.find_by_id('footer')

@Then(u's/he is able to see the web page successfully')
def step_impl(context):
	context.browser.find_by_id('editors_pick')
	context.browser.find_by_id('most_popular')
	context.browser.find_by_id('latest_post')
	context.browser.find_by_id('inspiration')
	context.browser.find_by_id('destinations')

# Scenario: User is able to search for something

@given(u'the user is on the main page of room5')
def step_impl(context):
	context.browser.visit('/')

@when(u'the s/he search for \'Brazil\' on the search field')
def step_impl(context):
	context.browser.search('Brazil')
    
@then(u'the site will return his/her research.')
def step_impl(context):
    context.browser.search_result()

# 