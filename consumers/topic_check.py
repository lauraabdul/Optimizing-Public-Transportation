from confluent_kafka.admin import AdminClient
import re

def topic_exists(topic):
    """Checks if the given topic exists in Kafka"""
    client = AdminClient({"bootstrap.servers": "PLAINTEXT://localhost:9092"})
    topic_metadata = client.list_topics(timeout=5)
    return topic in set(t.topic for t in iter(topic_metadata.topics.values()))


def topic_pattern_match(pattern):
    """Checks if the given topic pattern matches any topics in Kafka"""
    client = AdminClient({"bootstrap.servers": "PLAINTEXT://localhost:9092"})
    topic_metadata = client.list_topics(timeout=5)
    return any(re.match(pattern, t.topic) for t in iter(topic_metadata.topics.values()))
