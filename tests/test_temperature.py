import os.path

from climate.temperature import DEFAULT_TEMPERATURE_DATA_PATH, Temperatures


def test_temperature_data_loading():
    """Test temperature data loading"""

    test_data_file_path = os.path.join(
        DEFAULT_TEMPERATURE_DATA_PATH,
        'temperature_by_country_light.csv',
    )
    t = Temperatures(
        data_file_path=test_data_file_path
    )

    assert t.data is not None
