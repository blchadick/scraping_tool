# scraping_tool

Overview:

This script utilizes the Selenium Python library and Webdriver to automate crawling of websites, including responsive web applications. A sequence of actions is fed into the script as a CSV file. The script executes those actions, returning the results of their executions and a screenshot. Specific elements within a page can be targeted by either specifying xPath or CSS selectors.
The following methods are implemented in the latest iteration of the script.

**METHOD:**	               DESCRIPTION

**get_url:**	                  Navigates to a specified URL

**get_element_text:**	        Gets the text value of a specified element

**get_element_attrib:**	      Returns the attribute value of a specified element and attribute

**action_element_click:**	    Clicks on a specified element

**action_element_sendkeys:**	  Enters text into a specified element

**send_keys_submit:**	        Enters text into a specified element and presses the return key

**get_table_rows:**	        Returns rows in a table
