# R3-SoftwareTraining#2-VictoriaBuchanan

<h3>MILESTONE 1 - MAZE GENERATION CODE</h3>

<p>The code in <strong>Maze.py</strong> creates a maze in a 800x800 pixel grid with n rows and columns.  The program uses pygame to display the maze and runs on python2.  
The maze is generated using a Dept-first search recursive backtracker algorithm. The steps in this algorithm are as follows:</p>

<ol>
    <li>Mark the initial cell as visited and make it the current cell</li>
    <li>While there are unvisited cells:</li>
    <ol>
        <li>If the current cell has any neighbours that are unvisited:</li>
        <ul>
            <li>Randomly choose one of the unvisited neighbouring cells</li>
            <li>Append the current cell to the stack array</li>
            <li>Remove the wall between the current cell and the neighbouring cell chosen</li>
            <li>Change the chosen neighbouring cell to the current cell (make sure to mark it as visited)</li>
        </ul>
        <li>Else if the stack is not empty:</li>
            <ul>
                <li>Remove the top cell from the stack</li>
                <li>Make the removed cell the current cell</li>
        </ul>
    </ol>
</ol>

<h3>MILESTONE 2 - TCP COMMAND STREAM</h3>