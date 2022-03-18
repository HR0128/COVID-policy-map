#!/bin/bash
#SBATCH--workdir=/gpfs/home/sr2364/

module purge
module load py-pandas-1.1.5-gcc-9.3.0-7ahntqt
module load anaconda3-2020.07-gcc-9.3.0-myrjwlf
module load anaconda3-2020.07-gcc-9.3.0-myrjwlf
module load anaconda3-2020.07-gcc-9.3.0-myrjwlf
/opt/ohpc/admin/spack/spack/opt/spack/linux-centos8-zen2/gcc-9.3.0/anaconda3-2020.07-myrjwlfwrtrgdgpx6si4tcslrytnytnl/bin/python3.8 /gpfs/home/sr2364/map_html_generation.py
