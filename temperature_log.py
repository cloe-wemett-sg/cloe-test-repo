# Test file for cloe-test-repo — feel free to read, edit, or delete this.
from dataclasses import dataclass, field
from datetime import datetime
from statistics import mean, median, stdev
from typing import Optional


@dataclass
class Reading:
    timestamp: datetime
    celsius: float
    sensor_id: str

    @property
    def fahrenheit(self) -> float:
        return self.celsius * 9 / 5 + 32

    @property
    def kelvin(self) -> float:
        return self.celsius + 273.15


@dataclass
class TemperatureLog:
    sensor_id: str
    readings: list[Reading] = field(default_factory=list)

    def record(self, celsius: float, timestamp: Optional[datetime] = None) -> Reading:
        r = Reading(
            timestamp=timestamp or datetime.now(),
            celsius=celsius,
            sensor_id=self.sensor_id,
        )
        self.readings.append(r)
        return r

    def _values(self) -> list[float]:
        return [r.celsius for r in self.readings]

    def average(self) -> Optional[float]:
        v = self._values()
        return mean(v) if v else None

    def minimum(self) -> Optional[Reading]:
        return min(self.readings, key=lambda r: r.celsius, default=None)

    def maximum(self) -> Optional[Reading]:
        return max(self.readings, key=lambda r: r.celsius, default=None)

    def std_dev(self) -> Optional[float]:
        v = self._values()
        return stdev(v) if len(v) >= 2 else None

    def anomalies(self, threshold: float = 2.0) -> list[Reading]:
        v = self._values()
        if len(v) < 2:
            return []
        m, s = mean(v), stdev(v)
        return [r for r in self.readings if abs(r.celsius - m) > threshold * s]

    def summary(self) -> dict:
        return {
            "sensor": self.sensor_id,
            "count": len(self.readings),
            "avg_c": round(self.average() or 0, 2),
            "min_c": self.minimum().celsius if self.minimum() else None,
            "max_c": self.maximum().celsius if self.maximum() else None,
            "std_dev": round(self.std_dev() or 0, 2),
            "anomalies": len(self.anomalies()),
        }


if __name__ == "__main__":
    log = TemperatureLog("sensor-A")
    samples = [22.1, 21.8, 22.5, 23.0, 22.3, 41.7, 21.9, 22.2, 20.1, 22.0]
    for temp in samples:
        log.record(temp)

    print(log.summary())
    print("Anomalies:")
    for r in log.anomalies():
        print(f"  {r.celsius}°C  ({r.fahrenheit:.1f}°F)")
