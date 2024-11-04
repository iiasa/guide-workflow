from pathlib import Path
from pyam import IamDataFrame
from nomenclature import DataStructureDefinition, RegionProcessor, process
import logging


here = Path(__file__).absolute().parent


logger = logging.getLogger(__name__)

file_handler = logging.FileHandler(snakemake.log[0], mode="a")
file_handler.setLevel(logging.DEBUG)

# Define a logging format (optional)
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s", "%Y-%m-%d %H:%M:%S")
file_handler.setFormatter(formatter)

for logger_name in ["ixmp4", "pyam", "nomenclature", logger.name]:
    logging.getLogger(logger_name).addHandler(file_handler)


def main(df: IamDataFrame) -> IamDataFrame:
    """Project/instance-specific workflow for scenario processing"""

    # Run the validation and region-processing
    dsd = DataStructureDefinition(here / "definitions")
    processor = RegionProcessor.from_directory(path=here / "mappings", dsd=dsd)
    return process(df, dsd, processor=processor)

logger.info(f"Starting processing for {snakemake.input[0]}")
main(pyam.IamDataFrame(snakemake.input[0])).to_excel(snakemake.output[0])
logger.info(f"Successfully finished processing for {snakemake.input[0]}")
