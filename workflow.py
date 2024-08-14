from pathlib import Path
from pyam import IamDataFrame
from nomenclature import DataStructureDefinition, RegionProcessor, process


here = Path(__file__).absolute().parent


def main(df: IamDataFrame) -> IamDataFrame:
    """Project/instance-specific workflow for scenario processing"""

    # Run the validation and region-processing
    dsd = DataStructureDefinition(here / "definitions")
    processor = RegionProcessor.from_directory(path=here / "mappings", dsd=dsd)
    return process(df, dsd, processor=processor)

def public(df: IamDataFrame) -> IamDataFrame:
    return df
