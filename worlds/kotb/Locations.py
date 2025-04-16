from typing import Callable, Dict, NamedTuple, Optional, TYPE_CHECKING
from BaseClasses import Location

if TYPE_CHECKING:
    from . import KOTBWorld

LOCATION_OFFSET: int = 8675309


class KOTBLocation(Location):
    game = "KingOfTheBridge"


class KOTBLocationData(NamedTuple):
    region: str
    address: Optional[int] = None
    can_create: Callable[["KOTBWorld"], bool] = lambda world: True
    locked_item: Optional[str] = None


capture_locations: Dict[str, KOTBLocationData] = {
    "Capture Any Pawn": KOTBLocationData("Play", LOCATION_OFFSET + 0),
    "Capture Any Rook": KOTBLocationData("Play", LOCATION_OFFSET + 1),
    "Capture Any Knight": KOTBLocationData("Play", LOCATION_OFFSET + 2),
    "Capture Any Bishop": KOTBLocationData("Play", LOCATION_OFFSET + 3),
    "Capture Any King": KOTBLocationData("Play", LOCATION_OFFSET + 4),
    "Capture Any Queen": KOTBLocationData("Play", LOCATION_OFFSET + 5),
    "Capture Any Castle": KOTBLocationData("Play", LOCATION_OFFSET + 6),
    "Capture Any Landmine": KOTBLocationData("Play", LOCATION_OFFSET + 7),
}

capturesanity_locations: Dict[str, KOTBLocationData] = {
    "Capture A2 Pawn": KOTBLocationData("Play", LOCATION_OFFSET + 8),
    "Capture B2 Pawn": KOTBLocationData("Play", LOCATION_OFFSET + 9),
    "Capture C2 Pawn": KOTBLocationData("Play", LOCATION_OFFSET + 10),
    "Capture D2 Pawn": KOTBLocationData("Play", LOCATION_OFFSET + 11),
    "Capture E2 Pawn": KOTBLocationData("Play", LOCATION_OFFSET + 12),
    "Capture F2 Pawn": KOTBLocationData("Play", LOCATION_OFFSET + 13),
    "Capture G2 Pawn": KOTBLocationData("Play", LOCATION_OFFSET + 14),
    "Capture H2 Pawn": KOTBLocationData("Play", LOCATION_OFFSET + 15),
    "Capture A1 Rook": KOTBLocationData("Play", LOCATION_OFFSET + 16),
    "Capture H1 Rook": KOTBLocationData("Play", LOCATION_OFFSET + 17),
    "Capture B1 Knight": KOTBLocationData("Play", LOCATION_OFFSET + 18),
    "Capture G1 Knight": KOTBLocationData("Play", LOCATION_OFFSET + 19),
    "Capture C1 Bishop": KOTBLocationData("Play", LOCATION_OFFSET + 20),
    "Capture F1 Bishop": KOTBLocationData("Play", LOCATION_OFFSET + 21),
}

kingsanity_locations: Dict[str, KOTBLocationData] = {
    "Capture A1 King": KOTBLocationData("Disabled", LOCATION_OFFSET + 22),
    "Capture A2 King": KOTBLocationData("Disabled", LOCATION_OFFSET + 23),
    "Capture B1 King": KOTBLocationData("Disabled", LOCATION_OFFSET + 24),
    "Capture B2 King": KOTBLocationData("Disabled", LOCATION_OFFSET + 25),
    "Capture C1 King": KOTBLocationData("Disabled", LOCATION_OFFSET + 26),
    "Capture C2 King": KOTBLocationData("Disabled", LOCATION_OFFSET + 27),
    "Capture D1 King": KOTBLocationData("Disabled", LOCATION_OFFSET + 28),
    "Capture D2 King": KOTBLocationData("Disabled", LOCATION_OFFSET + 29),
    "Capture E1 King": KOTBLocationData("Disabled", LOCATION_OFFSET + 30),
    "Capture E2 King": KOTBLocationData("Disabled", LOCATION_OFFSET + 31),
    "Capture F1 King": KOTBLocationData("Disabled", LOCATION_OFFSET + 32),
    "Capture F2 King": KOTBLocationData("Disabled", LOCATION_OFFSET + 33),
    "Capture G1 King": KOTBLocationData("Disabled", LOCATION_OFFSET + 34),
    "Capture G2 King": KOTBLocationData("Disabled", LOCATION_OFFSET + 35),
    "Capture H1 King": KOTBLocationData("Disabled", LOCATION_OFFSET + 36),
    "Capture H2 King": KOTBLocationData("Disabled", LOCATION_OFFSET + 37),
}

rulesanity_locations: Dict[str, KOTBLocationData] = {
    "Break rule 00": KOTBLocationData("Play", LOCATION_OFFSET + 38),
    "Break rule 01": KOTBLocationData("Disabled", LOCATION_OFFSET + 39),
    "Break rule 02": KOTBLocationData("Play", LOCATION_OFFSET + 40),
    "Break rule 03": KOTBLocationData("Disabled", LOCATION_OFFSET + 41),
    "Break rule 04": KOTBLocationData("Play", LOCATION_OFFSET + 42),
    "Break rule 05": KOTBLocationData("Disabled", LOCATION_OFFSET + 43),
    "Break rule 06": KOTBLocationData("Play", LOCATION_OFFSET + 44),
    "Break rule 07": KOTBLocationData("Play", LOCATION_OFFSET + 45),
    "Break rule 08": KOTBLocationData("Disabled", LOCATION_OFFSET + 46),
    "Break rule 09": KOTBLocationData("Play", LOCATION_OFFSET + 47),
    "Break rule 10": KOTBLocationData("Disabled", LOCATION_OFFSET + 48),
    "Break rule 11": KOTBLocationData("Disabled", LOCATION_OFFSET + 49),
    "Break rule 12": KOTBLocationData("Play", LOCATION_OFFSET + 50),
    "Break rule 13": KOTBLocationData("Play", LOCATION_OFFSET + 51),
    "Break rule 14": KOTBLocationData("Play", LOCATION_OFFSET + 52),
    "Break rule 15": KOTBLocationData("Disabled", LOCATION_OFFSET + 53),
    "Break rule 16": KOTBLocationData("Disabled", LOCATION_OFFSET + 54),
    "Break rule 17": KOTBLocationData("Disabled", LOCATION_OFFSET + 55),
    "Break rule 18": KOTBLocationData("Play", LOCATION_OFFSET + 56),
    "Break rule 19": KOTBLocationData("Disabled", LOCATION_OFFSET + 57),
    "Break rule 20": KOTBLocationData("Disabled", LOCATION_OFFSET + 58),
    "Break rule 21": KOTBLocationData("Disabled", LOCATION_OFFSET + 59),
    "Break rule 22": KOTBLocationData("Disabled", LOCATION_OFFSET + 60),
    "Break rule 23": KOTBLocationData("Disabled", LOCATION_OFFSET + 61),
    "Break rule 24": KOTBLocationData("Play", LOCATION_OFFSET + 62),
    "Break rule 25": KOTBLocationData("Play", LOCATION_OFFSET + 63),
    "Break rule 26": KOTBLocationData("Play", LOCATION_OFFSET + 64),
    "Break rule 27": KOTBLocationData("Disabled", LOCATION_OFFSET + 65),
    "Break rule 28": KOTBLocationData("Play", LOCATION_OFFSET + 66),
    "Break rule 29": KOTBLocationData("Play", LOCATION_OFFSET + 67),
}

achievementsanity_locations: Dict[str, KOTBLocationData] = {
    "Achievement : Title Drop": KOTBLocationData("Pregame", LOCATION_OFFSET + 68),
    "Achievement : Forgot My Breadcrumbs": KOTBLocationData("Pregame", LOCATION_OFFSET + 69),
    "Achievement : Doubling Profits": KOTBLocationData("Play", LOCATION_OFFSET + 70),
    "Achievement : Altruist": KOTBLocationData("Play", LOCATION_OFFSET + 71),
    "Achievement : Slay Queen": KOTBLocationData("Play", LOCATION_OFFSET + 72),
    "Achievement : To infinity!": KOTBLocationData("Pregame", LOCATION_OFFSET + 73),
    "Achievement : Philanthropist": KOTBLocationData("Play", LOCATION_OFFSET + 74),
    "Achievement : Double Kill": KOTBLocationData("Play", LOCATION_OFFSET + 75),
    "Achievement : Triple Kill": KOTBLocationData("Play", LOCATION_OFFSET + 76),
    "Achievement : Fooled You Twice": KOTBLocationData("Endgame", LOCATION_OFFSET + 77),
    "Achievement : Oblivious": KOTBLocationData("Play", LOCATION_OFFSET + 78),
    "Achievement : Clairvoyance": KOTBLocationData("Disabled", LOCATION_OFFSET + 79),
    "Achievement : Royal Buffet": KOTBLocationData("Play", LOCATION_OFFSET + 80),
    "Achievement : Stickler": KOTBLocationData("Play", LOCATION_OFFSET + 81),
    "Achievement : Enforcer": KOTBLocationData("Play", LOCATION_OFFSET + 82),
    "Achievement : Tough Luck?": KOTBLocationData("Play", LOCATION_OFFSET + 83),
    "Achievement : Overkill": KOTBLocationData("Endgame", LOCATION_OFFSET + 84),
    "Achievement : Gempire": KOTBLocationData("Play", LOCATION_OFFSET + 85),
    "Achievement : Exclusion": KOTBLocationData("Play", LOCATION_OFFSET + 86),
    "Achievement : Foreshadowing": KOTBLocationData("Pregame", LOCATION_OFFSET + 87),
    "Achievement : A Legal Affair": KOTBLocationData("Play", LOCATION_OFFSET + 88),
    "Achievement : Juggler": KOTBLocationData("Endgame", LOCATION_OFFSET + 89),
    "Achievement : Regal Rally": KOTBLocationData("Endgame", LOCATION_OFFSET + 90),
    "Achievement : Showdown!": KOTBLocationData("Endgame", LOCATION_OFFSET + 91),
    "Achievement : Forceful Friendship": KOTBLocationData("Play", LOCATION_OFFSET + 92),
    "Achievement : King of the Bridge": KOTBLocationData("Disabled", LOCATION_OFFSET + 93),
}

achievementsanity_plus_locations: Dict[str, KOTBLocationData] = {
    "Achievement : Bon Voyage!": KOTBLocationData("Play", LOCATION_OFFSET + 94),
    "Achievement : Junior Game Designer": KOTBLocationData("Endgame", LOCATION_OFFSET + 95),
    "Achievement : Happy Ever After": KOTBLocationData("Endgame", LOCATION_OFFSET + 96),
    "Achievement : Bookworm": KOTBLocationData("Disabled", LOCATION_OFFSET + 97),
    "Achievement : Rule Savant": KOTBLocationData("Disabled", LOCATION_OFFSET + 98),
    "Achievement : Impatience": KOTBLocationData("Disabled", LOCATION_OFFSET + 99),
    "Achievement : Rush Hour": KOTBLocationData("Disabled", LOCATION_OFFSET + 100),
    "Achievement : Rocket Science I": KOTBLocationData("Endgame", LOCATION_OFFSET + 101),
    "Achievement : Rocket Science II": KOTBLocationData("Endgame", LOCATION_OFFSET + 102),
    "Achievement : Rocket Science III": KOTBLocationData("Endgame", LOCATION_OFFSET + 103),
    "Achievement : The Great Beyond": KOTBLocationData("Endgame", LOCATION_OFFSET + 104),
}

all_locations = {**achievementsanity_locations, **achievementsanity_plus_locations, **capturesanity_locations,
                 **capture_locations, **rulesanity_locations, **kingsanity_locations}

location_table = {name: data.address for name, data in all_locations.items() if data.address is not None}
locked_locations = {name: data for name, data in all_locations.items() if data.locked_item}
