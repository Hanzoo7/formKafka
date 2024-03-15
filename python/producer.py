from kafka import KafkaProducer

def getProducerKafka(url:str):
    return KafkaProducer(bootstrap_server=url)

def sendToKafka():
    url="".join(["localhost", "9092"])
    monproducer = getProducerKafka(url=url)

    while msg := input('message (vide pour stop) :'):
        mykey = input('KEy :')
        
        monproducer.send(
            key= bytes(mykey, "utf-8"),
            topic = "topicPython",
            value=bytes(msg, 'utf-8')
        )

if __name__ == '__name__':
    sendToKafka()