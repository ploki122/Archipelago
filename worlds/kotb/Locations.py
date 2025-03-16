from typing import Callable, Dict, NamedTuple, Optional, TYPE_CHECKING, List

from BaseClasses import Location

if TYPE_CHECKING:
    from . import KOTBWorld, KOTBItem


class KOTBLocation(Location):
    game = "KingOfTheBridge"


class KOTBLocationData(NamedTuple):
    region: str
    address: Optional[int] = None
    can_create: Callable[["KOTBWorld"], bool] = lambda world: True
    locked_item: Optional[str] = None
    is_rule: bool = False
    is_capture: bool = False


location_data_table: Dict[str, KOTBLocationData] = {
    "Capture Pawn": KOTBLocationData(
        region="Act 1",
        address=8675309,
        is_capture=True,
    ),
    "Capture Bishop": KOTBLocationData(
        region="Act 1",
        address=8675310,
        is_capture=True,
    ),
    "Capture Rook": KOTBLocationData(
        region="Act 1",
        address=8675311,
        is_capture=True,
    ),
    "Capture King": KOTBLocationData(
        region="Act 1",
        address=8675312,
        is_capture=True,
    ),
    "Capture Queen": KOTBLocationData(
        region="Act 1",
        address=8675313,
        is_capture=True,
    ),
    "Capture Knight": KOTBLocationData(
        region="Act 1",
        address=8675314,
        is_capture=True,
    ),
    "Capture Castle": KOTBLocationData(
        region="Act 1",
        address=8675315,
        is_capture=True,
    ),
    "Capture Landmine": KOTBLocationData(
        region="Act 1",
        address=8675316,
        is_capture=True,
    ),
    "Break rule 00": KOTBLocationData(
        region="Act 1",
        address=8675320,
        is_rule=True,
    ),
    "Break rule 01": KOTBLocationData(
        region="Act 1",
        address=8675321,
        can_create=lambda world: False,
        is_rule=True,
    ),
    "Break rule 02": KOTBLocationData(
        region="Act 1",
        address=8675322,
        is_rule=True,
    ),
    "Break rule 03": KOTBLocationData(
        region="Act 1",
        address=8675323,
        can_create=lambda world: False,
        is_rule=True,
    ),
    "Break rule 04": KOTBLocationData(
        region="Act 1",
        address=8675324,
        is_rule=True,
    ),
    "Break rule 05": KOTBLocationData(
        region="Act 1",
        address=8675325,
        can_create=lambda world: False,
        is_rule=True,
    ),
    "Break rule 06": KOTBLocationData(
        region="Act 1",
        address=8675326,
        is_rule=True,
    ),
    "Break rule 07": KOTBLocationData(
        region="Act 1",
        address=8675327,
        is_rule=True,
    ),
    "Break rule 08": KOTBLocationData(
        region="Act 1",
        address=8675328,
        can_create=lambda world: False,
        is_rule=True,
    ),
    "Break rule 09": KOTBLocationData(
        region="Act 1",
        address=8675329,
        is_rule=True,
    ),
    "Break rule 10": KOTBLocationData(
        region="Act 1",
        address=8675330,
        can_create=lambda world: False,
        is_rule=True,
    ),
    "Break rule 11": KOTBLocationData(
        region="Act 1",
        address=8675331,
        can_create=lambda world: False,
        is_rule=True,
    ),
    "Break rule 12": KOTBLocationData(
        region="Act 1",
        address=8675332,
        is_rule=True,
    ),
    "Break rule 13": KOTBLocationData(
        region="Act 1",
        address=8675333,
        is_rule=True,
    ),
    "Break rule 14": KOTBLocationData(
        region="Act 1",
        address=8675334,
        is_rule=True,
    ),
    "Break rule 15": KOTBLocationData(
        region="Act 1",
        address=8675335,
        is_rule=True,
    ),
    "Break rule 16": KOTBLocationData(
        region="Act 1",
        address=8675336,
        can_create=lambda world: False,
        is_rule=True,
    ),
    "Break rule 17": KOTBLocationData(
        region="Act 1",
        address=8675337,
        can_create=lambda world: False,
        is_rule=True,
    ),
    "Break rule 18": KOTBLocationData(
        region="Act 1",
        address=8675338,
        is_rule=True,
    ),
    "Break rule 19": KOTBLocationData(
        region="Act 1",
        address=8675339,
        can_create=lambda world: False,
        is_rule=True,
    ),
    "Break rule 20": KOTBLocationData(
        region="Act 1",
        address=8675340,
        can_create=lambda world: False,
        is_rule=True,
    ),
    "Break rule 21": KOTBLocationData(
        region="Act 1",
        address=8675341,
        can_create=lambda world: False,
        is_rule=True,
    ),
    "Break rule 22": KOTBLocationData(
        region="Act 1",
        address=8675342,
        can_create=lambda world: False,
        is_rule=True,
    ),
    "Break rule 23": KOTBLocationData(
        region="Act 1",
        address=8675343,
        can_create=lambda world: False,
        is_rule=True,
    ),
    "Break rule 24": KOTBLocationData(
        region="Act 1",
        address=8675344,
        is_rule=True,
    ),
    "Break rule 25": KOTBLocationData(
        region="Act 1",
        address=8675345,
        is_rule=True,
    ),
    "Break rule 26": KOTBLocationData(
        region="Act 1",
        address=8675346,
        is_rule=True,
    ),
    "Break rule 27": KOTBLocationData(
        region="Act 1",
        address=8675347,
        can_create=lambda world: False,
        is_rule=True,
    ),
    "Break rule 28": KOTBLocationData(
        region="Act 1",
        address=8675348,
        can_create=lambda world: False,
        is_rule=True,
    ),
    "Break rule 29": KOTBLocationData(
        region="Act 1",
        address=8675349,
        is_rule=True,
    ),
}

location_table = {name: data.address for name, data in location_data_table.items() if data.address is not None}
locked_locations = {name: data for name, data in location_data_table.items() if data.locked_item}
