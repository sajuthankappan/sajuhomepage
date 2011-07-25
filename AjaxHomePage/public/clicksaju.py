import os
from google.appengine.ext.webapp import template

import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

class Greeting(db.Model):
    author = db.UserProperty()
    content = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)

class MainPage(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, {}))

class Home(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'home.html')
        self.response.out.write(template.render(path, {}))

class Linux(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'linux.html')
        self.response.out.write(template.render(path, {}))

class Videos(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'videos.html')
        self.response.out.write(template.render(path, {}))

class UbuntuNewUserTips(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'ubuntunewusertips.html')
        self.response.out.write(template.render(path, {}))

class Chess(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'chess.html')
        self.response.out.write(template.render(path, {}))

class PowerBuilder(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'powerbuilder.html')
        self.response.out.write(template.render(path, {}))

class Links(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'links.html')
        self.response.out.write(template.render(path, {}))

class Mobile(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'mobile.html')
        self.response.out.write(template.render(path, {}))

class Mobile2(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'mobile2.html')
        self.response.out.write(template.render(path, {}))

class MobileDialog(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'mobiledialog.html')
        self.response.out.write(template.render(path, {}))

class Friends(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'friends.html')
        self.response.out.write(template.render(path, {}))

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/home.html', Home),
                                      ('/friends.html', Friends),
                                      ('/videos.html', Videos),
                                      ('/linux.html', Linux),
                                      ('/ubuntunewusertips.html', UbuntuNewUserTips),
                                      ('/chess.html', Chess),
                                      ('/powerbuilder.html', PowerBuilder),
                                      ('/links.html', Links),
                                      ('/mobile.html', Mobile),
                                      ('/mobile2.html', Mobile2),
                                      ('/mobiledialog.html', MobileDialog)
                                     ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
