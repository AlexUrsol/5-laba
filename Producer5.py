import pika 
import time 
 
connection = pika.BlockingConnection( 
    pika.ConnectionParameters(host='localhost')) 
channel = connection.channel() 
 
channel.queue_declare(queue='ack_queue1') 
 
 
 
for i in range(10): 
    time.sleep(2) 
    msg = f'msg{i}' 
    print(f'[x] Sent {msg}') 
    channel.basic_publish(exchange='', routing_key='ack_queue1', body=msg)
time.sleep(100)
connection.close() 