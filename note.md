kafka-avro-console-producer \
    --topic demotopic \
    --bootstrap-server broker:9092 \
    --property schema.registry.url=http://localhost:8081 \
    --property value.schema="$(< /etc/tutoregistry/user-schema.json)"

    kafka-avro-console-consumer \
    --topic demotopic \
    --bootstrap-server broker:9092 \
    --property schema.registry.url=http://localhost:8081 \
    --from-beginning