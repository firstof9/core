"""Test availability of entities for the Z-Wave JS integration."""

from .common import BULB_6_MULTI_COLOR_LIGHT_ENTITY, ZEN_31_ENTITY


async def test_node_availability(
    hass, client, dead_node, bulb_6_multi_color, integration
):
    """Test a dead node for availability."""
    dead_node
    state = hass.states.get(ZEN_31_ENTITY)
    assert state.state == "unavailable"

    bulb_6_multi_color
    state = hass.states.get(BULB_6_MULTI_COLOR_LIGHT_ENTITY)
    assert state.state == "off"
