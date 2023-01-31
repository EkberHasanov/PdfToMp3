import sys, os, time, pika
from api.services.converter.consumer.callback import callback
from api.models.rabbitmq import connect


def main() -> None:
    connection = connect()
    channel = connection.channel()

    channel.basic_consume(
        queue="pdf",
        on_message_callback=callback
    )

    print("Waiting for messages...")
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Process interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
