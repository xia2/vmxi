import h5py
import sys
import numpy
from scitbx.array_family import flex
data = h5py.File(sys.argv[1], 'r')['data']
shape = data.shape
for j in range(data.shape[0]):
  frame = flex.int(data[j,:,:]).as_double().as_1d()
  hist = flex.histogram(frame.as_1d(), data_min=0, data_max=4096, n_slots=4096)
  print j, hist.slot_centers()[list(hist.slots()).index(max(hist.slots()))]

