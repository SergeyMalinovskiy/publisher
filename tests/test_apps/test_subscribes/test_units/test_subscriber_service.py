import pytest

from server.apps.subscribes.logic.services.subscriber_service import SubscriberService


@pytest.fixture
def service() -> SubscriberService:
    return


def test_create_subscriber(service: SubscriberService):
    """"""
    subscriber = service.create_subscriber(
        'email',
        'test@email.ru',
        True
    )



def test_create_subscriber_with_unknown_method(service):
    pass
