import os
import os.path

import pandas as pd
import pytest

from climate.temperature import DEFAULT_TEMPERATURE_DATA_PATH, Temperatures
from climate.exceptions import DataLoadingException

TEST_DATA_FILE_PATH = os.path.join(
    DEFAULT_TEMPERATURE_DATA_PATH,
    'temperature_by_country_light.csv',
)


def test_temperature_data_loading():
    """Test temperature data loading"""

    t = Temperatures(data_file_path=TEST_DATA_FILE_PATH)
    assert t.data is not None

    with pytest.raises(FileNotFoundError):
        t = Temperatures(data_file_path='fake/path')


def test_set_country():
    """Test the _set_country() private method"""

    # Country exists
    t = Temperatures(data_file_path=TEST_DATA_FILE_PATH)
    t._set_country('France')
    assert t.country == 'France'

    # Country does not exists
    with pytest.raises(KeyError):
        t._set_country('Utopia')


def test_select():
    """Test data subset selection"""

    t = Temperatures(data_file_path=TEST_DATA_FILE_PATH)

    # Select without condition (no country)
    t.select()
    assert t.country is None
    assert t.selection is None

    # Select with an existing country
    t.select(country='France')
    assert t.country == 'France'
    assert t.selection is not None
    assert isinstance(t.selection, pd.DataFrame)


def test_monthly_plot(tmpdir):
    """Test monthly plot generation"""

    t = Temperatures(data_file_path=TEST_DATA_FILE_PATH)

    # No selection has been performed, we should raise an error
    with pytest.raises(DataLoadingException):
        t.monthly_plot()

    # Select a country
    t.select(country='France')
    t.monthly_plot(save=True, file_name=tmpdir.join('myplot.png'))
    assert len(tmpdir.listdir()) == 1
    assert tmpdir.listdir()[0].basename == 'myplot.png'


def test_monthly_plot_saving_with_defaults(tmpdir):
    """Test monthly plot generation"""

    t = Temperatures(data_file_path=TEST_DATA_FILE_PATH)

    # Test saving without file name
    t.select(country='France')

    # Go to the temporary directory
    os.chdir(tmpdir)
    t.monthly_plot(save=True)
    assert len(tmpdir.listdir()) == 1
    assert tmpdir.listdir()[0].basename == 'france.png'
