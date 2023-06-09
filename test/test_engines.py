import unittest
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestCapuletEngine(unittest.TestCase):
    def setUp(self):
        self.capulet_needing_service = CapuletEngine(30001, 0)
        self.capulet_no_service = CapuletEngine(30000, 0)

    def test_should_need_service(self):
        self.assertTrue(
            self.capulet_needing_service.needs_service()
        )

    def test_should_not_need_service(self):
        self.assertFalse(
            self.capulet_no_service.needs_service()
        )


class TestSternmanEngine(unittest.TestCase):
    def setUp(self):
        self.sternman_needing_service = SternmanEngine(warning_light_on=True)
        self.sternman_no_service = SternmanEngine(warning_light_on=False)

    def test_should_need_service(self):
        self.assertTrue(
            self.sternman_needing_service.needs_service()
        )

    def test_should_not_need_service(self):
        self.assertFalse(
            self.sternman_no_service.needs_service()
        )


class TestWilloughbyEngine(unittest.TestCase):
    def setUp(self):
        self.willoughby_needing_service = WilloughbyEngine(60001, 0)
        self.willoughby_no_service = WilloughbyEngine(60000, 0)

    def test_should_need_service(self):
        self.assertTrue(
            self.willoughby_needing_service.needs_service()
        )

    def test_should_not_need_service(self):
        self.assertFalse(
            self.willoughby_no_service.needs_service()
        )


if __name__ == "__main__":
    unittest.main()