from abc import ABC, abstractmethod
import pandas as pd
from IPython.display import display

# This class defines a common interface for data inspection strategies.
class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self, df: pd.DataFrame):
        """
        Perform a specific type of data inspection.
        """
        pass

# This strategy inspects the data types of each column and counts non-null values.
class DataTypesInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        """
        Inspects and prints the data types and non-null counts of the dataframe columns.
        """
        print("\nData Types and Non-null Counts:")
        display(df.info())

# This strategy provides summary statistics for both numerical and categorical features.
class SummaryStatisticsInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        """
        Prints summary statistics for numerical and categorical features.
        """
        print("\nSummary Statistics (Numerical Features):")
        display(df.describe())
        print("\nSummary Statistics (Categorical Features):")
        display(df.describe(include=["O"]))


# This class allows you to switch between different data inspection strategies.
class DataInspector:
    def __init__(self, strategy: DataInspectionStrategy):
        """
        Initializes the DataInspector with a specific inspection strategy.
        """
        self._strategy = strategy

    def set_strategy(self, strategy: DataInspectionStrategy):
        """
        Sets a new strategy for the DataInspector.
        """
        self._strategy = strategy

    def execute_inspection(self, df: pd.DataFrame):
        """
        Executes the inspection using the current strategy.
        """
        self._strategy.inspect(df)



