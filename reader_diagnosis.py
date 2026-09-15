IDEAL_TEMP = 30.0
IDEAL_VOLTAGE = 5.0
IDEAL_CURRENT = 0.5

TEMP_WEIGHT = 3.0
VOLTAGE_WEIGHT = 6.0
CURRENT_WEIGHT = 20.0

NORMAL_THRESHOLD = 80.0
WARNING_THRESHOLD = 60.0

def validate_temperature(temp):
    if temp < -20 or temp > 60:
        raise ValueError(f"temperature {temp} C is outside the plausible range (-20 to 60)")

def validate_voltage(voltage):
    if voltage < 0:
        raise ValueError(f"voltage cannot be negative: {voltage} V")
    if voltage > 12:
        raise ValueError(f"voltage {voltage} V is outside the plausible range (0 to 12)")

def validate_current(current):
    if current < 0 or current > 5:
        raise ValueError(f"current {current} A is outside the plausible range (0 to 5)")

def validate_reading(temp, voltage, current):
    validate_temperature(temp)
    validate_voltage(voltage)
    validate_current(current)

def calculate_health_score(temp, voltage, current):
    validate_reading(temp, voltage, current)
    score = 100.0
    score -= abs(temp - IDEAL_TEMP) * TEMP_WEIGHT
    score -= abs(voltage - IDEAL_VOLTAGE) * VOLTAGE_WEIGHT
    score -= abs(current - IDEAL_CURRENT) * CURRENT_WEIGHT
    return round(max(0.0, min(100.0, score)), 2)

def classify(score):
    if score >= NORMAL_THRESHOLD:
        return "Normal"
    if score >= WARNING_THRESHOLD:
        return "Warning"
    return "Critical"

def is_reliable(score):
    return classify(score) == "Normal"

def worst_reader(readers):
    return min(
        readers,
        key=lambda r: calculate_health_score(r["temp"], r["voltage"], r["current"]),
    )["id"]

def fleet_report(readers):
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