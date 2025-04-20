#! /usr/bin/env python2.7
""" Hello World, in CloudLab.

Instructions:
Wait for the profile instance to start. Then click on the node in the topology and choose the `shell` menu item. Happy experimenting!
"""
# tell vscode to not give a shit about Pylance(reportShadowedImports) on 'profile'
# type: ignore
# TODO: how can we remove this?

# packages
from geni import portal

# local
from images import ubuntu24

pc = portal.Context()
r = pc.makeRequestRSpec()

#----------------------------------------------------------------------
# Physical Nodes

pnode1 = r.RawPC('pnode1')
pnode1.disk_image = ubuntu24
pnode1.hardware_type='c6525-25g'

#======================================================================

def main():  # -> None:
    """"""

    # output the RSpec XML
    pc.printRequestRSpec()

if __name__ == '__main__':
   main()
