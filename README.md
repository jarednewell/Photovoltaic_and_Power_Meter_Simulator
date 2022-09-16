<h1>PV Simulator</h1>

<h3>About</h3>
<p>
This application simulates the communication between an electricity meter and a
photovoltaic array. The kilowatt output of the array is based on a standard
distribution with a mean of 14:00 hours and a standard deviation of 2.5 hours.
</p>

<h3>Getting Started</h3>
<p>
Containerisation software is used in this deployment, specifically Docker.
This will require the operating specific installation and instructions to be
performed using the vendors website. However, this application can run on any 
operating system which supports Python 3.8 execution with an installation 
of a RabbitMQ message broker. The meter and photovoltaic simulator can be run 
independently. In the installation below these are combined as two threads
with the same container.
</p>

<h3>Prerequisites</h3>
<p>
To use Docker containerisation install docker 
<a href="https://docs.docker.com/get-docker/">
Docker</a>.

To use the Docker compose file provided install 
<a href="https://docs.docker.com/compose/install/"> Docker Compose</a> also.

For a custom RabbitMQ installation:

To use a PaaS or unique installation of RabbitMQ set the host in <b>settings.py
</b> changing the value <b>rabbitmq_host = 'example.rabbitmq{dot}com'</b> RabbitMQ install
can be found at <a href="https://www.rabbitmq.com/download.html"> RabbitMQ</a>

</p>
<h3>Installation</h3>
<p>
Using the docker compose file in this repo to install the application and the
supporting environment.
</p>
<ul>
<li> </li>
<li> Docker  </li>
<li> Docker  </li>
<li> Docker  </li>
</ul>

<h3>Usage</h3>
<p>
The output of the application is stored in a file call pv_simulator_results:
</p>
<p>
<b> Date/Time - Energy Meter - Photovoltaic Simulated Output - The Sum of the Energy 
Meter and The Photovoltaic Simulated Output</b>
<li>2022-09-14T09:03:01.677948+00:00 23.07 0.4 23.47</li> 
</p>

For more examples, please refer to the pv_simulator_results.log

<h3>License</h3>
GNU General Public License (GPLv3)

