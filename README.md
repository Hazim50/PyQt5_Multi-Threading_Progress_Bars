<h1>PyQt5 Multi-Threading Progress Bars</h1>

<p>This project contains an example of designing an interface using the PyQt5 library and updating progress bars using multiple threads.</p>

<h2>How It Works</h2>

<ul>
    <li>There are three "Start" buttons on the main window. Each button starts a thread and updates a progress bar.</li>
    <li>Each thread increments a counter at a specific time interval and communicates this value to the main window by sending a signal.</li>
    <li>The main window receives the signal and updates the progress bar based on the sender's identity.</li>
    <li>Each thread has a corresponding "Stop" button to halt the thread.</li>
</ul>

<h2>Requirements</h2>

<ul>
    <li>Python 3.x</li>
    <li>PyQt5</li>
</ul>

<h2>Installation</h2>

<ol>
    <li>Clone the repository or download the ZIP file:</li>
    <code>git clone https://github.com/Hazim50/PyQt5-MultiThreading-ProgressBar.git</code>
    <li>Install the required libraries:</li>
    <code>pip install PyQt5</code>
    <li>Run the code:</li>
    <code>python PyQt5_Multi-Threading_Progress_Bars.py</code>
</ol>
