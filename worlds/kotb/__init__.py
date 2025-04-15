from typing import List, Dict, Any

from BaseClasses import Region, Tutorial
from worlds.AutoWorld import WebWorld, World
from .Items import KOTBItem, item_data_table, item_table
from .Locations import KOTBLocation, get_location_data_table, get_location_table, get_locked_locations
from .Options import KOTBOptions
from .Regions import region_data_table
from .Rules import set_victory_rule, set_location_rules


class KOTBWebWorld(WebWorld):
    theme = "stone"

    setup_en = Tutorial(
        tutorial_name="Getting started",
        description="Setting up King of the Bridge",
        language="English",
        file_name="guide_en.md",
        link="guide/en",
        authors=["Ploki122"]
    )

    tutorials = [setup_en]


class KOTBWorld(World):
    """Face off against the bridge troll in his bizarre game of chess!
    Decrypt, Twist and Enforce the rules as your devious opponent attempts to break them in King of the Bridge!"""

    game = "KingOfTheBridge"
    web = KOTBWebWorld()
    options: KOTBOptions
    options_dataclass = KOTBOptions
    location_name_to_id = get_location_data_table()
    item_name_to_id = item_table
    version = "0.0.1"
    minimum_compatible_client = "0.0.1"

    def create_item(self, name: str) -> KOTBItem:
        return KOTBItem(name, item_data_table[name].type, item_data_table[name].code, self.player)

    def create_items(self) -> None:
        item_pool: List[KOTBItem] = []
        for name, item in item_data_table.items():
            if item.code and item.can_create(self):
                item_pool.append(self.create_item(name))

        self.multiworld.itempool += item_pool

    def create_regions(self) -> None:
        location_data_table = get_location_data_table()

        # Create regions.
        for region_name in region_data_table.keys():
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        # Create locations.
        for region_name, region_data in region_data_table.items():
            region = self.get_region(region_name)
            region.add_locations({
                location_name: location_data.address for location_name, location_data in location_data_table.items()
                if location_data.region == region_name and location_data.can_create(self)
            }, KOTBLocation)
            region.add_exits(region_data_table[region_name].connecting_regions)

    def get_filler_item_name(self) -> str:
        return "Rule 00"

    def set_rules(self) -> None:
        # Location rules
        Rules.set_location_rules(self, self.player)

        # Completion condition.
        Rules.set_victory_rule(self, self.player)

    def fill_slot_data(self) -> Dict[str, Any]:
        return {
            "Version": self.version,
            "MinClientVersion": self.minimum_compatible_client,
        }
