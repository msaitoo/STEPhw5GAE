# -*- coding: utf-8 -*-
#!/usr/bin/env python
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('''
        Welcome! <br>
        Continue to:<br>
        <A HREF="http://localhost:9999/shuffle">SHUFFLE</A>
        to shuffle two words. <br>
        <A HREF="http://localhost:9999/route">ROUTE</A>
        to get routes to take in Kanto Region (Pokemon gen 1).
        ''')

class Shuffle(webapp2.RequestHandler):
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
    def get(self):
        self.response.write(self.html)
    
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

class Route(webapp2.RequestHandler):
    MAP = { 'Pallet Town'    : ['Viridian City', 'Cinnibar Island'],
            'Viridian City'  : ['Pallet Town', 'Pewter City'],
            'Pewter City'    : ['Viridian City', 'Cerulean City'],
            'Cerulean City'  : ['Pewter City', 'Saffron City', 'Lavender Town'],
            'Lavender Town'  : ['Cerulean City', 'Saffron City', 'Vermillion City', 'Fuschia City'],
            'Saffron City'   : ['Cerulean City', 'Lavender Town', 'Vermillion City', 'Celadon City'],
            'Celadon City'   : ['Saffron City', 'Fuschia City'],
            'Vermillion City': ['Saffron City', 'Lavender Town', 'Fuschia City'],
            'Fuschia City'   : ['Celadon City', 'Vermillion City', 'Lavender Town', 'Cinnibar Island'],
            'Cinnibar Island': ['Pallet Town','Fuschia City' ]}
    
    html = '''
    <!doctype html>
    <html lang = "en">
        <head>
            <meta charset = "utf = 8"/>
            <title> Form </title>
        </head>
        <body>
            <hl> Choose towns/cities you want to travel between! </hl>
            <br>
            <form method = "post">
                <label for = "start"> Leaving: </label>
                    <select name = "start">
                        <option value="Pallet Town">Pallet Town</option>
                        <option value="Viridian City">Viridian City</option>
                        <option value="Pewter City">Pewter City</option>
                        <option value="Cerulean City">Cerulean City</option>
                        <option value="Lavender Town">Lavender Town</option>
                        <option value="Saffron City">Saffron City</option>
                        <option value="Celadon City">Celadon City</option>
                        <option value="Fuschia City">Fuschia City</option>
                        <option value="Vermillion City">Vermillion City</option>
                        <option value="Cinnibar Island">Cinnibar Island</option>
                    </select>
                <br>
                <label for = "end"> Destination: </label>
                    <select name = "end">
                        <option value="Pallet Town">Pallet Town</option>
                        <option value="Viridian City">Viridian City</option>
                        <option value="Pewter City">Pewter City</option>
                        <option value="Cerulean City">Cerulean City</option>
                        <option value="Lavender Town">Lavender Town</option>
                        <option value="Saffron City">Saffron City</option>
                        <option value="Celadon City">Celadon City</option>
                        <option value="Fuschia City">Fuschia City</option>
                        <option value="Vermillion City">Vermillion City</option>
                        <option value="Cinnibar Island">Cinnibar Island</option>
                    </select>
                <br>
                <input name = "" type = "submit" value = "Submit">
                <br>
                <br>
                <label for = "item"> Item: </label>
                    <select name = "item">
                        <option value="Bicycle">Bicycle</option>
                        <option value="Water">Water type Pokemon</option>
                        <option value="Flying">Flying type Pokemon</option>
                        <option value="Ground">Ground type Pokemon</option>
                        <option value="Flash">Pokemon with 'flash'</option>
                <br>
            </form>
        </body>
    </html>
    '''
    
    def find_all_possible_Route(start, end, MAP, route, self):
        route = route + [start]
        if start == end:
            michi.append(route)
        else:
            for path in MAP[start]:
                if path not in route:
                    newpath = find_all_possible_Route(path, end, MAP, route)
        return michi
    
    def findRoute(michi):
        shortPath = []
        minlen = len(min(michi))
        for routes in michi:
            if len(routes) == minlen:
                shortPath.append(routes)
        return shortPath
    
    def get(self):
        self.response.write(self.html)
    
    def post(self):
        start = self.request.get("start")
        end = self.request.get("end")
        MAP = self.MAP
        route = []
        michi = []
        possibilities = self.find_all_possible_Route(start, end, MAP, route)
        short = self.findRoute(possibilities)
        self.response.write(short)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/shuffle', Shuffle),
    ('/route', Route),
], debug=True)