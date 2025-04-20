#! /usr/bin/env python2.7
""" Hello World, in CloudLab.

Instructions:
Wait for the profile instance to start. Then click on the node in the topology and choose the `shell` menu item. Happy experimenting!
"""
# tell vscode to not give a shit about Pylance(reportShadowedImports) about replacing stdlib profile module
# type: ignore
# TODO: how can we remove this?

# packages
from geni import portal
from geni.rspec import (
    # emulab,
    pg,
)

# local
from images import ubuntu24

pc = portal.Context()
pc.defineParameter(name="node_type",
                   description="Node Type",
                   typ=portal.ParameterType.STRING,
                   defaultValue="c6525-25g",
                   longDescription="Specify the node hardware type.")
params = pc.bindParameters()

#----------------------------------------------------------------------

r = pc.makeRequestRSpec()

#----------------------------------------------------------------------
# Physical Nodes

pnode1 = r.RawPC('pnode1')
pnode1.disk_image = ubuntu24
pnode1.hardware_type = params.node_type

# why are these run on every boot?
exec_svc = pg.Execute(shell='sh', command='sudo /local/repository/ubuntu-min.sh')
pnode1.addService(exec_svc)

#----------------------------------------------------------------------
# Virtual Nodes

# foo = r.DockerContainer('foo')
# foo = emulab.DockerContainer('foo')

#======================================================================

def main():  # -> None:
    """main()"""

    # output the RSpec XML
    pc.printRequestRSpec()

if __name__ == '__main__':
   main()
