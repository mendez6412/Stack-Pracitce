from stack import Stack, InvalidCapacity, StackOverflow, StackUnderflow
from nose.tools import assert_raises


def test_capacity():
    s = Stack()
    assert s.capacity == 10


def test_invalid_capacity():
    assert_raises(InvalidCapacity, lambda: Stack(-1))


def test_len():
    s = Stack(capacity=5, values=[1, 2, 3])
    assert len(s) == 3


def test_is_empty():
    s = Stack()
    s2 = Stack(capacity=5, values=[1, 2, 3])
    assert s.is_empty()
    assert not s2.is_empty()


def test_push_value():
    s = Stack()
    s.push(2)
    assert len(s) == 1
    assert 2 in s.values


def test_push_value_to_end():
    s = Stack()
    s.push(2)
    s.push(3)
    assert s.values[-1] == 3


def test_pop():
    s = Stack()
    s.push(2)
    s.push(3)
    s.pop()
    assert s.values[-1] == 2
    assert 3 not in s.values
    assert len(s) == 1


def test_peek():
    s = Stack()
    s.push(2)
    s.push(3)
    assert s.peek() == 3
    assert len(s) == 2


def test_push_past_capacity():
    s = Stack(capacity=2)
    s.push(1)
    s.push(2)
    assert_raises(StackOverflow, lambda: s.push(3))


def test_initial_overflow():
    assert_raises(StackOverflow, lambda: Stack(capacity=2, values=[1, 2, 3]))


def test_pop_under_capacity():
    s = Stack(capacity=2)
    assert_raises(StackUnderflow, lambda: s.pop())


def test_find():
    s = Stack(capacity=10, values=[1, 2, 3])
    assert s.find(2) == 1


def test_find_nothing():
    s = Stack(capacity=10, values=[1, 2, 3])
    assert not s.find(4)


def test_stack_equals_identical_stack():
    s = Stack(capacity=10, values=[1, 2, 3])
    t = Stack(capacity=10, values=[1, 2, 3])
    assert s == t


def test_stack_equals_nonidentical_stack():
    s = Stack(capacity=10, values=[1, 2, 3])
    t = Stack(capacity=11, values=[1, 2, 3])
    assert not s == t


def test_stack_equals_nonidentical_stack2():
    s = Stack(capacity=10, values=[1, 2, 3])
    t = Stack(capacity=10, values=[1, 2, 3])
    t.push(4)
    assert not s == t


def test_str():
    s = Stack(capacity=3, values=[1, 2, 3])
    assert str(s) == "Capacity: 3 | Values: [1, 2, 3]"
