from selenium import webdriver
import chromedriver_binary
driver = webdriver.Chrome()         
driver.get('https://oxylabs.io/blog')

blog_titles = driver.get_elements_by_css_selector(' h2.blog-card__content-title')
for title in blog_tiles:
    print(title.text)
driver.quit()