import pika 
import time 
 
connection = pika.BlockingConnection( 
    pika.ConnectionParameters(host='localhost')) 
channel = connection.channel() 
 
channel.queue_declare(queue='limit', arguments={'x-max-length': 5}) 
#channel.queue_declare(queue='limit_reject', arguments={'x-max-length': 5,  'x-overflow': 'reject-publish'})

 
 
for i in range(10): 
    time.sleep(1) 
    msg = f'msg{i}' 
    print(f'[x] Sent {msg}') 
    channel.basic_publish(exchange='', routing_key='limit', body=msg) 
connection.close() 