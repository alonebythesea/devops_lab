import json
import nose
from handlers.pulls import get_pulls


def check_state(state):
    try:
        json.dumps(get_pulls(state))
    except ValueError:
        return False
    return True


def test_json_accepted():
    nose.tools.ok_(check_state('accepted'), True)


def test_json_needs_work():
    nose.tools.ok_(check_state('needs work'), True)


def test_json_closed():
    nose.tools.ok_(check_state('closed'), True)


def test_json_open():
    nose.tools.ok_(check_state('open'), True)


def test_json_none():
    nose.tools.ok_(check_state(None), True)


if __name__ == '__main__':
    nose.run()
