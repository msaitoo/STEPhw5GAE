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
            
route = []
michi = []
def find_all_possible_Route(start, end, MAP, route=[]):
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

michi = find_all_possible_Route('Pallet Town', 'Celadon City', MAP, route)
path = findRoute(michi)
#print ans
#print len(ans)