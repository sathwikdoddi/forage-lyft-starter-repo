from battery import Battery

class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.years_to_service = 4

    def needs_service(self):
        temp_date = self.last_service_date
        temp_date.replace(year=self.last_service_date + self.years_to_service)
        date_which_battery_should_be_serviced_by = temp_date
        if date_which_battery_should_be_serviced_by < self.current_date:
            return True
        else:
            return False