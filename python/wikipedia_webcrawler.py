import time, requests, bs4

def continue_crawl(search_history, target_url, max_steps=25):
    # Procedure implements function that continues or break main code execution based on set of parameters
    if search_history[-1]==target_url:
        print('The crawl has reached philosophy article')
        return False
    elif search_history [-1] in search_history[:-2]:
        print('The crawl has entered infinite loop')
        return False
    elif len(search_history) > max_steps:
        print('The crawl has reached maximum iterative function')
        return False
        # elif link in page:
        #   print('The crawler has found no active links on a page: '+str(target_url))
        #  return False
    else:
        print('continue')
        return True

def find_first_link (current_article):
    # return the first link as a string, or return None if there is no link
    # get the HTML from "url", use the requests library and feed the HTML into Beautiful Soup
    response = requests.get(current_article)
    html=response.text
    soup=bs4.BeautifulSoup(html, "html.parser")

    # finding the first link in the article
    # return the first link as a string
    # or set return to None if there is no link in the article.

    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    for element in content_div.find_all("p", recursive=False):
            if element.find("a", recursive=False):
                first_relative_link = element.find("a", recursive=False).get('href')
                break

    #article_link = soup.find(id='mw-content-text').find(class_="mw-parser-output").p.a.get('href')
    article_link = 'https://en.wikipedia.org'+first_relative_link
    print (article_link)
    return article_link

def web_crawl(first_article, target_url='https://en.wikipedia.org/wiki/Philosophy'):
    # Main Body of the Web-Crawler
    article_chain=[first_article]
    while continue_crawl(article_chain, target_url):
        # Open an article and download html of last article in article_chain
        # find the first link in that html
        first_link = find_first_link(article_chain[-1])
        if first_link == None:
            break
        else:
            # add the first link to article_chain
            article_chain.append(first_link)
            # delay for about two seconds
        time.sleep(1)
        # Follow the link

# Execution code
first_article='https://en.wikipedia.org/wiki/Special:Random'
target_url='https://en.wikipedia.org/wiki/Philosophy'
print (web_crawl(first_article, target_url))

