import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_solution, calculate_happiness
import sys
from os.path import basename, normpath
import glob

# New ideas: 1) Brute force k, in other words, we increment k if our current k value does not return a valid output
# 2) If we hit our maximum k, we throw away any edge/pair of students that create a new breakout room

class BreakoutRoom:
    def __init__(self, id, first_student):
        self.id = 0 #Counter; increment by 1 every time we create a new BreakoutRoom
        self.stress = 0
        self.happiness = 0
        self.students = set()
        self.initialize_student(first_student)

    # private method
    def initialize_student(self, edges, student1):
        # Base Case: Add our first student to the breakout room
        # Still keep stress and happiness to 0
        # Add our first student1 to the student set
        #
        # Loop through all students/breakout rooms not in this BreakoutRoom, 
        # call our current iteration student/breakout room: w
        # Find the edge from (w, student1)/(student1, w)
        # Delete edge from (w, student1)/(student1, w)
        # Add a new edge (w, this breakout room) with the same weight of edge (w, student1)
        # 
        # Return new edge list
        self.students.add(student1)
        for edge, weights in edges.items():
            u, v = edge[0], edge[1]
            if u == student1:
                del edges[edge]
                # possible bug: object isn't hashable
                edges[(self, v)] = weights
            elif v == student1:
                del edges[edge]
                edges[(u, self)] = weights
        return edges

    # adds a student to this breakout room; returns new edge list
    def add_student(self, edges, student, s, k):
        """Given the edges dictionary, stress budget s, and number of breakout rooms k, adds the specified student to
        this breakout room."""
        if student in self.students:
            print("This student is already in this breakout room")
            return
        
        # used for calculating the summed phantom edges
        # key: the node connected to this breakout room
        # value: dictionary with "happiness" and "stress"
        new_edges = {}

        for edge in edges:
            u, v = edge[0], edge[1]
            if type(u) == BreakoutRoom and u.id == self.id:
                if v == student:
                    student_found = True
                    # Initialize variables u=BreakoutRoom and v=student
                    # Check that this does not exceed our S_max / k. 
                    # If it does, then we return an Exception saying we exceed S_max / k
                    #
                    # Otherwise,
                    # Add v to the student set (actually, this is done at the end of the function)
                    # Add v's happiness&stress level to BreakoutRoom's happiness&stress level, 
                    # according to our edge weight connecting (u, v)
                    # Delete edge u-v
                    #
                    if self.stress + edges[edge]["stress"] > s / k:
                        # maybe change this to throwing an actual Python exception?
                        print("Stress budget exceeded in this breakout room")
                        return
                    
                    self.happiness += edges[edge]["happiness"] # kinda forget what get_edge_data dictionary looks like
                    self.stress += edges[edge]["stress"]
                    del edges[edge]

                if v not in self.students:
                    # Loop through all studentss&breakout rooms not in this BreakoutRoom, 
                    # call our current iteration student/breakout room: w
                    # Find edge (w, u)/(u, w) and (w, v)/(v, w)
                    # WLOG it's in the forward direction: 
                    # Add the weight of edge w-u and w-v to total weight: tw
                    # Delete the edge w-u and delete the edge w-v
                    # Create a brand new edge connecting w-u, with weight tw
                    # Add this edge
                    #
                    # After finishing the loop, we re-sort by our edge ratios
                    # Return our new edge list
                    if v not in new_edges:
                        new_edges[v] = {"happiness": 0, "stress": 0}
                    old_edge = edges[edge]
                    new_edges[v]["happiness"] += old_edge["happiness"]
                    new_edges[v]["stress"] += old_edge["stress"]
                    del edges[edge]

            elif type(v) == BreakoutRoom and v.id == self.id:
                # same code as above, just if u and v are swapped
                # (there might be a cleaner way to code this rather than this copy and paste shit)
                if u == student:
                    if self.stress + edges[edge]["stress"] > s / k:
                        # maybe change this to throwing an actual Python exception?
                        print("Stress budget exceeded in this breakout room")
                        return
                    
                    self.happiness += edges[edge]["happiness"] # kinda forget what get_edge_data dictionary looks like
                    self.stress += edges[edge]["stress"]
                    del edges[edge]

                if u not in self.students:
                    if u not in new_edges:
                        new_edges[u] = {"happiness": 0, "stress": 0}
                    old_edge = edges[edge]
                    new_edges[u]["happiness"] += old_edge["happiness"]
                    new_edges[u]["stress"] += old_edge["stress"]
                    del edges[edge]
                    
        self.students.add(student)
        
        for v, weights in new_edges.items():
            edges[(self, v)] = weights
        
        return edges

def solve(G, s):
    """
    Args:
        G: networkx.Graph
        s: stress_budget
    Returns:
        D: Dictionary mapping for student to breakout room r e.g. {0:2, 1:0, 2:1, 3:2}
        k: Number of breakout rooms
    """
    n = len(G.nodes)
    e = {}
    k = 0
    e_tuples = []
    for edge in G.edges:
        u, v = edge[0], edge[1]
        e[(u, v)] = G.get_edge_data(u, v)
        
    # Attempt 1: Choose the edge with highest happiness/stress ratio as first greedy algo
    # Attempt 2: Choose the edge with highest happiness
    # Attempt 3: Use hybrid

    # this is attempt 1
    def get_ratio(edge):
        happy = G.get_edge_data(edge[0], edge[1])['happiness']
        stress = G.get_edge_data(edge[0], edge[1])['stress']
        if stress == 0:
            return float('inf')
        return happy / stress
        
    sorted_edges = sorted(list(G.edges), key=get_ratio, reverse=True)

    for ed in list(sorted_edges):
        print(ed, G.get_edge_data(ed[0], ed[1])['happiness'], G.get_edge_data(ed[0], ed[1])['stress'], get_ratio(ed))
    
    # key: breakout room number, value: set of student numbers
    breakouts = {}
    for x in range(0, n/2 + 1):
        
    
    

    #print(e)
    return {}, k


# Here's an example of how to run your solver.

# Usage: python3 solver.py test.in

if __name__ == '__main__':
    assert len(sys.argv) == 2
    path = sys.argv[1]
    G, s = read_input_file(path)
    D, k = solve(G, s)
    assert is_valid_solution(D, G, s, k)
    print("Total Happiness: {}".format(calculate_happiness(D, G)))
    write_output_file(D, 'outputs/small-1.out')


# For testing a folder of inputs to create a folder of outputs, you can use glob (need to import it)
# if __name__ == '__main__':
#      inputs = glob.glob('inputs/*')
#      for input_path in inputs:
#          output_path = 'outputs/' + basename(normpath(input_path))[:-3] + '.out'
#          G, s = read_input_file(input_path)
#          D, k = solve(G, s)
#          assert is_valid_solution(D, G, s, k)
#          happiness = calculate_happiness(D, G)
#          write_output_file(D, output_path)
