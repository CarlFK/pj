# pj.py
# dump some netmasky stuff to confirm I wired things up the way I wanted.

import argparse

from operator import itemgetter, attrgetter, methodcaller
from pprint import pprint

from kicad_parser import KicadPCB


def get_net(filename, start,end, verbose):

    net = KicadPCB.load(filename)

    l=[]

    for i in range(start,end):

        n = net.nets.net[i]
        d = {
                'code' : eval(n.code),
                'name' : eval(n.name)[1:],
                'pico' : { 'name': eval(n.node[0].pinfunction), 'pin' : eval(n.node[0].pin) },
                'index' : int(eval(n.node[0].pin)),
                'pi' : { 'name': eval(n.node[1].pinfunction), 'pin' : eval(n.node[1].pin) },
                }
        if verbose: pprint(d)
        l.append(d)

        if verbose: pprint(l)

    return l


def sort_net(l, key):
    l=sorted(l,key=itemgetter( key ) )
    return l

def wiki_rows(l):

    for i in l:
        # print(" | ".join([i['name'], i['pi']['name'][3:], i['pi']['pin'], i['pico']['pin'], i['pico']['name'][4:]]))
        print(" | ".join([i['name'], i['pi']['name'], i['pi']['pin'], i['pico']['pin'], i['pico']['name']]))


def get_args():

    parser = argparse.ArgumentParser(
            description="KiCad netlist thing")

    parser.add_argument('range',
            help='start end netlist range',
            nargs='+',
            type=int,
            )

    parser.add_argument('--filename',
            help='input filename',
            nargs='?',
            default='../project/pj.net',
            )

    parser.add_argument('-k', '--key',
            help='key to sort on',
            default='index',
            )

    parser.add_argument('-t', '--test', help="run test(s)", action="store_true")
    parser.add_argument('-v', '--verbose', action="store_true")

    args = parser.parse_args()

    return args


def main():
    args = get_args()

    net = get_net(args.filename, args.range[0], args.range[1], args.verbose)
    net = sort_net(net, args.key)

    wiki_rows(net)


if __name__=='__main__':
    main()


