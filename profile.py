#! /usr/bin/env python2.7
""" Hello World, in CloudLab.

Instructions:
Wait for the profile instance to start.
Then click on the node in the topology and choose the `shell` menu item.Happy experimenting!
"""
# tell vscode to not give a shit about Pylance(reportShadowedImports) about replacing stdlib profile module
# type: ignore
# TODO: how can we remove this?

# stdlib
try:
    from typing import List, Any  # available via pip install typing for Python 2.7
except ImportError:
    pass

# packages
from geni import portal
from geni.rspec import (
    # emulab,
    pg,
)

# local
from images import ubuntu24


def main():  # type: () -> None
    """ Main entry point to define experiment configuration. """

    pc = portal.Context()
    params = define_parameters(pc)
    r = pc.makeRequestRSpec()

    pnodes = add_phy_nodes(r, params.node_type)
    vnodes = add_virt_nodes(r, params.count)

    # links =
    create_links(r, pnodes + vnodes)

    # output the RSpec XML
    pc.printRequestRSpec()


def define_parameters(pc):  # type: (portal.Context) -> Any
    """ Define and bind user parameters for this experiment. """

    pc.defineParameter(name='node_type',
                       description='Node Type',
                       typ=portal.ParameterType.STRING,
                       defaultValue='c6525-25g',
                       longDescription='Specify the physical node hardware type.')
    pc.defineParameter(name='count',
                       description='Number of VMs',
                       typ=portal.ParameterType.INTEGER,
                       defaultValue=3,
                       longDescription='How many VMs to create.')

    return pc.bindParameters()


def add_phy_nodes(req, node_type):  # type: (pg.Request, str) -> List[pg.RawPC]
    """ Create and return a list of physical nodes with configuration. """

    pnode1 = req.RawPC('pnode1')
    pnode1.disk_image = ubuntu24
    pnode1.hardware_type = node_type

    # why are these run on every boot?
    exec_svc = pg.Execute(shell='sh', command='sudo /local/repository/ubuntu-min.sh')
    pnode1.addService(exec_svc)

    return [pnode1]


def add_virt_nodes(req, count):  # type: (pg.Request, int) -> List[pg.XenVM|pg.DockerContainer]
    """ Create and return a list of virtual nodes (Xen and Docker). """

    vnodes = [
        req.XenVM("vnode{}".format(i))
        for i in range(1, count + 1)
    ]

    # dnode1 = r.DockerContainer(client_id='dnode1')

    return vnodes  # + [dnode1] + dnodes


def create_links(r, nodes):  # type: (Any, Any) -> List[Any]
    """ Create and return a list of network links between given nodes. """

    link1 = r.Link(name='link1', members=nodes)

    return [link1]


if __name__ == '__main__':
    main()
