#!/bin/bash -l
#SBATCH --account=lp_h_ds_2023_2024
#SBATCH --cluster=wice
#SBATCH --nodes=1
#SBATCH --time=10:00:00

python -m venv myenv
source myenv/bin/activate

# Upgrade pip
python -m pip install --upgrade pip

# Install matplotlib
python -m pip install matplotlib

python benchmark_bloom.py