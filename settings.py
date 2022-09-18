"""
PV Simulator Settings File
"""

# Message client configuration
rabbitmq_host = 'rabbitmq'  # set the location of your RabbitMQ server
queue_name = 'energy'
exchange = ''
default_port = 5672 # For test case reference only

# Meter configuration whole number >= 1
sample_rate = 5

# Log file
results_file = 'pv_simulator_results.log'

