class Url:
    def __init__(self):
        self.link = None
        self.prev = None
        self.foward = None

class BrowserHistory:
    def __init__(self):
        self.link = None
        self.url_i = Url() 
        self.links = {}
    def get_current_url(self):
        if self.url_i is None:
            return None
        return self.url_i.link
    def go_to(self,URL):
        URL = Url()
        self.links[URL.link] = URL.link
        return URL.link
    def back(self):
        if self.url_i.prev is None:
            return None
        return self.url_i.prev
    def foward(self):
        if self.url_i.foward is None:
            return None
        return self.url_i.foward
    def jump_to(self,URL):
        URL = Url()
        if URL.link not in self.links:
            return("URL has not been visited before")
        elif URL.link in self.links:
            self.url_i = URL
            return URL.link
            
