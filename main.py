from __future__ import print_function
import json
import os
import pandas as pd
import csv
import datetime
from datetime import date
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from codecs import encode
import selenium

# Creates a webdriver instance
def get_driver(chrome_binary,chrome_driver_binary): 
    my_options = Options()
    my_options.binary_location = chrome_binary
    driver = webdriver.Chrome(chrome_driver_binary, chrome_options=my_options)
    return driver

# Checks if an element exists. 
def element_exists(driver,selector,selector_type):
    try:
        if selector_type == 'css':
            driver.find_element_by_css_selector(selector)
        elif selector_type == 'xpath':
            driver.find_element_by_xpath(selector)
        return True
    except:
        return False

# Container for executing methods
def element_action(method_args):
    driver              = method_args['driver']
    element_selector    = method_args['element_selector']
    method_name         = method_args['method_name']
    retry_count         = int(method_args['retry_count'])
    selector_type       = method_args['selector_type']
    
    returnvalue = {}
    if element_selector == '':
        returnvalue = exec_method(driver,method_name,'',method_args)
        returnvalue['method'] = method_name
        return [returnvalue]
    else:
        if element_exists(driver,element_selector,selector_type):
            i = 0
            # This loop waits for the DOM to finish loading
            while i < retry_count:
                print(i)
                try:
                    time.sleep(1)
                    if selector_type == 'xpath':
                        this_element = driver.find_element_by_xpath(element_selector)
                        returnvalue = exec_method(driver,method_name,this_element,method_args)
                        returnvalue['method'] = method_name
                        return [returnvalue]
                    elif selector_type == 'css':
                        this_element = driver.find_element_by_css_selector(element_selector)
                        returnvalue = exec_method(driver,method_name,this_element,method_args)
                        returnvalue['method'] = method_name
                        return [returnvalue]
                except selenium.common.exceptions.StaleElementReferenceException:
                    i+=1         
        else:
            print('element not found')
            return [{'error':'Element not found'}]

##### Methods ####

# Clicks on the specified element
def action_element_click(driver,selenium_element,method_args):
    time.sleep(float(method_args['wait']))
    selenium_element.click()
    time.sleep(float(method_args['wait']))
    driver.save_screenshot(method_args['test_folder']+'screenshots/'+method_args['action_id']+'.png')
    return {'return_value':'action successful', 'js_log': driver.get_log('browser'),'timestamp':str(datetime.datetime.now())}

# Returns the text value of the specified element
def get_element_text(driver,selenium_element,method_args):
    time.sleep(float(method_args['wait']))
    #driver.save_screenshot(method_args['test_folder']+'screenshots/'+method_args['action_id']+'.png')
    this_element_text = selenium_element.text
    response = {'return_value':this_element_text.encode('utf-8'), 'js_log': driver.get_log('browser'),'timestamp':str(datetime.datetime.now())}
    response['action_id'] = method_args['action_id']
    return response


def get_element_html(driver,selenium_element,method_args):
    time.sleep(float(method_args['wait']))
    #driver.save_screenshot(method_args['test_folder']+'screenshots/'+method_args['action_id']+'.png')
    this_element_html = selenium_element.get_attribute('innerHTML')
    response = {'return_value':this_element_html.encode('utf-8'), 'js_log': driver.get_log('browser'),'timestamp':str(datetime.datetime.now())}
    response['action_id'] = method_args['action_id']
    return response

# Returns the text value of the specified element attribute
def get_element_attrib(driver,selenium_element,method_args):
    time.sleep(float(method_args['wait']))
    #driver.save_screenshot(method_args['test_folder']+'screenshots/'+method_args['action_id']+'.png')
    this_element_attrib = selenium_element.get_attribute(method_args['attrib'])
    response={'return_value':this_element_attrib, 'js_log': driver.get_log('browser'),'timestamp':str(datetime.datetime.now())}
    response['action_id'] = method_args['action_id']
    return response
    
# Enters text into the specified element
def action_element_sendkeys(driver,selenium_element,method_args):
    response = {}
    if method_args['sendkeys_text'] == 'Keys.ENTER':
        sendkeys_text = Keys.ENTER
    else:
        sendkeys_text = method_args['sendkeys_text']
    selenium_element.clear()
    selenium_element.send_keys(sendkeys_text)
    time.sleep(float(method_args['wait']))
    driver.save_screenshot(method_args['test_folder']+'screenshots/'+method_args['action_id']+'.png')
    # Build the response
    response['action_id']       = method_args['action_id']
    response['return_value']    = 'action_successful'
    response['js_log']          = driver.get_log('browser')
    response['timestamp']       = str(datetime.datetime.now())
    return response

# Returns the text value of the specified element attribute
def get_table_rows(driver,selenium_element,method_args):
    time.sleep(float(method_args['wait']))
    rows =""
    for tr in selenium_element.find_elements_by_tag_name('tr'): ### All rows in the
        rows = rows + '\n' + tr.text
    response={'return_value':'"'+rows+'"', 'js_log': driver.get_log('browser'),'timestamp':str(datetime.datetime.now())}
    response['action_id'] = method_args['action_id']
    return response

# Enters text into the specified element and presses the "ENTER" key

def send_keys_submit(driver,selenium_element,method_args):
    response = {}
    sendkeys_text = method_args['sendkeys_text']
    selenium_element.clear()
    selenium_element.send_keys(sendkeys_text)
    selenium_element.send_keys(Keys.ENTER)
    time.sleep(float(method_args['wait']))
    driver.save_screenshot(method_args['test_folder']+'screenshots/'+method_args['action_id']+'.png')

    # Build the response
    response['action_id']       = method_args['action_id']
    response['return_value']    = 'action_successful'
    response['js_log']          = driver.get_log('browser')
    response['timestamp']       = str(datetime.datetime.now())
    return response

def get_url(driver,selenium_element,method_args):
    driver.get(method_args['open_url'])
    time.sleep(float(method_args['wait']))
    driver.save_screenshot(method_args['test_folder']+'screenshots/'+method_args['action_id']+'.png')
    response = {'return_value':'action successful', 'js_log': driver.get_log('browser'),'timestamp':str(datetime.datetime.now())}
    response['action_id'] = method_args['action_id']
    return response

def custom_action1():
    pass

methods = {
            'get_element_text':         get_element_text, 
            'get_element_attrib':       get_element_attrib,
            'action_element_click':     action_element_click,
            'action_element_sendkeys':  action_element_sendkeys,
            'get_url':                  get_url,
            'send_keys_submit':         send_keys_submit,
            'custom_action1':           custom_action1,
            'get_element_html':         get_element_html,
            'get_table_rows':           get_table_rows
            }

def exec_method(driver,method_name,selenium_element,method_args):
    if method_name in methods:
        method_output = methods[method_name](driver,selenium_element,method_args)
        return method_output
    else:
        raise Exception("Method %s not implemented" % method_name)

def create_folderstructure(timestamp):
    test_dir        ='output/'+timestamp+'/'
    screenshot_dir  = test_dir + 'screenshots'
    results_dir     = test_dir + 'results'
    os.mkdir(test_dir)
    os.mkdir(screenshot_dir)
    os.mkdir(results_dir)
    return test_dir

def parse_testscript(filename):
    test_actions = []
    with open(filename,'rb') as infile:
        csvreader = csv.DictReader(infile)
        for row in csvreader:
            test_actions.append(row)
        return test_actions

if __name__ == '__main__':
    # Load configuration
    with open("config.json","r") as jsonfile:
        config = json.load(jsonfile)
    start_url               = config['start_url']
    chrome_binary           = config['chrome_binary']
    chrome_driver_binary    = config['chrome_driver_binary']
    test_scripts            = ['test_script_template.csv']

    driver = get_driver(chrome_binary, chrome_driver_binary)
    driver.fullscreen_window()
    
    timestamp       = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    test_folder     = create_folderstructure(timestamp)
    for test_script in test_scripts:
        test_steps      = parse_testscript(test_script)
        test_results    =[]
        for test_args in test_steps:
            test_args['driver']         = driver
            test_args['test_folder']    = test_folder
            test_results = test_results + element_action(test_args)
    
        df_steps    = pd.DataFrame(test_steps)
        df_results  = pd.DataFrame(test_results)
        df_merge = df_steps.merge(right=df_results,on='action_id')
        df_merge.to_csv(test_folder+'results/results.csv')
        driver.close()
