from typing import NamedTuple, List, Dict


class KOTBRegionData(NamedTuple):
    connecting_regions: List[str] = []


region_data_table: Dict[str, KOTBRegionData] = {
    "Menu": KOTBRegionData(["Pregame"]),
    "Pregame": KOTBRegionData(["Play"]),
    "Play": KOTBRegionData(["Endgame"]),
    "Endgame": KOTBRegionData(),
}