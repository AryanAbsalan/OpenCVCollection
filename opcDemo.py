from opcua import Server
from opcua import Client
import datetime
import time
import check_file_change
import read_from_file
import save_file
from opcua import ua
from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaError
import msgpack
from asn1crypto._ffi import null
import save_file

machinestate = "False"
bActivateDemo = []
rActualPosition = 'null'
rActualVelocity = 'null'
rActualTorqueForce = 'null'
oneData = (1,'null','null','null','null')
transaction = []
machinetime = 'null'
numTransaction= 0
numData = 0

class SubScriptionHandler(object):
#set handler for client, so thant we can new a handler for later use (for each data subscription).
# here i've wrote some function to process data, i.e. save data to Apache-Kafka.
# The code here is written according to requirements, but "def datachange_notification(self, node, val, data):" is needed anyway.
# So you can ignore the code inside "def datachange_notification(self, node, val, data):"
    def datachange_notification(self, node, val, data):
        str(val)
        def setmachinestate(ms):
            global machinestate
            global bActivateDemo
            machinestate = ms
        def setrActualPosition(ap):
            global rActualPosition
            rActualPosition = ap        
        def setrActualVelocity(av):
            global rActualVelocity
            rActualVelocity = av     
        def setrActualTorqueForce(atf):
            global rActualTorqueForce
            rActualTorqueForce = atf 
        def setOneData():
            global rActualPosition
            global rActualVelocity
            global rActualTorqueForce
            global machinetime
            global transaction
            oneData = (1,machinetime,rActualPosition,rActualVelocity,rActualTorqueForce)
            transaction.append(oneData)
            rActualPosition='null'
            rActualVelocity='null'
            rActualTorqueForce='null'
        def setTime(tm):
            global machinetime
            setOneData()
            machinetime = tm
        def sendTransaction():
            global transaction
            global bActivateDemo
            global numTransaction
            save_file.Savefile().saveTransaction(str(transaction))
            producersourcevalidator = KafkaProducer(bootstrap_servers=['localhost:9092'])
            txns = str(transaction).encode('utf-8')
            numTransaction += 1
            future = producersourcevalidator.send('transaction-topic', txns)
            try:
                record_metadata = future.get(timeout=10)
            except KafkaError:
                log.exception()
                pass
            print("Source was send to 'transaction-topic'", txns)
            transaction.clear()
            print("----------------all buffered data cleared")
            print(time.time())
        if str(node) == "Node(StringNodeId(ns=2;s=Application.PlcProg.bActivateDemo))":
            if str(val) == "True":
                setmachinestate("True")
                print("Maschine started!")
            elif str(val) == "False":
                setmachinestate("False")
                print("Machine stopped!")
        if (machinestate=="True" and
              len(transaction) <= 100):
            if str(node) == "Node(StringNodeId(ns=2;s=Application.PlcProg.rActualPosition))":
                    print("Position updated: ", val)
                    setrActualPosition(val)
            elif str(node) == "Node(StringNodeId(ns=2;s=Application.PlcProg.rActualVelocity))":
                    print("Velocity updated: ",val)
                    setrActualVelocity(val)
            elif str(node) == "Node(StringNodeId(ns=2;s=Application.PlcProg.rActualTorqueForce))":
                    print("TorqueForce updated: ",val)
                    setrActualTorqueForce(val)
            elif str(node) == "Node(StringNodeId(ns=2;s=Application.PlcProg.sysTimeNs))":
                    setTime(val)
                    print('time updated')
        else:
            sendTransaction()



# below is the code of client part, it implemented how to chose a server, and subscribe data from each node of a opcua-server.
if __name__ == "__main__":

#set server url
    url_1 = "opc.tcp://192.168.178.99:4840/"
    try:
#connect to server
        client1= Client(url_1)
        client1.connect()
        print("Connected")
    except:
        print("No Connection with server!")
     
# chose a handler, the handler-class defined over is used here.
    handler = SubScriptionHandler()
    sub1 = client1.create_subscription(1, handler)    

# choose the node of server, which need to be observed.
    node_bActivateDemo = client1.get_node("ns=2;s=Application.PlcProg.bActivateDemo")
    node_rActualPosition = client1.get_node("ns=2;s=Application.PlcProg.rActualPosition")
    node_rActualVelocity = client1.get_node("ns=2;s=Application.PlcProg.rActualVelocity")
    node_rActualTorqueForce = client1.get_node("ns=2;s=Application.PlcProg.rActualTorqueForce")
    node_sysTimeNs = client1.get_node("ns=2;s=Application.PlcProg.sysTimeNs")

# subscribe the data on the node of a opcua-server after it changed.
    handle_1 = sub1.subscribe_data_change(node_bActivateDemo)
    handle_2 = sub1.subscribe_data_change(node_rActualPosition)
    handle_3 = sub1.subscribe_data_change(node_rActualVelocity)
    handle_4 = sub1.subscribe_data_change(node_rActualTorqueForce)
    handle_5 = sub1.subscribe_data_change(node_sysTimeNs)

    