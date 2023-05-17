import pm4py
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.objects.petri_net.exporter.variants.pnml import export_net as pnml_exporter




# Step 1: Install the required dependencies if not already installed
# !pip install pm4py

# Step 2: Import the necessary modules

# Step 3: Import the event log file using the XES importer
log = xes_importer.apply('datasets/production_2.xes')

# Step 4: Transform the event log into a Petri net
net, initial_marking, final_marking = pm4py.discover_petri_net_inductive(log)

# Step 5: Export the Petri net as a PNML file
pnml_exporter(net, initial_marking, 'production.pnml')