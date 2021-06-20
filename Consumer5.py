import pika 
import time 
import re 
 
 
def main(): 
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost')) 
    channel = connection.channel() 
 
    channel.queue_declare(queue='ttl_queue', arguments={'x-message-ttl': 10000}) 

 
    def callback(ch, method, properties, body): 
        print(" [x] Received %r" % body.decode()) 
        # time.sleep(int(re.findall(r'\d+', body.decode())[0])) 
        print(" [x] Done") 
 
 
    channel.basic_consume(queue='ttl_queue', on_message_callback=callback, auto_ack=True) 
 
    print(' [*] Waiting for messages. To exit press CTRL+C') 
    channel.start_consuming() 
 
 
if __name__ == '__main__': 
    main() 