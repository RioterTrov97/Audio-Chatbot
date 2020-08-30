import webbrowser
import main
import speaker
import recorder

def google_search(q):
    try:
        if main.person_says (["on google"]):
            if main.person_says(["of"]):
                search = main.voice_data.split("of")[-1]
                search_term = " ".join(search.split("on google") [0:])
            elif main.person_says(["for"]):
                search = main.voice_data.split("for")[-1]
                search_term = " ".join(search.split("on google") [0:])
            else:
                if main.person_says(["search"]):
                    search = main.voice_data.split("search")[-1]
                    search_term = " ".join(search.split("on google") [0:])
                else:
                    search = " ".join(main.voice_data.split(" ")[0:])
                    search_term = " ".join(search.split("on google") [0:])
        elif main.person_says (["in google"]):
            if main.person_says(["of"]):
                search = main.voice_data.split("of")[-1]
                search_term = " ".join(search.split("in google") [0:])
            elif main.person_says(["for"]):
                search = main.voice_data.split("for")[-1]
                search_term = " ".join(search.split("in google") [0:])
            else:
                if main.person_says(["search"]):
                    search = main.voice_data.split("search")[-1]
                    search_term = " ".join(search.split("in google") [0:])
                else:
                    search = " ".join(main.voice_data.split(" ")[0:])
                    search_term = " ".join(search.split("in google") [0:])
        else:
            if main.person_says(["of"]):    
                search_term = main.voice_data.split("of")[-1]
                search_term = search_term.replace('google', ' ')
            elif main.person_says(["for"]):
                search_term = main.voice_data.split("for")[-1]
                search_term = search_term.replace('google', ' ')
            else:
                if main.person_says(["search"]):
                    search = main.voice_data.split("search")[-1]
                    search_term = " ".join(search.split(" ") [0:])
                    search_term = search_term.replace('google', ' ')
                else:
                    search_term = main.voice_data.split(" ")[0:]
                    search_term = search_term.replace('google', ' ')
        
        if search_term != '':
            google_url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(google_url)
            q.put(main.asis_obj.name + ": " + "Here is what I found for " + search_term + " on google" + "\n")
            speaker.speech_output("Here is what I found for " + search_term + " on google")
        else:
            speaker.speech_output("Sorry, I got confused in your search query. For example, you can ask me 'search for politics on google'")
    except Exception:
            speaker.speech_output("Sorry, I did not understand what search you wanted. For example, you can ask me 'search for politics on google'")

def youtube_search(q):
    try:
        if main.person_says (["on youtube"]):
            if main.person_says(["of"]):
                search = main.voice_data.split("of")[-1]
                search_term = " ".join(search.split("on youtube") [0:])
            elif main.person_says(["for"]):
                search = main.voice_data.split("for")[-1]
                search_term = " ".join(search.split("on youtube") [0:])
            elif main.person_says(["play"]):
                search = main.voice_data.split("play")[-1]
                search_term = " ".join(search.split("on youtube") [0:])
            else:
                if main.person_says(["search"]):
                    search = main.voice_data.split("search")[-1]
                    search_term = " ".join(search.split("on youtube") [0:])
                else:
                    search = " ".join(main.voice_data.split(" ")[0:])
                    search_term = " ".join(search.split("on youtube") [0:])

        elif main.person_says (["in youtube"]):
            if main.person_says(["of"]):
                search = main.voice_data.split("of")[-1]
                search_term = " ".join(search.split("in youtube") [0:])
            elif main.person_says(["for"]):
                search = main.voice_data.split("for")[-1]
                search_term = " ".join(search.split("in youtube") [0:])
            elif main.person_says(["play"]):
                search = main.voice_data.split("play")[-1]
                search_term = " ".join(search.split("in youtube") [0:])
            else:
                if main.person_says(["search"]):
                    search = main.voice_data.split("search")[-1]
                    search_term = " ".join(search.split("in youtube") [0:])
                else:
                    search = " ".join(main.voice_data.split(" ")[0:])
                    search_term = " ".join(search.split("in youtube") [0:])
        else:
            if main.person_says(["of"]):    
                search_term = main.voice_data.split("of")[-1]
                search_term = search_term.replace('youtube', ' ')
            elif main.person_says(["for"]):
                search_term = main.voice_data.split("for")[-1]
                search_term = search_term.replace('youtube', ' ')
            else:
                if main.person_says(["search"]):
                    search = main.voice_data.split("search")[-1]
                    search_term = " ".join(search.split(" ") [0:])
                    search_term = search_term.replace('youtube', ' ')
                else:
                    search = " ".join(main.voice_data.split(" ")[0:])
                    search_term = " ".join(search.split(" ") [0:])
                    search_term = search_term.replace('youtube', ' ')
        if search_term != '':        
            url = search_term
            webbrowser.get().open("https://www.youtube.com/results?search_query=" + url)
            q.put(main.asis_obj.name + ": " + "Here is what I found for " + search_term + " on youtube" + "\n")
            speaker.speech_output("Here is what I found for " + search_term + " on youtube")
            ask_playback(url,q)
        else:
            speaker.speech_output("Sorry, I got confused in your search query. For example, you can ask me 'search for banana on youtube'")
    except Exception:
            speaker.speech_output("Sorry, I did not understand what search you wanted. For example, you can ask me 'search for politics on youtube'")

def price_search(q):
    try:
        if main.person_says (["on google"]):
            if main.person_says(["of"]):
                search = main.voice_data.split("of")[-1]
                search_term = " ".join(search.split("on google") [0:])
                search_term = search_term.replace('price', ' ')
            elif main.person_says(["for"]):
                search = main.voice_data.split("for")[-1]
                search_term = " ".join(search.split("on google") [0:])
                search_term = search_term.replace('price', ' ')
            else:
                if main.person_says(["search"]):
                    search = main.voice_data.split("search")[-1]
                    search_term = " ".join(search.split("on google") [0:])
                    search_term = search_term.replace('price', ' ')
                else:
                    search = " ".join(main.voice_data.split(" ")[0:])
                    search_term = " ".join(search.split("on google") [0:])
                    search_term = search_term.replace('price', ' ')
        elif main.person_says (["in google"]):
            if main.person_says(["of"]):
                search = main.voice_data.split("of")[-1]
                search_term = " ".join(search.split("in google") [0:])
                search_term = search_term.replace('price', ' ')
            elif main.person_says(["for"]):
                search = main.voice_data.split("for")[-1]
                search_term = " ".join(search.split("in google") [0:])
                search_term = search_term.replace('price', ' ')
            else:
                if main.person_says(["search"]):
                    search = main.voice_data.split("search")[-1]
                    search_term = " ".join(search.split("in google") [0:])
                    search_term = search_term.replace('price', ' ')
                else:
                    search = " ".join(main.voice_data.split(" ")[0:])
                    search_term = " ".join(search.split("in google") [0:])
                    search_term = search_term.replace('price', ' ')
        else:
            if main.person_says(["of"]):    
                search_term = main.voice_data.split("of")[-1]
                search_term = search_term.replace('price', ' ')
            elif main.person_says(["for"]):
                search_term = main.voice_data.split("for")[-1]
                search_term = search_term.replace('price', ' ')
            else:
                if main.person_says(["search"]):
                    search = main.voice_data.split("search")[-1]
                    search_term = " ".join(search.split(" ") [0:])
                    search_term = search_term.replace('price', ' ')
                else:
                    search_term = main.voice_data.split(" ")[0:]
                    search_term = search_term.replace('price', ' ')
        
        if search_term != '':
            google_url = "https://google.com/search?q=" + "price+"+ "of+" + search_term
            webbrowser.get().open(google_url)
            q.put(main.asis_obj.name + ": " + "Here is what I found for price of " + search_term + " on google" + "\n")
            speaker.speech_output("Here is what I found for price of " + search_term + " on google")
        else:
            q.put(main.asis_obj.name + ": " + "Sorry, I got confused in your search query. For example, you can ask me 'search for price of banana'" + "\n")
            speaker.speech_output("Sorry, I got confused in your search query. For example, you can ask me 'search for price of banana'")
    except Exception:
            q.put(main.asis_obj.name + ": " + "Sorry, I did not understand what search you wanted. For example, you can ask me 'search for price of banana'" + "\n")
            speaker.speech_output("Sorry, I did not understand what search you wanted. For example, you can ask me 'search for price of banana'")

def display_ip():
    import requests
    """  Function To Print GeoIP Latitude & Longitude """
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    my_ip = ip_request.json()['ip']
    geo_request = requests.get('https://get.geojs.io/v1/ip/geo/' +my_ip + '.json')
    geo_data = geo_request.json()
    location = geo_data['city']
    return location

def weather_search(q):
        search_term = display_ip()
        url = "https://google.com/search?q=" + "weather+"+ "of+" + search_term
        webbrowser.get().open(url)
        q.put(main.asis_obj.name + ": " + "Here is what I found about weather on " + search_term + "\n")
        speaker.speech_output("Here is what I found about weather on " + search_term)

def definitions(q):
        import recorder
        if main.person_says(["what is"]) and 'definition' not in main.voice_data and 'definitions' not in main.voice_data:
            search_term = main.voice_data.split("what is")[-1]
            search_term = search_term.replace('is', ' ')
            wiki_search(search_term, q)
        elif main.person_says(["definition of", "definitions of"]):
            search_term = main.voice_data.split("of")[-1]
            wiki_search(search_term, q)
        elif main.person_says(["definition for", "definitions for"]):
            search_term = main.voice_data.split("for")[-1]
            wiki_search(search_term, q)
        else:
            definition=recorder.record_audio("What do you need the definitions of? Please tell me the word again.")
            search_term = main.voice_data
            wiki_search(search_term, q)
       

def wiki_search(search, q):
        if main.voice_data != "" and search != "":
            import wikipediaapi
            q.put(main.asis_obj.name + ": " + "Give me a few seconds." + "\n")
            speaker.speech_output("Give me a few seconds.")
            wiki_wiki = wikipediaapi.Wikipedia('en')
            page = wiki_wiki.page(search)
            if page.exists():
                summary = page.summary
                definition = summary.split(".") [0]
                q.put(main.asis_obj.name + ": " + definition + ".\n")
                speaker.speech_output(definition)
            else:
                q.put(main.asis_obj.name + ": " + "Sorry, I believe that is a made up word." + "\n")
                speaker.speech_output("Sorry, I believe that is a made up word.")
                main.main_page()
        else:
            q.put(main.asis_obj.name + ": " + "Sorry I did not get what definition you want. Please ask again." + "\n")
            speaker.speech_output("Sorry I did not get what definition you want. Please ask again.")
            main.main_page()

def ask_playback(urls, q):
    url = str(urls)
    main.voice_data = recorder.record_audio("Let me know if you like me to play any video from the search results?",q)
    #print("Voice data is: " + str(main.voice_data))
    if main.person_says(["first", "1", "one", "1st", "start", "yes", "sure", "yep", "yeah", "any", "play"]):
            watchvideo(url, 0, q)
    elif main.person_says(["second", "2", "two", "2nd"]):
            watchvideo(url, 1, q)
    elif main.person_says(["third", "3", "three", "3rd"]):
            watchvideo(url, 2, q)
    elif main.person_says(["fourth", "4", "four", "4th"]):
            watchvideo(url, 3, q)
    elif main.person_says(["fifth", "5", "five", "5th"]):
            watchvideo(url, 4, q)
    elif main.person_says(["sixth", "6", "six", "6th"]):
            watchvideo(url, 5, q)
    elif main.person_says(["seventh", "7", "seven", "7th"]):
            watchvideo(url, 6, q)
    elif main.person_says(["eighth", "8", "eight", "8th"]):
            watchvideo(url, 7, q)
    elif main.person_says(["ninth", "9", "nine", "9th"]):
            watchvideo(url, 8, q)
    elif main.person_says(["tenth", "10", "ten", "10th"]):
            watchvideo(url, 9, q)
    elif main.person_says(["eleventh", "11", "eleven", "11th"]):
            watchvideo(url, 10, q)
    elif main.person_says(["No", "nope", "sorry", "Nah", "quit"]):
            q.put(main.asis_obj.name + ": " + "Okay!" + "\n")
            speaker.speech_output("Okay!")
    else:
            q.put(main.asis_obj.name + ": " + "Sorry, I could not grasp what you meant." + "\n")
            speaker.speech_output("Sorry, I could not grasp what you meant.")


def watchvideo(url, num, q):
    try:
        try:
            from selenium import webdriver
            from selenium.webdriver.common.by import By
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC
            n = int(num)
            #print("Video number: " + str(n + 1))
            #print("URL: " + str(url))
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            options.add_argument('headless')
            options.add_argument("disable-infobars")
            options.add_argument("--disable-extensions")
            driver=webdriver.Chrome(options=options, executable_path=r'chromedriver.exe', service_log_path='NUL')
            q.put(main.asis_obj.name + ": " + "Give me a few seconds." + "\n")
            speaker.speech_output("Give me a few seconds.")
            driver.get("https://www.youtube.com/results?search_query=" + url)
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#search"))).send_keys("Python")
            driver.find_element_by_css_selector("button.style-scope.ytd-searchbox#search-icon-legacy").click()
            videos =[my_href.get_attribute("href") for my_href in WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "a.yt-simple-endpoint.style-scope.ytd-video-renderer#video-title")))]
            driver.quit()
    
            #print("Video address:" + str(videos[n]))
            webbrowser.get().open(videos[n])
        except:
            q.put(main.asis_obj.name + ": " + "Give me a few seconds." + "\n")
            speaker.speech_output("Give me a few seconds.")
            from youtube_search import YoutubeSearch

            results = YoutubeSearch(url).to_dict()
            address =[ d.get('url_suffix', None) for d in results]
            webbrowser.get().open("www.youtube.com" + str(address[num]))

    except Exception:
        q.put(main.asis_obj.name + ": " + "Sorry, I could not process your request." + "\n")
        speaker.speech_output("Sorry, I could not process your request.")
