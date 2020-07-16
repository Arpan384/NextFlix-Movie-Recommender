import bs4
import urllib.request as url

def imgScrapper(objs):
    imgSources = dict()
    for i in range(len(objs)):
        # print(objs[i][:-7])
        try:
            # print("Enter")
            key = objs[i][:-7]
            # print(key)
            key = "_".join(key.split(" "))
            # print(key)
            path = "http://en.wikipedia.org/wiki/"+key
            # path =  "https://www.google.com/search?q="+key+"&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiSkc2_hNPjAhVCpY8KHQoKDGIQ_AUIESgB&biw=1920&bih=969"
            http = url.urlopen(path)
            page = bs4.BeautifulSoup(http)
            # img = page.find("img", class_="rg_ic rg_i")
            a = page.find("a", class_="image")
    #         print(a)
            img = a.find("img")
            try:
                src = img.attrs["src"]
            except AttributeError:
                src = img.attrs["alt"]
    #         print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",img)
            imgSources[objs[i]] = src
        except:
            imgSources[objs[i]] = ""
    return imgSources