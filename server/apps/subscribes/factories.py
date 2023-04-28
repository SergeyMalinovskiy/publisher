from typing import Any

import factory
from factory import Factory, Faker, SubFactory, LazyFunction

from server.apps.subscribes.logic.services.subscribe_method_service import (
    registered_subscribe_methods as subscribe_methods,
)
from server.apps.subscribes.models import Subscribe, Subscriber, Event
from faker import Faker as SimpleFaker


fake = SimpleFaker()

def generate_subscribe_method_name() -> str:
    return fake.random_element(elements=subscribe_methods.keys())

def generate_subscribe_method_data(method: str) -> str:
    return 'test_data'


class SubscriberFactory(Factory):
    """Subscriber factory"""

    class Meta(type):
        model = Subscriber


    is_active = Faker('pybool')
    method = LazyFunction(generate_subscribe_method_name)


    @factory.lazy_attribute
    def method_data(self):
        pass



class EventFactory(Factory):
    """Event factory"""

    class Meta(type):
        model = Event

    name = Faker('sentence')


class SubscribeFactory(Factory):
    """Subscribe factory"""

    class Meta(type):
        model = Subscribe

    subscriber = SubFactory(SubscriberFactory)
    event = SubFactory(EventFactory)

    valid_until_date = Faker('date_between', start_date='today', end_date='+30d')




