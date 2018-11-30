from config import keys
from selenium import webdriver
import time


def order(k):
	driver = webdriver.Chrome('./chromedriver')
	
	driver.get(k['product_url'])

	driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
	time.sleep(1)
	driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
	# name
	driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(k["name"])
	# email
	driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(k["email"])
	# phone
	driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(k["phone_number"])
	# address
	driver.find_element_by_xpath('//*[@id="bo"]').send_keys(k["address"])
	# zip
	driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(k["zip"])
	# city
	driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(k["city"])
	# state
	driver.find_element_by_xpath('//*[@id="order_billing_state"]').send_keys(k["state"])
	# card information
	driver.find_element_by_xpath('//*[@id="nnaerb"]').send_keys(k["card_number"])
	driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(k["card_cvv"])
	# card month
	driver.find_element_by_xpath('//*[@id="credit_card_month"]/option[{}]').format(k["credit_card_month"]).click()
	#card year 
	driver.find_element_by_xpath('//*[@id="credit_card_year"]/option[{}]').format(k["credit_card_year"]).click()
	# terms and conditions
	driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()
	# process payment
	driver.find_element_by_xpath('//*[@id="pay"]/input').click()

if __name__ == '__main__':
	order(keys)
