# coding: utf-8
# configs.py

class mq_config:

    host="192.168.0.11"
    virtual_host="test"
    username="test"
    password="test"
    port=5672

    queue_config = dict(
        exchange='topic_link',
        type='topic',
        queue='hello',
        auto_delete=False,
        exclusive=False,
        routing_key='hello.world',
        prefetch_count=1,
        no_ack=False,
        delay=0.01
    )