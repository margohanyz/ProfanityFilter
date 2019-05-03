#old version
#https://notepad.pw/pisiorekwkuciapkealohomora

from selenium import webdriver

path_to_chromedriver = r'\chromedriver.exe'  # enter path of chromedriver

url = 'https://twitter.com/realdonaldtrump'

# this function is to handle dynamic page content loading - using Selenium
def tweet_scroller(url, text):
    browser = webdriver.Chrome(executable_path=path_to_chromedriver)
    browser.get(url)
    tweet_list = ['1','3']
    length = len(tweet_list)
    end = 5
    tweet_list = browser.find_elements_by_xpath("(//*[@class='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text'])"
                                                "[position()>%d and position()<%d]" % (0,20))
    #browser.execute_script("arguments[0].innerText = '" + text + "'", tweet_list)

    for i in tweet_list:
        browser.execute_script("arguments[0].innerText = '" + text + "'", i)


    html = browser.page_source
    Html_file = open("sourcepage.html", "w")
    Html_file.write(str(html.encode("utf-8")))
    Html_file.close()
    return html

#main
#if __name__ == "__main__":
#    list = tweet_scroller(url, 'shit')