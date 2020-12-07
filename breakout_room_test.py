import pprint
from solver import BreakoutRoom


def weight_dict(happiness, stress):
    return {"happiness": happiness, "stress": stress}

def two_rooms_quality_test():
    """Prints the edges dictionary as we do breakout room operations"""
    print("===TEST: printing edge list to ensure breakout room functionality")
    pp = pprint.PrettyPrinter()

    s = 100
    k = 2

    edges = {(0, 1): weight_dict(1, 1),
            (0, 2): weight_dict(4, 1),
            (0, 3): weight_dict(6, 1),
            (1, 2): weight_dict(2, 1),
            (1, 3): weight_dict(3, 1),
            (2, 3): weight_dict(5, 1)}
            
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

    b0.add_student(2, s, k)
    print("After placing student 2 into breakout 0:")
    pp.pprint(edges)
    print()

    b1 = BreakoutRoom(1, edges, 3)
    print("After placing student 3 into breakout 1:")
    pp.pprint(edges)
    print()

    print("Testing breakout room happiness and stress levels...")
    assert b0.happiness == 7
    assert b0.stress == 3
    assert b1.happiness == 0
    assert b1.stress == 0
    print("PASSED\n")

def single_room():
    """Tests that internal breakout room happiness and stress is calculated correctly"""
    pp = pprint.PrettyPrinter()

    print("===TEST: testing a single room's happiness and stress is calculated correctly...")
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
    print(f"After placing student 0 into breakout 0:")
    pp.pprint(edges)
    print()

    for i in range(1, 4):
        b0.add_student(i, s, k)
        print(f"After placing student {i} into breakout 0:")
        pp.pprint(edges)
        print()

    print("Testing breakout room happiness and stress levels...")
    assert b0.happiness == 1 + 11 + 94 + 11 + 4 + 0
    assert b0.stress == 11 + 23 + 11 + 11 + 0 + 11
    print("PASSED\n")

def test_max_stress_capacity():
    """Tests that a student will not be added if it would exceed the stress capacity."""
    """Expected output: Stress exceeded! solver.py line 79. If doesn't print, we have a problem"""

    print("===TEST: printing edge list to ensure breakout room functionality")
    pp = pprint.PrettyPrinter()

    s = 100
    k = 2

    edges = {(0, 1): weight_dict(1, 1),
            (2, 0): weight_dict(4, 69),
            (3, 0): weight_dict(6, 1),
            (1, 2): weight_dict(2, 1),
            (3, 1): weight_dict(3, 1),
            (2, 3): weight_dict(5, 1)}
            
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

    b0.add_student(2, s, k)
    print("After placing student 2 into breakout 0:")
    pp.pprint(edges)
    print()

    b1 = BreakoutRoom(1, edges, 3)
    print("After placing student 3 into breakout 1:")
    pp.pprint(edges)
    print()

    print("Testing breakout room happiness and stress levels...")
    assert b0.happiness == 7
    assert b0.stress == 71
    assert b1.happiness == 0
    assert b1.stress == 0
    print("FAILED\n")
    

if __name__ == "__main__":
    two_rooms_quality_test()
    single_room()
    test_max_stress_capacity()
