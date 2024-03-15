const {kafka} = require("kafkajs")

const getConsumer = (group_Id) => {
    let kafkaConfig = {
        clientId: "js-consumer",
        broker: ["localhost:9092"],

    };
    const kafka = new kafka(config = kafkaConfig);
    return kafka.consumer(groupId: group_Id);

);

