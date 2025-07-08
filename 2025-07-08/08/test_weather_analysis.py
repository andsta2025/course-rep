import numpy as np
from weather_analysis import analyze_temperatures

def test_analyze_temperatures():
    sample_data = np.array([10, 15, 20, 15, 10])
    result = analyze_temperatures(sample_data)

    assert result["mean"] == np.mean(sample_data)
    assert result["median"] == np.median(sample_data)
    assert result["min"] == np.min(sample_data)
    assert result["max"] == np.max(sample_data)