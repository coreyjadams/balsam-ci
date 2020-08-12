# balsam-ci
CI Scripts and applications for testing Balsam on HPC Systems


This repository contains the Jenkins tools to perform the following steps:
- Create a python environment and a fresh build of Balsam with it's relevant dependencies
  - This include postgres, mpi4py, etc.
- Initialize several applications within the balsam database:
  - A single-node application for the system
  - A single-core application for the system
  - A multi-node application for the system
  - A containerized application for the system
- Populate the balsam database with a sufficient number of jobs per application to successfully test.
- Launch jobs and wait for them to run.
- When jobs have completed, collect the throughput per application and report it.


The intention is to continuously monitor several aspects of balsam for usability and performance.
