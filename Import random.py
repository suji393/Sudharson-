Import random
Import time

Class SmartMeter:
    Def __init__(self, meter_id):
        Self.meter_id = meter_id
        Self.energy_consumption = 0
    
    Def generate_energy_consumption(self):
        # Simulate energy consumption by generating random values
        Self.energy_consumption = random.uniform(0.5, 2.5)  # kWh
        Return self.energy_consumption

Class UtilityCompany:
    Def __init__(self):
        Self.meters = {}
    
    Def add_meter(self, meter_id):
        Self.meters[meter_id] = SmartMeter(meter_id)
    
    Def collect_data(self):
        Total_consumption = 0
        For meter_id, meter in self.meters.items():
            Consumption = meter.generate_energy_consumption()
            Total_consumption += consumption
            Print(f”Meter {meter_id}: Energy consumption = {consumption} kWh”)
        Print(f”Total energy consumption = {total_consumption} kWh”)

If __name__ == “__main__”:
    Utility = UtilityCompany()
    
    # Add some smart meters
    For I in range(1, 6):
        Utility.add_meter(i)
    
    # Simulate data collection at regular intervals
    While True:
        Print(“\nData collection:”)
        Utility.collect_data()
        Time.sleep(5)  # Simulate data collection every 5 seconds
