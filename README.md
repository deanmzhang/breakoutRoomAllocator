2020 has been a stressful year, and course staff is trying to reduce student stress and increase student happiness
as much as possible. Since school has been reduced to a series of awkward Zoom breakout rooms, we figured this is
a good place to start. We noticed that student stress and happiness fluctuate greatly depending on how they are split
into breakout rooms, so we are looking to find a way to divide up stressed students to make them a little happier.

Your job is to place n students into Zoom breakout rooms. For each pair of students i and j, there is one value quantifying how much happiness these two students give each other and one value quantifying how much stress
they give each other. The total happiness value of a room is the sum of the happiness values of every student
pair in that room, and the total stress value of a room is the sum of the stress values of every student pair in
that room. Knowing that trying to eliminate student stress is impossible, we have settled with keeping total student
stress low enough so that it does not surpass S_max/k in each room, where k is the number of breakout rooms you
choose to open. Your goal is to maximize total happiness H_total across all rooms, while keeping the total stress below
the threshold S_max/k in each room.

Requirements:

Python 3.6+

You'll only need to install networkx to work with the starter code. For installation instructions, follow: https://networkx.github.io/documentation/stable/install.html

If using pip to download, run `python3 -m pip install networkx`


Files:
- `parse.py`: functions to read/write inputs and outputs
- `solver.py`: where you should be writing your code to solve inputs
- `utils.py`: contains functions to compute cost and validate NetworkX graphs

When writing inputs/outputs:
- Make sure you use the functions `write_input_file` and `write_output_file` provided
- Run the functions `read_input_file` and `read_output_file` to validate your files before submitting!
- These are the functions run by the autograder to validate submissions

Credit to CS170 Course Staff
