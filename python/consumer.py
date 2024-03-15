# import librairies

from kafka import KafkaConsumer
from time import sleep

# création d'un consumer

def getConsumerKafka(url:str, group_id:str):
    return KafkaConsumer(
        topics='topicPython',
        bootstrap_servers= url,
        client_id="mon_client_python",
        auto_offset_reset="earlest",
        group_id= group_id
    )

# programme de lecture message kafka
def consumeFromKafka():
    kafka_ip = "localhost"
    kafka_port = "9092"
    url = "".join([kafka_ip,":", kafka_port])
    monConsumer = getConsumerKafka(url=url, group_id="grp-python")

    for event in monConsumer:
        if not event.value:
            continue
        
        msg = event.value.decode('utf-8')
        key = event.key
        offset = event.offset
        sleep(1)
        print("key = " + key + ", offset = " + offset + ", message = " + msg)



# demarrage du programme
        
if __name__ == "__name__":
    consumeFromKafka()
    
