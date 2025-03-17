from typing import TYPE_CHECKING
from enum import StrEnum
from BaseClasses import CollectionState
from ..generic.Rules import set_rule

if TYPE_CHECKING:
    from . import KOTBWorld


class Rules(StrEnum):
    ACCUSE_RIGHT = "Rule 00"
    ACCUSE_WRONG = "Rule 01"
    MOVE_OWN = "Rule 02"
    MOVE_QUEEN_OPP = "Rule 03"
    MOVE_PAWN = "Rule 04"
    JUNK_PLEBS = "Rule 05"
    MOVE_PAWN_BACK = "Rule 06"
    MOVE_KNIGHT = "Rule 07"
    JUNK_HORSE = "Rule 08"
    MOVE_KNIGHT_JUMP = "Rule 09"
    GAME_LOSE = "Rule 10"
    GAME_WIN = "Rule 11"
    MOVE_KING = "Rule 12"
    MOVE_BISHOP = "Rule 13"
    MOVE_ROOK = "Rule 14"
    MOVE_BISHOP_OUTSIDE = "Rule 15"
    GAME_ROOK_CASTLE = "Rule 16"
    GAME_CASTLE_SCRAPS = "Rule 17"
    MOVE_QUEEN = "Rule 18"
    JUNK_OLD = "Rule 19"
    GAME_PAWN_ASCEND = "Rule 20"
    GAME_QUEEN_FLIP = "Rule 21"
    GAME_BISHOP_GIFT = "Rule 22"
    GAME_ROOK_CAPTURE = "Rule 23"
    GAME_PIECE_OVERLAP = "Rule 24"
    GAME_MOVE_OUTSIDE = "Rule 25"
    MOVE_LANDMINE = "Rule 26"
    GAME_SLIPPERY_TILE = "Rule 27"
    MOVE_CASTLE = "Rule 28"
    GAME_QUEEN_AFFAIR = "Rule 29"


class KOTBRules:
    player: int

    def __init__(self, player: int):
        self.player = player

    # region Sub-rules
    def can_move_bishop(self, state: CollectionState) -> bool:
        return state.has(Rules.MOVE_BISHOP, self.player)

    def can_move_bishop_fully(self, state: CollectionState) -> bool:
        return state.has_all([Rules.MOVE_BISHOP, Rules.MOVE_BISHOP_OUTSIDE], self.player)

    def can_move_knight(self, state: CollectionState) -> bool:
        return state.has(Rules.MOVE_KNIGHT, self.player)

    def can_move_knight_fully(self, state: CollectionState) -> bool:
        return state.has(Rules.MOVE_KNIGHT_JUMP, self.player)

    def can_move_rook(self, state: CollectionState) -> bool:
        return state.has(Rules.MOVE_ROOK, self.player)

    def can_move_rook_self_capture(self, state: CollectionState) -> bool:
        return state.has_all([Rules.MOVE_ROOK, Rules.GAME_ROOK_CAPTURE], self.player)

    def can_move_pawn(self, state: CollectionState) -> bool:
        return state.has(Rules.MOVE_PAWN, self.player)

    def can_move_pawn_fully(self, state: CollectionState) -> bool:
        return state.has_all([Rules.MOVE_PAWN, Rules.MOVE_PAWN_BACK], self.player)

    def can_move_queen(self, state: CollectionState) -> bool:
        return state.has(Rules.MOVE_QUEEN, self.player)

    def can_move_enemy_queen(self, state: CollectionState) -> bool:
        return state.has_all([Rules.MOVE_QUEEN, Rules.MOVE_QUEEN_OPP], self.player)

    def can_move_king(self, state: CollectionState) -> bool:
        return state.has_all([Rules.MOVE_KING], self.player)

    def can_accuse_of_cheating(self, state: CollectionState) -> bool:
        return state.has(Rules.ACCUSE_RIGHT, self.player)

    def can_castle(self, state: CollectionState) -> bool:
        return state.has_all([Rules.MOVE_ROOK, Rules.GAME_ROOK_CASTLE], self.player)

    def can_lay_mines(self, state: CollectionState) -> bool:
        return (state.has_all([Rules.MOVE_BISHOP, Rules.GAME_BISHOP_GIFT], self.player)
                and state.has_any([Rules.MOVE_BISHOP_OUTSIDE, Rules.MOVE_PAWN], self.player))

    def can_kill_enemies_on_mines(self, state: CollectionState) -> bool:
        return self.can_lay_mines(state) and self.can_accuse_of_cheating(state)

    def can_capture_pawn(self, state: CollectionState) -> bool:
        return (self.can_move_pawn(state) or self.can_move_bishop_fully(state) or self.can_move_knight_fully(state) or
                self.can_move_rook_self_capture(state))

    def can_capture_pieces(self, state: CollectionState) -> bool:
        return self.can_move_pawn(state) and (self.can_capture_pawn(state) or self.can_move_knight_fully(state) or
                                              self.can_move_rook_self_capture(state) or self.can_move_queen(state))

    def can_capture_everything(self, state: CollectionState) -> bool:
        return (self.can_move_pawn(state) and self.can_move_bishop_fully(state) and self.can_move_knight_fully(state)
                and self.can_move_queen(state) and self.can_move_rook(state))

    def can_capture_bishop(self, state: CollectionState) -> bool:
        return self.can_capture_pieces(state) and self.can_move_bishop_fully(state)

    def can_capture_knight(self, state: CollectionState) -> bool:
        return self.can_capture_pawn(state)

    def can_capture_rook(self, state: CollectionState) -> bool:
        return self.can_castle(state) or self.can_capture_pieces(state)

    def can_capture_queen(self, state: CollectionState) -> bool:
        return self.can_capture_pieces(state) or (self.can_capture_pawn(state) and self.can_move_enemy_queen(state))

    def can_capture_king(self, state: CollectionState) -> bool:
        return self.can_capture_pieces(state)

    def can_capture_castle(self, state: CollectionState) -> bool:
        return self.can_castle(state) and self.can_accuse_of_cheating(state)

    def can_capture_landmine(self, state: CollectionState) -> bool:
        return self.can_capture_pieces(state) or self.can_lay_mines(state)
    # endregion


def set_location_rules(world: "KOTBWorld", player: int) -> None:
    rules: KOTBRules = KOTBRules(player)

    # Captures
    set_rule(world.get_location("Capture Pawn"),
             lambda state: rules.can_capture_pawn(state))
    set_rule(world.get_location("Capture Bishop"),
             lambda state: rules.can_capture_bishop(state))
    set_rule(world.get_location("Capture Rook"),
             lambda state: rules.can_capture_rook(state))
    set_rule(world.get_location("Capture King"),
             lambda state: rules.can_capture_king(state))
    set_rule(world.get_location("Capture Queen"),
             lambda state: rules.can_capture_queen(state))
    set_rule(world.get_location("Capture Knight"),
             lambda state: rules.can_capture_knight(state))
    set_rule(world.get_location("Capture Castle"),
             lambda state: rules.can_capture_castle(state))
    set_rule(world.get_location("Capture Landmine"),
             lambda state: rules.can_capture_landmine(state))

    # Rule breaks
    set_rule(world.get_location("Break rule 00"),
             lambda state: rules.can_accuse_of_cheating(state))
    set_rule(world.get_location("Break rule 02"),
             lambda state: state.has("Rule 02", player))
    set_rule(world.get_location("Break rule 04"),
             lambda state: rules.can_move_pawn(state))
    set_rule(world.get_location("Break rule 06"),
             lambda state: rules.can_move_pawn_fully(state))
    set_rule(world.get_location("Break rule 07"),
             lambda state: rules.can_move_knight_fully(state) or
             (rules.can_move_knight(state) and rules.can_move_pawn(state)))
    set_rule(world.get_location("Break rule 09"),
             lambda state: state.has("Rule 09", player) and (rules.can_move_bishop(state) or rules.can_move_queen(state)
                                                             or rules.can_move_rook(state)))
    set_rule(world.get_location("Break rule 12"),
             lambda state: rules.can_move_king(state))
    set_rule(world.get_location("Break rule 13"),
             lambda state: rules.can_move_bishop(state))
    set_rule(world.get_location("Break rule 14"),
             lambda state: rules.can_move_rook(state))
    set_rule(world.get_location("Break rule 18"),
             lambda state: rules.can_move_queen(state))
    set_rule(world.get_location("Break rule 24"),
             lambda state: rules.can_capture_pawn(state))
    set_rule(world.get_location("Break rule 25"),
             lambda state: rules.can_move_knight(state) or rules.can_move_queen(state) or rules.can_move_rook(state)
             or rules.can_move_pawn(state) or rules.can_move_king(state))
    set_rule(world.get_location("Break rule 26"),
             lambda state: rules.can_lay_mines(state))
    set_rule(world.get_location("Break rule 28"),
             lambda state: rules.can_castle(state))
    set_rule(world.get_location("Break rule 29"),
             lambda state: rules.can_move_queen(state) and rules.can_capture_king(state))


def set_victory_rule(world: "KOTBWorld", player: int) -> None:
    rules: KOTBRules = KOTBRules(player)

    world.multiworld.completion_condition[player] = lambda state: rules.can_capture_everything(state)
