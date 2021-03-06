import pika 
import time 
import re 
 
 
def main(): 
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost')) 
    channel = connection.channel() 
 
    channel.queue_declare(queue='limit', arguments={'x-max-length': 5}) 
    #channel.queue_declare(queue='limit_reject', arguments={'x-max-length': 5,  'x-overflow': 'reject-publish'})

 
    def callback(ch, method, properties, body): 
        print(" [x] Received %r" % body.decode()) 
        # time.sleep(int(re.findall(r'\d+', body.decode())[0])) 
        print(" [x] Done") 
 
 
    channel.basic_consume(queue='limit', on_message_callback=callback, auto_ack=True) 
 
    print(' [*] Waiting for messages. To exit press CTRL+C') 
    channel.start_consuming() 
 
 
if __name__ == '__main__': 
    main() 