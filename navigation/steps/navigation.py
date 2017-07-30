
from behave import *
from browser import Browser
import unittest

# @given('the room5 website')
# def step_impl(context):
#     context.browser.visit('/')

# @When('the user enter on it')
# def step_impl(context):
#     context.browser.find_by_class_name('single-header')
#     context.browser.find_by_id('content')
#     context.browser.find_by_id('footer')

# @Then('s/he is able to see the web page successfully')
# def step_impl(context):
# 	context.browser.find_by_id('editors_pick')
# 	context.browser.find_by_id('most_popular')
# 	context.browser.find_by_id('latest_post')
# 	context.browser.find_by_id('inspiration')
# 	context.browser.find_by_id('destinations')

@given(u'the user is on the main page of room5')
def step_impl(context):
	context.browser.visit('/')

@when(u'the s/he search for \'Brazil\' on the search field')
def step_impl(context):
	context.browser.find_by_class_name('room5-icons-search').click()
    raise NotImplementedError(u'STEP: When the s/he search for \'Brazil\' on the search field')

@then(u'the site will return his/her research.')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the site will return his/her research.')

