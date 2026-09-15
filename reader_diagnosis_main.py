"""Interactive front-end for the reader_diagnosis health-score module."""

import reader_diagnosis
from reader_diagnosis import calculate_health_score


def read_reader(index):
    """Prompt for one reader's data, re-prompting on invalid values."""
    while True:
        try:
            unit_id = input(f"Reader {index} ID: ")
            temp = float(input(f"  {unit_id} temperature (C): "))
            voltage = float(input(f"  {unit_id} voltage (V): "))
            current = float(input(f"  {unit_id} current (A): "))
            reader_diagnosis.validate_reading(temp, voltage, current)
            return {"id": unit_id, "temp": temp, "voltage": voltage, "current": current}
        except ValueError as e:
            print(f"Rejected reading: {e} - please re-enter.")


def main():
    """Collect readings, then print a per-unit report and fleet summary."""
    try:
        n = int(input("How many readers to analyze? "))
    except ValueError:
        print("Invalid count. Exiting.")
        return

    readers = [read_reader(i) for i in range(1, n + 1)]  # gather all units first

    print("\n===== READER DIAGNOSIS REPORT =====")
    for r in readers:
        score = calculate_health_score(r["temp"], r["voltage"], r["current"])
        condition = reader_diagnosis.classify(score)
        reliable = reader_diagnosis.is_reliable(score)
        print(f"{r['id']}: health score {score:.2f} ({condition})"
              f" - {'reliable' if reliable else 'unreliable'}")
        if condition == "Warning":
            print(f"  -> {r['id']} requires recalibration")
        elif condition == "Critical":
            print(f"  -> {r['id']} requires servicing")

    print("\n===== FLEET SUMMARY =====")
    print(f"Unit most in need of servicing: {reader_diagnosis.worst_reader(readers)}")
    report = reader_diagnosis.fleet_report(readers)
    print("Fleet report:", {k: report[k] for k in ("Normal", "Warning", "Critical")})


if __name__ == "__main__":
    main()