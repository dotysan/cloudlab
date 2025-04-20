#! /usr/bin/env python2.7
""" Hello World, in CloudLab.

Instructions:
Wait for the profile instance to start, then click on the node in the topology and choose the `shell` menu item. 
"""
# tell vscode to not give a shit about Pylance(reportShadowedImports) on 'profile'
# type: ignore
# TODO: how can we remove this?

# packages
from geni import portal

pc = portal.Context()
r = pc.makeRequestRSpec()

ubuntu24 = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU24-64-STD'

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
