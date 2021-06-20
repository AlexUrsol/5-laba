import pika 
 
 
def main(): 
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost')) 
    channel = connection.channel() 
 
    channel.queue_declare(queue='ack_queue1') 
 
    def callback(ch, method, properties, body): 
        print(" [x] Received %r" % body.decode()) 
        print(" [x] Done") 
        channel.basic_ack(multiple=False, delivery_tag=method.delivery_tag) 
 
    channel.basic_consume(queue='ack_queue1', on_message_callback=callback) 
 
    print(' [*] Waiting for messages. To exit press CTRL+C') 
    channel.start_consuming() 
 
 
if __name__ == '__main__': 
    main() 