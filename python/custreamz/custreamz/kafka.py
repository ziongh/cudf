# Copyright (c) 2020, NVIDIA CORPORATION.

import custreamz._libxx.kafka as libkafka


class KafkaHandle(object):
    def __init__(self, kafka_configs):
        self.kafka_configs = kafka_configs
        libkafka.create_kafka_handle(kafka_configs)

    def metadata(self):
        libkafka.print_consumer_metadata()

    def dump_configs(self):
        libkafka.dump_configs()

    def read_gdf(
        self,
        lines=True,
        start=-1,
        end=-1,
        timeout=10000,
        delimiter="\n",
        *args,
        **kwargs,
    ):
        return libkafka.read_gdf(lines, start, end, timeout, delimiter)

    def committed(self):
        return libkafka.get_committed_offset()

    def get_watermark_offsets(
        self, topic=None, partition=-1, *args, **kwargs,
    ):
        offsets = libkafka.get_watermark_offsets(topic, partition)
        return offsets[b"low"], offsets[b"high"]

    def commit(
        self, topic=None, partition=0, offset=-1001, *args, **kwargs,
    ):
        libkafka.commit_topic_offset(topic, partition, offset)

    def produce(self, topic=None, message_val=None, message_key=None):
        return libkafka.produce_message(topic, message_val, message_key)
