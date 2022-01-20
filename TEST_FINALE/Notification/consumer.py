import pika, os

credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
parameters = pika.ConnectionParameters('localhost',
                                   5672,
                                   '/',
                                   credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel() # start a channel
channel.queue_declare(queue='borrowing') # Declare a queue
def callback(ch, method, properties, body):
  print("Received " + str(body))

channel.basic_consume('borrowing',
                      callback,
                      auto_ack=True)

print(' Waiting for messages:')
channel.start_consuming()
connection.close()