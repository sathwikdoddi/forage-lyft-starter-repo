import unittest
from datetime import date, datetime, timedelta
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class TestNubbinBattery(unittest.TestCase):
    def setUp(self):
        time_to_service = 4
        today = datetime.today().date()
        more_than_service_time = today - timedelta(days=365*time_to_service+1)
        less_than_service_time = today - timedelta(days=365*time_to_service-1)
        self.nubin_needing_service = NubbinBattery(
            current_date=today,
            last_service_date=more_than_service_time
        )
        self.nubbin_no_serivce = NubbinBattery(
            current_date=today,
            last_service_date=less_than_service_time
        )

    def test_should_need_service(self):
        self.assertTrue(
            self.nubin_needing_service.needs_service()
        )

    def test_should_not_need_service(self):
        self.assertFalse(
            self.nubbin_no_serivce.needs_service()
        )


class TestSpindlerBattery(unittest.TestCase):
    def setUp(self):
        time_to_service = 2
        today = datetime.today().date()
        more_than_service_time = today - timedelta(days=365*time_to_service+1)
        less_than_service_time = today - timedelta(days=365*time_to_service-1)
        self.spindler_needing_service = SpindlerBattery(
            current_date=today,
            last_service_date=more_than_service_time
        )
        self.spinder_no_service = SpindlerBattery(
            current_date=today,
            last_service_date=less_than_service_time
        )

    def test_should_need_service(self):
        self.assertTrue(
            self.spindler_needing_service.needs_service()
        )

    def test_should_not_need_service(self):
        self.assertFalse(
            self.spinder_no_service.needs_service()
        )


if __name__ == "__main__":
    unittest.main()