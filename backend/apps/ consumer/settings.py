import os

# Set the environment variable for the RabbitMQ connection
os.environ['RABBITMQ_URL'] = 'amqp://user:password@localhost/'

# Import the pika library
import pika

# Define the connection parameters for RabbitMQ
params = pika.URLParameters(os.environ['RABBITMQ_URL'])

# Connect to RabbitMQ
connection = pika.BlockingConnection(params)
channel = connection.channel()

# Declare the queue to consume messages from
queue_name = 'my_queue'
channel.queue_declare(queue=queue_name)


# Define the callback function to handle incoming messages
def callback(body):
    print(f'Received message: {body.decode()}')


# Start consuming messages from the queue
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
