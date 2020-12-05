import pprint
from solver import BreakoutRoom


def weight_dict(happiness, stress):
    return {"happiness": happiness, "stress": stress}

def print_two_rooms():
    """Prints the edges dictionary as we do breakout room operations"""
    pp = pprint.PrettyPrinter()

    s = 100000000000
    k = 2

    edges = {(0, 1): weight_dict(1, 11),
            (0, 2): weight_dict(11, 23),
            (0, 3): weight_dict(94, 11),
            (1, 2): weight_dict(11, 11),
            (1, 3): weight_dict(4, 0),
            (2, 3): weight_dict(0, 11)}
    print("Original edges:")
    pp.pprint(edges)
    print()

    b0 = BreakoutRoom(0, edges, 0)
    print("After placing student 0 into breakout 0:")
    pp.pprint(edges)
    print()

    b0.add_student(1, s, k)
    print("After placing student 1 into breakout 0:")
    pp.pprint(edges)
    print()

    b1 = BreakoutRoom(1, edges, 2)
    print("After placing student 2 into breakout 1:")
    pp.pprint(edges)
    print()

    b1.add_student(3, s, k)
    print("After placing student 3 into breakout 1:")
    pp.pprint(edges)
    print()

    print("Testing breakout room happiness and stress levels...")
    assert b0.happiness == 1
    assert b0.stress == 11
    assert b1.happiness == 0
    assert b1.stress == 11
    print("PASSED")


if __name__ == "__main__":
    print_two_rooms()
