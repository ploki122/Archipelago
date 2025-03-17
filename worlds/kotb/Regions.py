from typing import Dict, List, NamedTuple


class KOTBRegionData(NamedTuple):
    connecting_regions: List[str] = []


region_data_table: Dict[str, KOTBRegionData] = {
    "Menu": KOTBRegionData(["Act 2"]),
    "Act 2": KOTBRegionData(),
}
