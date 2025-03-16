from typing import Callable, Dict, NamedTuple, Optional, TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from . import KOTBWorld


class KOTBItem(Item):
    game = "KingOfTheBridge"


class KOTBItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    can_create: Callable[["KOTBWorld"], bool] = lambda world: True


item_data_table: Dict[str, KOTBItemData] = {
    "Rule 00": KOTBItemData(
        code=8675309,
        type=ItemClassification.progression,
    ),
    "Victory": KOTBItemData(
        code=8675310,
        type=ItemClassification.useful,
        can_create=lambda world: False,
    )
}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
