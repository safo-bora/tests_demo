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


class BoardList:
    def __init__(self, data):
        if isinstance(data, list):
            self.lists = list(BoardList(data) for data in data)
        else:
            self.id = data.get('id')
            self.name = data.get('name')
            self.closed = data.get('closed')
            self.pos = data.get('pos')
            self.soft_limit = data.get('softLimit')
            self.id_board = data.get('idBoard')
            self.subscribed = data.get('subscribed')
            self.limits = data.get('limits')
            self.color = data.get('color')


class Card:
    def __init__(self, data):
        if isinstance(data, list):
            self.cards = list(Card(data) for data in data)
        else:
            self.id = data.get('id')
            self.address = data.get('address')
            self.badges = data.get('badges')
            self.name = data.get('name')
            self.pos = data.get('pos')
            self.subscribed = data.get('subscribed')


class Label:
    def __init__(self, data):
        if isinstance(data, list):
            self.labels_list = list(Label(data) for data in data)
            self.json = data
        else:
            self.id = data.get('id')
            self.id_board = data.get('id_board')
            self.name = data.get('name')
            self.uses = data.get('uses')
            self.color = data.get('color')


class Membership:
    def __init__(self, data):
        if isinstance(data, list):
            self.memberships_list = list(Membership(data) for data in data)
            self.json = data
        else:
            self.id = data.get('id')
            self.id_member = data.get('idMember')
            self.member_type = data.get('memberType')
            self.unconfirmed = data.get('unconfirmed')
            self.deactivated = data.get('deactivated')


class Action:
    def __init__(self, data):
        if isinstance(data, list):
            self.actions_list = list(Action(data) for data in data)
            self.json = data
        else:
            self.id = data.get('id')
            self.date = data.get('date')
            self.member_creator = data.get('memberCreator')
            self.id_member_creator = data.get('idMemberCreator')
            self.board_id = data.get('data', {}).get('board', {}).get('id')
            self.board_name = data.get('data', {}).get('board', {}).get('name')
            self.card_id = data.get('data', {}).get('card', {}).get('id')
            self.card_name = data.get('data', {}).get('card', {}).get('id')


def assert_properties(obj, expected_props):
    """
    Assert properties of an object.
    :param obj: Object, the object whose properties are to be validated
    :param expected_props: dict, a dictionary of properties and their expected values
    """
    for prop, value in expected_props.items():
        assert getattr(obj, prop) == value, f"'{prop}' should be '{value}', but got '{getattr(obj, prop)}'"
