Use of machine learning for anomaly detection in netflow data
=============================================================

This notebook can be viewed on `github <https://github.com/eraclitux/machine-learning-netflow/blob/master/machinelearning-netflow.ipynb>`_.

A readable version of this ipython notebook can also be found `here <http://nbviewer.ipython.org/github/eraclitux/machine-learning-netflow/blob/master/machinelearning-netflow.ipynb>`_.

Notes
=====

I'm not a data scientist and I'm sure that this process contains errors and inaccuracies. One of I'm aware of is that I've used euclidean distance calculation on heterogeneous features. This is formally incorrect even if classification results are consistent.

If you find other errors feels free to report them with isses or pull requests.

I've no longer access to any netflow data collector. I'd like to develop a service (and open source it ;-)) that applies ml alghoritms to this data to automatically spot anomalies. If someone is interested and has a collector with ``nfdump`` installed, which I can have ssh access to, please contact me!
