import pytest
from quarry.web.app import create_app


@pytest.fixture(scope="function")
def client(redisdb, mocker):

    # Make sure that we only ever use the redisdb function
    #  from pytest-redis
    mocker.patch("redis.Redis", return_value=redisdb)

    app = create_app(
        {
            "TESTING": True,
            "OAUTH_CONSUMER_TOKEN": None,
            "OAUTH_SECRET_TOKEN": None,
            "REDIS_HOST": "localhost",
            "REDIS_PORT": 6379,
            "REDIS_DB": None,
        }
    )

    with app.test_client() as client:
        yield client
