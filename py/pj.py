# pj.py
# dump some netmasky stuff to confirm I wired things up the way I wanted.

from operator import itemgetter, attrgetter, methodcaller
from pprint import pprint

from kicad_parser import KicadPCB


net = KicadPCB.load('../project/pj.net')

l=[]

for i in range(8,10):

    n = net.nets.net[i]
    d = {
            'code' : eval(n.code),
            'name' : eval(n.name)[1:],
            'pico' : { 'name': eval(n.node[0].pinfunction), 'pin' : eval(n.node[0].pin) },
            'index' : int(eval(n.node[0].pin)),
            'pi' : { 'name': eval(n.node[1].pinfunction), 'pin' : eval(n.node[1].pin) },
            }
    # pprint(d)
    l.append(d)


# pprint(l)
l=sorted(l,key=itemgetter( 'index' ) )

# pprint(l)

for i in l:
    # print(" | ".join([i['name'], i['pi']['name'][3:], i['pi']['pin'], i['pico']['pin'], i['pico']['name'][4:]]))
    print(" | ".join([i['name'], i['pi']['name'], i['pi']['pin'], i['pico']['pin'], i['pico']['name']]))

