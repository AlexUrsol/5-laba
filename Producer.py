import pika 
import time 
 
connection = pika.BlockingConnection( 
    pika.ConnectionParameters(host='localhost')) 
channel = connection.channel()
channel.queue_declare(queue='hello') 
 
for i in range(10): 
    time.sleep(1) 
    msg = f'msgProducer{i}' 
    print(f'[x] Sent {msg}') 
    channel.basic_publish(exchange='', routing_key='hello', body=msg) 
connection.close() 