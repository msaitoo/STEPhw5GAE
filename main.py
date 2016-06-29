#!/usr/bin/env python
# -*- coding: utf-8 -*-
import webapp2

html = '''
<!doctype html>
<html lang = "en">
    <head>
        <meta charset = "utf = 8"/>
        <title> Form </title>
    </head>
    <body>
        <hl> Give two words to shuffle! </hl>
        <form method = "post">
            <label for = "firstWord"> First Word: </label>
            <input name = "firstWord" type = "text" value = ""><br>
            
            <label for = "secondWord"> Second Word: </label>
            <input name = "secondWord" type = "text" value = ""><br>
            
            <input name = "" type = "submit" value = "Submit">
        </form>
    </body>
</html>
'''

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(html)
    
    def post(self):
        firstWord = self.request.get("firstWord")
        secondWord = self.request.get("secondWord")
        word = ""
        for i in range(max(len(firstWord), len(secondWord))):
            if i <= len(firstWord)-1:
                word += firstWord[i]
            if i <= len(secondWord)-1:
                word += secondWord[i]
        self.response.out.write(word)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
