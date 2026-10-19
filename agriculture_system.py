class Farmer:
    """Stores basic information about a farmer."""

    def __init__(self, farmer_id, name, village):
        self.farmer_id = farmer_id
        self.name = name
        self.village = village

    def display_info(self):
        return f"Farmer: {self.name} | ID: {self.farmer_id} | Village: {self.village}"


class CropRecord:
    """Stores information about one crop harvest record."""
    records_created = 0

    def __init__(self, farmer, crop_name, area_hectares, yield_kg):
        self.farmer = farmer
        self.crop_name = crop_name
        self.area_hectares = area_hectares
        self.yield_kg = yield_kg
        CropRecord.records_created += 1

    # Instance method
    def display_info(self):
        print(f"Farmer: {self.farmer.name}")
        print(f"Crop: {self.crop_name}")
        print(f"Farm area: {self.area_hectares} hectares")
        print(f"Harvest: {self.yield_kg} kg")
        print("-" * 35)

    # Class method
    @classmethod
    def record_count(cls):
        return cls.records_created


# One list stores multiple CropRecord objects.
crop_records = []


def add_record(farmer, crop_name, area_hectares, yield_kg):
    """Create and store a crop record."""
    record = CropRecord(farmer, crop_name, area_hectares, yield_kg)
    crop_records.append(record)
    print("Crop record added successfully.")


def display_all_records():
    """Display every record in the list."""
    if not crop_records:
        print("No crop records have been added.")
        return

    for record in crop_records:
        record.display_info()


def calculate_total_yield():
    """Calculate total harvest across all records."""
    total = sum(record.yield_kg for record in crop_records)
    print(f"Total crop yield: {total} kg")


def main():
    # Fictional sample farmer; no sensitive personal data is used.
    farmer1 = Farmer("F001", "Musa Kamara", "Makeni")
    farmer2 = Farmer("F002", "Aminata Sesay", "Bo")

    print("AGRICULTURAL CROP YIELD MONITORING SYSTEM")
    print(farmer1.display_info())
    print(farmer2.display_info())
    print("-" * 35)

    add_record(farmer1, "Rice", 2.0, 1800)
    add_record(farmer2, "Cassava", 1.5, 1200)
    add_record(farmer1, "Groundnut", 1.0, 650)

    print("\nALL CROP RECORDS")
    display_all_records()
    calculate_total_yield()
    print(f"Number of records: {CropRecord.record_count()}")


if __name__ == "__main__":
    main()
