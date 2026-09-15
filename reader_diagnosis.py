"""Health-score diagnosis for sensor-reader units.

Computes a 0-100 score from temperature/voltage/current deviations from
ideal values, classifies units as Normal/Warning/Critical and provides
fleet-level summary helpers. Run directly to execute self-tests.
"""

# Ideal operating point of a reader
IDEAL_TEMP = 30.0
IDEAL_VOLTAGE = 5.0
IDEAL_CURRENT = 0.5

# Penalty weights per unit of deviation from the ideal values
TEMP_WEIGHT = 3.0
VOLTAGE_WEIGHT = 6.0
CURRENT_WEIGHT = 20.0

# Classification cutoffs for the health score
NORMAL_THRESHOLD = 80.0
WARNING_THRESHOLD = 60.0


def validate_temperature(temp):
    """Reject temperatures outside the plausible -20..60 C range."""
    if temp < -20 or temp > 60:
        raise ValueError(f"temperature {temp} C is outside the plausible range (-20 to 60)")


def validate_voltage(voltage):
    """Reject voltages outside the plausible 0..12 V range."""
    if voltage < 0:
        raise ValueError(f"voltage cannot be negative: {voltage} V")
    if voltage > 12:
        raise ValueError(f"voltage {voltage} V is outside the plausible range (0 to 12)")


def validate_current(current):
    """Reject currents outside the plausible 0..5 A range."""
    if current < 0 or current > 5:
        raise ValueError(f"current {current} A is outside the plausible range (0 to 5)")


def validate_reading(temp, voltage, current):
    """Run all three validation checks on a single reading."""
    validate_temperature(temp)
    validate_voltage(voltage)
    validate_current(current)


def calculate_health_score(temp, voltage, current):
    """Return a 0-100 score: 100 minus weighted deviations from ideal."""
    validate_reading(temp, voltage, current)
    score = 100.0
    score -= abs(temp - IDEAL_TEMP) * TEMP_WEIGHT        # temperature penalty
    score -= abs(voltage - IDEAL_VOLTAGE) * VOLTAGE_WEIGHT  # voltage penalty
    score -= abs(current - IDEAL_CURRENT) * CURRENT_WEIGHT  # current penalty
    return round(max(0.0, min(100.0, score)), 2)  # clamp to [0, 100]


def classify(score):
    """Classify a health score as Normal, Warning or Critical."""
    if score >= NORMAL_THRESHOLD:
        return "Normal"
    if score >= WARNING_THRESHOLD:
        return "Warning"
    return "Critical"


def is_reliable(score):
    """A reader is considered reliable only in the Normal band."""
    return classify(score) == "Normal"


def worst_reader(readers):
    """Return the id of the reader with the lowest health score."""
    return min(
        readers,
        key=lambda r: calculate_health_score(r["temp"], r["voltage"], r["current"]),
    )["id"]


def fleet_report(readers):
    """Count readers per classification across the whole fleet."""
    report = {"Normal": 0, "Warning": 0, "Critical": 0}
    for r in readers:
        score = calculate_health_score(r["temp"], r["voltage"], r["current"])
        report[classify(score)] += 1
    return report


if __name__ == "__main__":
    assert calculate_health_score(30, 5, 0.5) == 100
    assert is_reliable(calculate_health_score(30, 5, 0.5)) is True
    assert classify(calculate_health_score(35, 4.5, 0.7)) == "Warning"
    assert classify(calculate_health_score(45, 3, 2.0)) == "Critical"

    sample = [
        {"id": "R001", "temp": 30, "voltage": 5, "current": 0.5},
        {"id": "R002", "temp": 45, "voltage": 3, "current": 2.0},
        {"id": "R003", "temp": 35, "voltage": 4.5, "current": 0.7},
    ]
    assert worst_reader(sample) == "R002"
    assert fleet_report(sample) == {"Normal": 1, "Warning": 1, "Critical": 1}

    try:
        validate_voltage(-1)
        raise AssertionError("negative voltage should be rejected")
    except ValueError:
        pass

    print("reader_diagnosis self-tests passed")