from enum import Enum


class LatencyOptimization(Enum):
    NONE = 0
    NORMAL = 1
    STRONG = 2
    MAX = 3
    MAX_WITH_NO_TEXT_NORMALIZER = 4
