import uuid
import requests


class SubscriberDoesNotExistError(Exception):
    pass

class TopicDoesNotExistError(Exception):
    pass

class Subscribe:
    topics = {}

    @classmethod
    def add_topic(cls, topic_name):
        cls.topics[topic_name] = {}

    @classmethod
    def remove_topic(cls, topic_name):
        if cls.topics.get(topic_name):
            del cls.topics[topic_name]
        else:
            raise TopicDoesNotExistError()

    @classmethod
    def get_topics(cls):
        return cls.topics.keys()

    @classmethod
    def get_topic_subscribers(cls, topic_name):
        return cls.topics[topic_name]

    @classmethod
    def subscribe_to_topic(cls, topic_name, subscriber_name, subscriber_endpoint):
        if cls.topics.get(topic_name):
            cls.topics[topic_name][subscriber_name] = subscriber_endpoint
        else:
            raise TopicDoesNotExistError()

    @classmethod
    def unsubscribe_from_topic(cls, topic_name, subscriber_name):
        if topic_name not in cls.topics:
            raise TopicDoesNotExistError()
        if cls.topics[topic_name].get(subscriber_name):
            del cls.topics[topic_name][subscriber_name]
        else:
            raise SubscriberDoesNotExistError()




class Publish:
    messages = {}

    @classmethod
    def on_message(cls, topic_name, message):

        topic_list = Subscribe.get_topics()

        if topic_name not in topic_list:
            raise TopicDoesNotExistError()

        message_dict = {"id": uuid.uuid4().hex, "content": message}
        if topic_name not in cls.messages:
            cls.messages[topic_name] = []

        cls.messages[topic_name].append(message_dict)

        subscribers = Subscribe.get_topic_subscribers(topic_name)
        for endpoint in subscribers.values():
            cls.publish_to_subscriber(endpoint, message)

    @classmethod
    def publish_to_subscriber(cls, endpoint, message):
        requests.post(endpoint, message)
