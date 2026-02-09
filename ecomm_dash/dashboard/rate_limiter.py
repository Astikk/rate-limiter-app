import redis
from rest_framework.response import Response
from rest_framework.exceptions import Throttled

# decode_responses=True (important)
# By default, Redis returns bytes, not strings.
# Redis has numbered databases: db=0 (default)
redis_client = redis.StrictRedis(host="localhost", port="6379", db=0, decode_responses=True)

def rate_limit(max_request:int, time_window:int):
    def decorator(func):
        def wrapper(self, request, *args, **kwargs):
            client = request.user.id if request.user.is_authenticated else request.META.get('REMOTE_ADDR')
            endpoint = request.path

            redis_key = f"rate_limit:{client}:{endpoint}"
            current_request = redis_client.get(redis_key)

            if current_request is None:
                redis_client.set(redis_key, 1, ex=time_window)
            elif int(current_request) < max_request:
                redis_client.incr(redis_key)
            else:
                raise_after = redis_client.ttl(redis_key)
                raise Throttled(detail=f"Rate limit exceed. Try again after {raise_after} sec!")
            return func(self, request, *args, **kwargs)
        return wrapper
    return decorator