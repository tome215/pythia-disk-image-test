"""
Setup script for testing contents of the current Pythia disk image on CloudLab
"""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

# # Pick your OS.
# imageList = [
#     ('default', 'Default Image'),
#     ('urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU18-64-STD', 'UBUNTU 18.04'),
#     ('urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU20-64-STD', 'UBUNTU 20.04'),
#     ('urn:publicid:IDN+emulab.net+image+emulab-ops//CENTOS7-64-STD',  'CENTOS 7'),
#     ('urn:publicid:IDN+emulab.net+image+emulab-ops//CENTOS8-64-STD',  'CENTOS 8'),
#     ('urn:publicid:IDN+emulab.net+image+emulab-ops//FBSD114-64-STD', 'FreeBSD 11.4'),
#     ('urn:publicid:IDN+emulab.net+image+emulab-ops//FBSD122-64-STD', 'FreeBSD 12.2')]



# pc.defineParameter("osImage", "Select OS image",
#                    portal.ParameterType.IMAGE,
#                    imageList[0], imageList,
#                    longDescription="Most clusters have this set of images, " +
#                    "pick your favorite one.")

pc.defineParameter("controllerDiskImage","Controller Node Disk Image",
                   portal.ParameterType.IMAGE, "urn:publicid:IDN+lab.onelab.eu+image+tracing-pythia-PG0:base-with-repos",
                   longDescription="An image URN or URL that the controller node will run.")



# Retrieve the values the user specifies during instantiation.
params = pc.bindParameters()



# Add a raw PC to the request.
node = request.RawPC("node")

# Set OS Image
if params.controllerDiskImage and params.controllerDiskImage != "default":
    node.disk_image = params.controllerDiskImage

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
