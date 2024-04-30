class Board:
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')
        self.closed = data.get('closed')
        self.permission_level = data.get('prefs', {}).get('permissionLevel')
        self.voting = data.get('prefs', {}).get('voting')
        self.comments = data.get('prefs', {}).get('comments')
        self.self_join = data.get('prefs', {}).get('selfJoin')
        self.card_covers = data.get('prefs', {}).get('cardCovers')
        self.background = data.get('prefs', {}).get('background')


def assert_properties(obj, expected_props):
    """
    Assert properties of an object.
    :param obj: Object, the object whose properties are to be validated
    :param expected_props: dict, a dictionary of properties and their expected values
    """
    for prop, value in expected_props.items():
        assert getattr(obj, prop) == value, f"'{prop}' should be '{value}', but got '{getattr(obj, prop)}'"


