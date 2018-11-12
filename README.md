# scraping_tool

## Overview:

This script utilizes the Selenium Python library and Webdriver to automate crawling of websites, including responsive web applications. A sequence of actions is fed into the script as a CSV file. The script executes those actions, returning the results of their executions and a screenshot. Specific elements within a page can be targeted by either specifying xPath or CSS selectors.
The following methods are implemented in the latest iteration of the script.

## Setup:

In the config.json file, enter the location of your Selenium webdriver binary and chrome binary. Enter the location of your test script template -- this file provides crawling instructions to the script.

action_id
method_name
element_selector
selector_type
attrib
wait
retry_count
sendkeys_text
open_url
action_description






## Methods

- **x**: required argument for method
- **o**: optional argument for method


|**METHOD**	   |METHOD_DESCRIPTION|element_selector|selector_type|attrib|wait|retry_count|sendkeys_text	|open_url|action_description|
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|**get_url**	                 | Navigates to a specified URL|x|x||x|x||x|o|
|**get_element_text**	       | Gets the text value of a specified element|x|x||x|x|||o|
|**get_element_attrib**	     | Returns the attribute value of a specified element and attribute|x|x|x|x|x|||o|
|**action_element_click**	   | Clicks on a specified element|x|x||x|x|||o|
|**action_element_sendkeys**	 | Enters text into a specified element|x|x||x|x|x||o|
|**send_keys_submit**	      |  Enters text into a specified element and presses the return key|x|x||x|x|x||o|
|**get_table_rows**	      |  Returns rows in a table|x|x||x|x|||o|
