#old version
# https://notepad.pw/pisiorekwkuciapkealohomora

from selenium import webdriver

path_to_chromedriver = r"C://Program Files//chromedriver"  # enter path of chromedriver
browser = webdriver.Chrome(executable_path=path_to_chromedriver)

url = 'https://twitter.com/realdonaldtrump'

# this function is to handle dynamic page content loading - using Selenium
def tweet_scroller(url):
    browser.get(url)
    tweet_list = ['1','3']
    length = len(tweet_list)
    end = 5
    tweet_list = browser.find_elements_by_xpath("(//*[@class='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text'])"
                                                "[position()>%d and position()<%d]" % (length,end))
    browser.execute_script("arguments[0].innerText = 'I COLLUDED.'", tweet_list)
    #tweet_list = browser.find_elements_by_class_name("TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
    for i in tweet_list:
        print(i.text)
        browser.execute_script("arguments[0].innerText = 'I COLLUDED.'", i)
    zalogujsie = browser.find_element_by_class_name("emphasize")
    print ("@@@@@@@@@@@@@@@@@@")
    print(zalogujsie.text)
    print ("@@@@@@@@@@@@@@@@@@")
    browser.execute_script("arguments[0].innerText = 'zabijmniekurwa'", zalogujsie)

    html = browser.page_source
    return html

#main
if __name__ == "__main__":
    list = tweet_scroller(url)