from datetime import datetime, timezone, timedelta
from typing import Optional


class Date:
    TIME_ZONE = "UTC"
    DATABASE_TIMESTAMP_FORMAT = 'Y-m-d H:i:s'

    def __init__(self, date: Optional[str] = None):
        try:
            self._date = datetime.fromisoformat(date) if date else datetime.now(timezone.utc)
        except ValueError:
            raise ValueError(f"Invalid date value {date}")

    def date_value(self) -> datetime:
        return self._date

    def string_date(self) -> str:
        return self._date.strftime(self.DATABASE_TIMESTAMP_FORMAT)

    def modify(self, modifier: str) -> 'Date':
        self._date = self._date + timedelta(days=int(modifier))
        return self

    def is_in_the_past(self) -> bool:
        return self._date < datetime.now(timezone.utc)

    def year(self) -> int:
        return int(self._date.strftime('%Y'))

    def month(self) -> int:
        return int(self._date.strftime('%m'))

    def to_format(self, format_value: str) -> str:
        return self._date.strftime(format_value)

    def is_greater_than(self, other: 'Date') -> bool:
        return self._date > other._date

    def __str__(self) -> str:
        return str(self._date)
