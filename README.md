# R3-SoftwareTraining#2-VictoriaBuchanan

<h3>MILESTONE 1 - MAZE GENERATION CODE</h3>

<p>The code in <strong>Maze.py</strong> creates a maze in a 800x800 pixel grid with n rows and columns.  The program uses pygame to display the maze and runs on python2.</p>

<h4><strong>Image 1 - Generated maze for a 11x11 grid</strong></h4>
<img src="https://github.com/SG-Command/R3-SoftwareTraining-2-VictoriaBuchanan/blob/main/photos/MazeN11.JPG" width="500" height="500">

<p>The maze is generated using a Depth-first search recursive backtracker algorithm. The steps in this algorithm are as follows:</p>

<ol>
    <li>Mark the initial cell as visited and make it the current cell.</li>
    <li>While there are unvisited cells:</li>
    <ol>
        <li>If the current cell has any neighbours that are unvisited:</li>
        <ul>
            <li>Randomly choose one of the unvisited neighbouring cells.</li>
            <li>Append the current cell to the stack array.</li>
            <li>Remove the wall between the current cell and the neighbouring cell chosen.</li>
            <li>Change the current cell to the chosen neighbouring cell (make sure to mark it as visited).</li>
        </ul>
        <li>Else if the stack is not empty:</li>
            <ul>
                <li>Remove the top cell from the stack.</li>
                <li>Change the current cell to the removed cell.</li>
        </ul>
    </ol>
</ol>

<p>Immediately, when the program starts the maze begins to generate a n by n grid based on the value of n (located in the global variables). The code shows the maze being generated in real time and highlights the current cell where the program is in green.  Depending on the value of n, the maze may take several minutes to generate.  For example, when n = 50 the maze takes around 3min.</p>

<h4><strong>Image 2 - Generated maze for a 20x20 grid</strong></h4>
<img src="https://github.com/SG-Command/R3-SoftwareTraining-2-VictoriaBuchanan/blob/main/photos/MazeN20.JPG" width="500" height="500">

<h3>MILESTONE 2 - TCP COMMAND STREAM</h3>

<p>The server for the TCP commands is in the <strong>Maze2.py</strong> file. The client side of the TCP commands is in the <strong>Client.py</strong> file. Similar to the 
maze generating file the programs should be accessed using python2 (not python3). One thing to note about the TCP Command Stream is that each string sent is 54 characters long (which means that if any of these strings differ in length from that amount the formatting will look funny when it prints the strings sent on the client side.)</p>