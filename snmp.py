from easysnmp import Session
#https://easysnmp.readthedocs.io/en/latest/index.html
session = Session(hostname='127.0.0.1', community='public', version=2)
oid = {'sys':'.1.3.6.1.2.1.1.1.0'}
result = {}
for k in oid:
        result[k] = session.get(oid[k]).value
print(result)