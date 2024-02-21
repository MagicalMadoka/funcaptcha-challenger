import threading

from loguru import logger


class LoguruContext:
    def __init__(self):
        self._storage = threading.local()

    def set(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self._storage, key, value)

    def get(self, key):
        return getattr(self._storage, key, None)


log_context = LoguruContext()


def add_trace_id(record):
    trace_id = log_context.get("trace_id")
    if trace_id:
        record["message"] = f" Trace ID: {trace_id} | {record['message']}"


logger = logger.patch(add_trace_id)
