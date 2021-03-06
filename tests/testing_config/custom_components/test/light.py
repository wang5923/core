"""
Provide a mock light platform.

Call init before using it in your tests to ensure clean test data.
"""
from homeassistant.components.light import Light
from homeassistant.const import STATE_OFF, STATE_ON

from tests.common import MockToggleEntity

ENTITIES = []


def init(empty=False):
    """Initialize the platform with entities."""
    global ENTITIES

    ENTITIES = (
        []
        if empty
        else [
            MockLight("Ceiling", STATE_ON),
            MockLight("Ceiling", STATE_OFF),
            MockLight(None, STATE_OFF),
        ]
    )


async def async_setup_platform(
    hass, config, async_add_entities_callback, discovery_info=None
):
    """Return mock entities."""
    async_add_entities_callback(ENTITIES)


class MockLight(MockToggleEntity, Light):
    """Mock light class."""

    brightness = None
    supported_features = 0
