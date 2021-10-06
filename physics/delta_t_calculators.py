import time


class DefaultDeltaTCalculator:
    def __init__(self):
        self._current_time = time.time()
        self._last_time = time.time()

    def __call__(self):
        self._current_time = time.time()
        delta_t = self._current_time - self._last_time
        self._last_time = self._current_time
        return delta_t


class FixedDeltaTCalculator:
    def __init__(self, delta_t=0.01):
        self._delta_t = delta_t

    def __call__(self):
        return self._delta_t
