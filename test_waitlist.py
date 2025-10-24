import sys
import traceback

from waitlist import getPosition, popFront, addUsername, removeUsername, printWaitlist


def test_getPosition_found_and_not_found():
    wl = ["alice", "bob", "charlie"]
    # found
    assert getPosition("bob", wl) == 1
    # not found
    assert getPosition("dan", wl) == -1
    # original list must not be mutated by getPosition
    assert wl == ["alice", "bob", "charlie"]


def test_popFront_nonempty_and_empty():
    wl = ["alice", "bob"]
    name = popFront(wl)
    assert name == "alice"
    assert wl == ["bob"]

    name2 = popFront(wl)
    assert name2 == "bob"
    assert wl == []

    # popping empty waitlist returns None and leaves list unchanged
    assert popFront(wl) is None
    assert wl == []


def test_addUsername_adds_and_no_duplicate():
    wl = ["alice"]
    # add a new user
    assert addUsername("bob", wl) is True
    assert wl[-1] == "bob"

    before_len = len(wl)
    # adding an existing user should return False and not change the list
    assert addUsername("alice", wl) is False
    assert len(wl) == before_len


def test_removeUsername_remove_and_not_present():
    wl = ["alice", "bob", "charlie"]
    before_len = len(wl)
    # remove an existing user
    assert removeUsername("bob", wl) is True
    assert "bob" not in wl
    assert len(wl) == before_len - 1

    before_len = len(wl)
    # attempt to remove a non-existent user
    assert removeUsername("dan", wl) is False
    assert len(wl) == before_len


def test_printWaitlist_empty_and_nonempty():
    wl = []
    assert printWaitlist(wl) == "Waitlist Empty"

    wl = ["alice", "bob"]
    expected = "1:alice\n2:bob"
    assert printWaitlist(wl) == expected


def run_tests():
    tests = [
        test_getPosition_found_and_not_found,
        test_popFront_nonempty_and_empty,
        test_addUsername_adds_and_no_duplicate,
        test_removeUsername_remove_and_not_present,
        test_printWaitlist_empty_and_nonempty,
    ]
    failed = 0
    for t in tests:
        try:
            t()
            print(f"PASS: {t.__name__}")
        except AssertionError:
            failed += 1
            print(f"FAIL: {t.__name__}")
            traceback.print_exc()
        except Exception:
            failed += 1
            print(f"ERROR: {t.__name__}")
            traceback.print_exc()

    print(f"\nRan {len(tests)} tests: {len(tests)-failed} passed, {failed} failed")
    if failed:
        # non-zero exit code to indicate failure when used in CI or scripts
        sys.exit(1)


if __name__ == "__main__":
    run_tests()
