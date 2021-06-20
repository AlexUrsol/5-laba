import pika 
import time 
 
connection = pika.BlockingConnection( 
    pika.ConnectionParameters(host='localhost')) 
channel = connection.channel() 
 
 
channel.queue_declare(queue='persistent_queue', durable=True) 
 
 
 
for i in range(10): 
    time.sleep(1) 
    msg = f'msg{i}' 
    print(f'[x] Sent {msg}') 
    channel.basic_publish(exchange='', routing_key='persistent_queue', body=msg, properties=pika.BasicProperties(delivery_mode=2)) 
connection.close() 