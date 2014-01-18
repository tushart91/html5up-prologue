import webapp2

class IndexHandler(webapp2.RequestHandler):
    def get(self):
        if self.request.url.endswith('/'):
            path = '%sindex.html'%self.request.url
        else:
            path = '%s/index.html'%self.request.url

        self.redirect(path)

    def post(self):
        self.get()

application = webapp2.WSGIApplication([('/', IndexHandler)],
                                         debug=False)
