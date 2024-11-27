import asyncio
import sys
# sys.path.insert(0, "..")
import logging
from asyncua import Client, Node, ua

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger('asyncua')

async def main():
    url = 'opc.tcp://127.0.0.1:4840'
    # url = 'opc.tcp://commsvr.com:51234/UA/CAS_UA_Server'
    async with Client(url=url) as client:
        # Client has a few methods to get proxy to UA nodes that should always be in address space such as Root or Objects
        # Node objects have methods to read and write node attributes as well as browse or populate address space
        _logger.info('Children of root are: %r', await client.nodes.root.get_children())

        uri = 'http://examples.freeopcua.github.io'
        idx = await client.get_namespace_index(uri)
        # get a specific node knowing its node id
        # var = client.get_node(ua.NodeId(1002, 2))
        # var = client.get_node("ns=3;i=2002")
        var1 = await client.nodes.root.get_child(["0:Objects", f"{idx}:MyDemoObject1", f"{idx}:MyDemoVariable1"])
        var2 = await client.nodes.root.get_child(["0:Objects", f"{idx}:MyDemoObject2", f"{idx}:MyDemoVariable21"])
        
        # print("My variable1", var1, await var1.read_value())
        # print('Variable1 from Server:', await var1.read_value())
        print("Variable1 from server: {0:.2f}".format(await var1.read_value()))

        # print("My variable2: " ,var1, "{0:.2f}".format(await var21.read_value()))
        print("Variable2 from server: {0:.2f}".format(await var2.read_value()))


if __name__ == '__main__':
    asyncio.run(main())