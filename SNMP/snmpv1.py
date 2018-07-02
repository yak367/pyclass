from snmp_helper import snmp_get_oid,snmp_extract

COMMUNITY_STRING = 'galileo'
SNMP_PORT = 161
IP1 = '184.105.247.70'
IP2 = '184.105.247.71' 

OID1 = '1.3.6.1.2.1.1.5.0'
OID2 = '1.3.6.1.2.1.1.1.0'

a_device = (IP1, COMMUNITY_STRING, SNMP_PORT)
b_device = (IP2, COMMUNITY_STRING, SNMP_PORT)


for device in (a_device, b_device):
    print ("\n**********************")
    for the_oid in (OID1, OID2):
        snmp_data = snmp_get_oid (device, oid=the_oid)
        output = snmp_extract (snmp_data) 
        print output   
    print ("\n**********************")
 


