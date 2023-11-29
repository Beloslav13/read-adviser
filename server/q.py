import functools
import time

from django.db import reset_queries, connection


def query_debugger(func):
    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        reset_queries()
        start_queries = len(connection.queries)

        start = time.perf_counter()
        res = func(*args, **kwargs)
        print(res)
        # func(*args, **kwargs)
        end = time.perf_counter()

        end_queries = len(connection.queries)

        # for q in connection.queries:
        #     for k, v in q.items():
        #         print(v)
        print(f"View (function name): {func.__name__}")
        print(f"Queries quantity: {end_queries - start_queries}")
        print(f"Execution time: {(end - start):.2f}s")
        # res
        return res

    return inner_func
