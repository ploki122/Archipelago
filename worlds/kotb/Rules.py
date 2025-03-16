from typing import Callable, TYPE_CHECKING
from enum import StrEnum
from BaseClasses import CollectionState
from ..generic.Rules import CollectionRule

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
    world: "KOTBWorld"
    capture_rules: dict[str, CollectionRule]
    rule_break_rules: dict[str, CollectionRule]
    goal_rules: dict[str, CollectionRule]
    # def get_capture_rule(world: "KOTBWorld", piece: str) -> Callable[[CollectionState], bool]:
    #     if piece == "pawn":
    #         return lambda state: (state.has_any([Rules.MOVE_PAWN, Rules.MOVE_KNIGHT], world.player) or
    #                               can_move_bishop_fully(world) or
    #                               can_move_rook_fully(world) or
    #                               can_kill_enemies_on_mines(world))
    #
    #     if piece == "bishop":
    #         return can_move_bishop_fully(world) or can_kill_enemies_on_mines(world)
    #
    #     if piece == "knight":
    #         return can_move_bishop_fully(world) or can_kill_enemies_on_mines(world) or can_move_rook_fully(world)
    #
    #     if piece == "rook":
    #         return can_move_bishop_fully(world) or can_kill_enemies_on_mines(world) or can_move_rook_fully(world)
    #
    #     if piece == "queen":
    #         return can_move_bishop_fully(world) or can_kill_enemies_on_mines(world) or can_move_rook_fully(world)
    #
    #     if piece == "king":
    #         return can_move_bishop_fully(world) or can_kill_enemies_on_mines(world) or can_move_rook_fully(world)
    #
    #     if piece == "castle":
    #         return can_move_bishop_fully(world) or can_kill_enemies_on_mines(world) or can_move_rook_fully(world)
    #
    #     if piece == "landmine":
    #     return lambda state: state.has_all([Rules.MOVE_BISHOP, Rules.MOVE_PAWN, Rules.GAME_BISHOP_GIFT], world.player)
    #
    #     return lambda state: True

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
