from datetime import datetime, time
from datetime import timedelta
import pytz
from .static_config import TIME_TO_BOOT_AND_SHUTDOWN


class Schedule:
    def __init__(self):
        self._time_offset: int = 0

    def adjust_time(self, timestamp: str) -> str:
        pass

    def calculate_shutdown_duration(self, app_run_time: float) -> float:
        shutdown_duration = app_run_time - TIME_TO_BOOT_AND_SHUTDOWN
        return max(shutdown_duration, 0)

    def get_wake_time(self, time_spent_shutdown: float) -> datetime:
        pass

    def should_shutdown(self, desired_shutdown_duration: float) -> bool:
        pass

    def shutdown(self, waiting_time: float, current_time: datetime) -> None:
        pass

    def working_time_check(self, wake_up_timestamp: str, shut_down_timestamp: str) -> None:
        pass
