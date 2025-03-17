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
    "Rule 01": KOTBItemData(  # Starting item
        code=8675310,
        type=ItemClassification.filler,
        can_create=lambda world: False,
    ),
    "Rule 02": KOTBItemData(
        code=8675311,
        type=ItemClassification.progression,
    ),
    "Rule 03": KOTBItemData(
        code=8675312,
        type=ItemClassification.progression,
    ),
    "Rule 04": KOTBItemData(
        code=8675313,
        type=ItemClassification.progression,
    ),
    "Rule 05": KOTBItemData(
        code=8675314,
        type=ItemClassification.filler,
        can_create=lambda world: False,
    ),
    "Rule 06": KOTBItemData(
        code=8675315,
        type=ItemClassification.progression,
    ),
    "Rule 07": KOTBItemData(
        code=8675316,
        type=ItemClassification.progression,
    ),
    "Rule 08": KOTBItemData(
        code=8675317,
        type=ItemClassification.filler,
        can_create=lambda world: False,
    ),
    "Rule 09": KOTBItemData(
        code=8675318,
        type=ItemClassification.progression,
    ),
    "Rule 10": KOTBItemData(  # Starting item
        code=8675319,
        type=ItemClassification.filler,
        can_create=lambda world: False,
    ),
    "Rule 11": KOTBItemData(  # Starting item
        code=8675320,
        type=ItemClassification.filler,
        can_create=lambda world: False,
    ),
    "Rule 12": KOTBItemData(
        code=8675321,
        type=ItemClassification.progression,
    ),
    "Rule 13": KOTBItemData(
        code=8675322,
        type=ItemClassification.progression,
    ),
    "Rule 14": KOTBItemData(
        code=8675323,
        type=ItemClassification.progression,
    ),
    "Rule 15": KOTBItemData(
        code=8675324,
        type=ItemClassification.progression,
    ),
    "Rule 16": KOTBItemData(
        code=8675325,
        type=ItemClassification.progression,
    ),
    "Rule 17": KOTBItemData(
        code=8675326,
        type=ItemClassification.filler,
    ),
    "Rule 18": KOTBItemData(
        code=8675327,
        type=ItemClassification.progression,
    ),
    "Rule 19": KOTBItemData(
        code=8675328,
        type=ItemClassification.filler,
        can_create=lambda world: False,
    ),
    "Rule 20": KOTBItemData(
        code=8675329,
        type=ItemClassification.filler,  # To become progression trap
    ),
    "Rule 21": KOTBItemData(
        code=8675330,
        type=ItemClassification.trap,
    ),
    "Rule 22": KOTBItemData(
        code=8675331,
        type=ItemClassification.progression,
    ),
    "Rule 23": KOTBItemData(
        code=8675332,
        type=ItemClassification.progression,
    ),
    "Rule 24": KOTBItemData(
        code=8675333,
        type=ItemClassification.progression,
    ),
    "Rule 25": KOTBItemData(
        code=8675334,
        type=ItemClassification.progression,
    ),
    "Rule 26": KOTBItemData(
        code=8675335,
        type=ItemClassification.progression,
    ),
    "Rule 27": KOTBItemData(
        code=8675336,
        type=ItemClassification.filler,
        can_create=lambda world: False,
    ),
    "Rule 28": KOTBItemData(
        code=8675337,
        type=ItemClassification.progression,
    ),
    "Rule 29": KOTBItemData(
        code=8675338,
        type=ItemClassification.progression,
    ),

    "Victory": KOTBItemData(
        type=ItemClassification.progression,
    ),
}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
