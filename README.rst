pynamelix
=========

.. image:: https://img.shields.io/jenkins/build/https/jenkins.axju.de/job/axju/job/pynamelix/job/master
   :alt: Jenkins
   :target: https://jenkins.axju.de/job/axju/job/pynamelix/

.. image:: https://img.shields.io/jenkins/coverage/cobertura/https/jenkins.axju.de/job/axju/job/pynamelix/job/master
   :alt: Jenkins Coverage
   :target: https://jenkins.axju.de/job/axju/job/pynamelix/

.. image:: https://img.shields.io/pypi/pyversions/pynamelix
   :alt: Python Version
   :target: https://pypi.org/project/pynamelix/

.. image:: https://raw.githubusercontent.com/axju/pynamelix/master/ext/demo.gif
   :alt: demo.gif
   :align: right

API to `namelix.com <https://namelix.com>`__

Install
-------
From PyPi:

.. code-block:: bash

  pip install pynamelix

from source:

.. code-block:: bash

  git clone https://github.com/axju/pynamelix
  pip install .

Quick start
-----------
As a command line interface:

.. code-block:: bash

  python -m pynamelix -h

or:

.. code-block:: bash

  pynamelix -h

Example:

.. code-block:: bash

  python -m pynamelix -p -s wordmix -l medium python axju
