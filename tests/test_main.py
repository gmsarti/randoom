from main import where_the_adventure_happen


def test_adventure_location():
    """Test that the function returns one of the expected locations."""

    valid_locations = ["forest", "cave", "dungeon"]
    location = where_the_adventure_happen()

    assert location in valid_locations, f"Unexpected location: {location}"
