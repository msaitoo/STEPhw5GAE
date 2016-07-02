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
            

def findpaths(start, end, MAP, item):
    route = []
    michi = []
    def find_all_possible_Routes(start, end, MAP, route=[]):
        route = route + [start]
        if start == end:
            michi.append(route)
        else:
            for path in MAP[start]:
                if path not in route:
                    newpath = find_all_possible_Routes(path, end, MAP, route)
        
        return michi
    
    def findRoute(michi):
        shortPath = []
        keiyu = []
        for i in range(len(michi)):
            keiyu.append(len(michi[i]))
        minlen = min(keiyu)
        for routes in michi:
            if len(routes) == minlen:
                shortPath.append(routes)
        return shortPath
    michi = find_all_possible_Routes(start, end, MAP, route)
    path = findRoute(michi)
    

        #shortestroutes = []
        #if item != 'Water type Pokemon':
            #if item == 'Flying type Pokemon':
                #print end
            #for i in range(len(path)):
                #if 'Cinnibar Island' not in path[i]:
                    #shortestroutes.append(path[i])
        #else:
            #shortestroutes = path
        #return shortestroutes
    
    if item == 'Flying type Pokemon':
        print "You can fly straight to {}!!! Or take routes as following:".format(end)
        
    for i in range(len(path)):
        if 'Cinnibar Island' in path[i]:
            if item != 'Water type Pokemon':
                print 'Please take a water type Pokemon with you to take the route {}'.format(path[i])
    return path

#print "Start:"
#start = raw_input()
#print "End:"
#end = raw_input()
#print "item"
#item = raw_input()

#path = findpaths(start, end, MAP, item)
#if len(path) == 1:
    #print "Here is the shortest route to {}".format(path[-1][-1])
#else:
    #print "Here are {} shortest routes to {}".format(len(path),path[-1][-1])

#print path