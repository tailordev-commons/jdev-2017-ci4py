import datetime
import os.path

import matplotlib.pyplot as plt
import pandas as pd

from .exceptions import DataLoadingException
from .utils import slugify

DEFAULT_TEMPERATURE_DATA_PATH = os.path.realpath(
    os.path.join(
        os.path.dirname(__file__),
        './data'
    )
)
DEFAULT_TEMPERATURE_DATA_FILE_PATH = os.path.join(
    DEFAULT_TEMPERATURE_DATA_PATH,
    'temperature_by_country.csv',
)


class Temperatures:
    """Play with Earth Surface Temperature Dataset from Kaggle.

    Source data:
    https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data
    """

    def __init__(self, data_file_path=DEFAULT_TEMPERATURE_DATA_FILE_PATH):

        self.data = None
        self.country = None
        self.selection = None
        self._load_data(data_file_path)

    def _load_data(self, data_file_path):
        """Load data in a Pandas DataFrame from a csv file"""

        self.data = pd.read_csv(
            data_file_path,
            parse_dates=['dt']
        )

        if self.data is None:
            raise DataLoadingException(
                "No data loaded from file {}".format(data_file_path)
            )

    def _set_country(self, country):
        """Assign self.country if country dataset is available"""

        # Check data availability for a country
        if country not in self.data.Country.unique():
            raise KeyError(
                "No data available for country: '{}'".format(country)
            )

        self.country = country

    def select(self, country=None):
        """Perform country records selection and assign new DataFrame to
        self.selection
        """

        if country:
            self._set_country(country)
            self.selection = self.data.query(
                'Country == "{}"'.format(self.country)
            )

    def monthly_plot(self, save=False, file_name=None):
        """Plot country average temperatures sorted by month
        """

        if self.selection is None:
            raise DataLoadingException("Selection is empty")

        fig, ax = plt.subplots()
        months = [
            datetime.date(2017, m, 1).strftime('%B')
            for m in range(1, 13)
        ]

        for month in range(1, 13):
            month_rows = self.selection.dt.map(lambda d: d.month == month)
            month_line, = ax.plot(
                self.selection.dt[month_rows],
                self.selection.AverageTemperature[month_rows],
                label="{}".format(months[month - 1])
            )

        ax.set_title(
            "{} monthly temperatures over the years".format(self.country)
        )
        ax.legend(loc='upper left')
        plt.xlabel("Year")
        plt.ylabel("Average temperature (°C)")

        if save:
            if file_name is None:
                file_name = slugify(self.country)
            fig.savefig(file_name)
        else:
            plt.show()
