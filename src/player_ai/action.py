from enum import Enum

class Action(Enum):
    DRIVE_FERRY = "Drive/Ferry"
    DIRECT_FLIGHT = "Direct Flight"
    CHARTER_FLIGHT = "Charter Flight"
    SHUTTLE_FLIGHT = "Shuttle Flight"
    BUILD_RESEARCH_STATION = "Build Research Station"
    TREAT_DISEASE = "Treat Disease"
    SHARE_KNOWLEDGE = "Share Knowledge"
    DISCOVER_CURE = "Discover Cure"
    PASS = "Pass"