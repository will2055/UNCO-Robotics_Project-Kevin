# Project Kevin
Autonomous Navigation Prototype Platform Rover
<hr>
This project was started under and facilitated by: the Colorado Space Grant and Symposium Robotics Competition, UNCO Physics and Astronomy Department, and NASA.
<hr>
<h3>System Objective Introduction:</h3>
<p>This project is designed to develop an open source rover system based upon the Raspberry Pi micro-computers. In general, most introductory rover systems are prototyped using Arduinos and thier large variety of modules. The most popular microcontroller board is the Arduino UNO; which operates at 5V, 32KB flash memory, and 16MHz clock speed. The UNO presents several problems for a rover system.</p>
<p>The largest issue for the UNO is the 32KB flash memory. This 'write-once-then-read-only' memory structure works great for algorithmic self-performing tasks to interact with the physical enviroment in only one way. If you want to run a motor to move forward or start a power saving procedure based upon the analog data from a solar sensor then we are simply performing a task or take a chunk of data and perform and action. When we end the task, all relevant data is lost to make room for new data for those tasks. This poses a problem for a main use of rover systems, Data Collection. We can't truly save particular data for future analysis unless we use an expandable memory shield. This is adding another component onto the system. To maintain simplicity, the Raspberry Pi boards have an SD card memory already as a component of the base system since this is where the OS resides.</p>
<p>Our second problem is the clock speed, or processor speed. Both the Raspberry Pi's (currently) and the UNO have uniprocessor systems. This means that tasks are ran linearly, like a lunch line. The key difference is how fast can these systems process these tasks. For comparison; the Raspberry Pi Zero (W) runs at a clock speed of 1 GHz, while the UNO runs at a clock speed of 16MHz. This means that the Raspberry Pi Zero (W) is 62.5 times faster than the UNO. This is processing efficiency that is a key element in designing a rover system.</p>
<p>A less necessary comparison also deals with the power supply. The Arduino UNO has an operating voltage of 5 Volts and the Raspberry Pis operate at 5 Volts similarly. This indicates that there is no change necessary for moderate power supplies on an existing system. Furthermore, this means that changing from the UNO to the Pi will not fundementally change the system.</p>
<p>Since both components can accomplish the same tasks, with the same power supplies, but the Raspberry Pi is largely more efficient then the goal for this project to accopmlish this change while maintaing (or exceeding) existing system requirements.</p>
<h3>System Objective Description</h3>
<p>As mentioned above, the main goal is to design an autonomous navigation rover system.</p>
<p>This is accomplished by using a Raspberry Pi micro-computer (specifically the Zero (W)). The system will use the following modules for objective performance:</p>
<ol>
  <li>Xbee Series 1 Reciever</li>
  <li>L293DD Motor Driver</li>
  <li>Three Sharp IR Distance Sensors</li>
</ol>
<hr>
<footer>
  <p>More Updates to this project will be added over time. Stay tuned!</p>
  <p>For any inquiries, comments, or suggestions please email at brandon.w2055@gmail.com</p>
</footer>
