from typing import NamedTuple, List, Dict

from BaseClasses import Region
from worlds.kotb import KOTBWorld


class KOTBRegionData(NamedTuple):
    connecting_regions: List[str] = []


region_data_table: Dict[str, KOTBRegionData] = {
    "Menu": KOTBRegionData(["Pregame"]),
    "Pregame": KOTBRegionData(["Play"]),
    "Play": KOTBRegionData(["Endgame"]),
    "Endgame": KOTBRegionData(),
}