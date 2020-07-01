"""
This module contains scripts which are shared across multiple ACS modules.
"""

default_job_info_dict_after_initial_sp_screening = \
{
'project': None,  # project name, str
'is_initial_sp_screening': False,  # used to identify type of info file when read from disk
'conformer_to_opt_hash_ids': None,  # tuples of conformer (identified by its hash id) that will be opted
'colliding_conformer_after_opt_hash_ids': None,
'crashing_conformer_in_opt_hash_ids': None,
'conformer_to_calc_sp_after_opt_hash_ids': None,
'conformer_to_calc_solv_hash_ids': None,
'valid_conformer_hash_ids': None,  # for non-TS this means it's isomorphic to the given smile and is a well, for TS this means it's a first order saddle point for the reaction of interest
'project_folder_path': None,  # absolute path where the project info is saved, str
'calc_solvation_sp_correction': None,  # bool
'comment': None,  # reserved for additional info

'level_of_theory': {
                    'initial_screening_sp': None,  # initial sp energy used to screen conformers, hartree, float
                    'opt': None,  # optimization after conformer screening
                    'fine_opt': None,  # optional fine optimization
                    'sp_after_opt': None,  # high level gas phase sp energy computed using optimized geometry, hatree, float
                    'solv_sp_gas': None,  # gas phase sp energy computed using optimized geometry for solvation correction, hatree, float
                    'solv_sp_liq': None,  # liquid phase sp energy (e.g., SMD, PCM) computed using optimized geometry for solvation correction, hatree, float
                    'solv_correction': None,  # either (1) solv_sp_liq - solv_sp_gas for PCM, SMD corrections or (2) direct delta G solv correction such as COSMO-RS, hatree, float
                    },

'species': {
            'name': None,  # species name, str
            'smiles': None,
            'is_ts': None,  # bool
            'multiplicity': None,  # int
            'charge': None,  # int
            '1d_torsions': None,  # tuple of atom indices of all 1d rotatable dihedrals in the species
                                             # ((1, 2, 3, 4), (7, 8, 9, 10)) indicates two rotatable dihedrals

            'coord':    {
                        'file': None,  # files with coord info, can be xyz, gjf, log, out etc
                        'xyz_str': None,  # xyz format with atom symbol and coords only (no charge/multiplicity)
                        'arc_xyz': None,  # arc_xyz format
                        'zmat': None,  # standard zmat format
                        'arc_zmat': None,
                        'gaussian_std_zmat': None,
                        'connectivity': None,  # connectivity info deduced by ACS
                        },
            },

'conformers': dict()
}


default_conformer_info_dict_after_initial_sp_screening = \
{
'rotor_dimension': None,  #  number of dihedrals originally modified
'dihedral_before_opt': None,  #  ((atom indices for dihedral X), float of dihedral angle X)
                   #  ( ((1, 2, 3, 4), 45.0), ((7, 8, 9, 10), 120.0) ) for 2d dihedral changes
'is_colliding': None, # bool
'is_crashing': None, # bool
'is_isomorphic': None, # bool
'is_valid_ts': None,  # bool
'frequencies': None,  # tuple
'negative_frequencies': None,  # tuple
'xyz_str_before_opt': None,  # xyz format with atom symbol and coords only (no charge/multiplicity/atom count)
'arc_xyz_before_opt': None,  # arc_xyz format
'xyz_str_after_opt': None,  # xyz format with atom symbol and coords only (no charge/multiplicity/atom count)
'arc_xyz_after_opt': None,  # arc_xyz format


'energy':   {
            'initial_screening_sp': None,
            'end_of_opt': None,
            'end_of_fine_opt': None,
            'sp_after_opt': None,
            'solv_sp_gas': None,
            'solv_sp_liq': None,
            'solv_correction': None,
            'sp_include_solv_correction': None,
            },

'file_path': {
                'input': {
                            'initial_screening_sp': None,
                            'opt': None,
                            'fine_opt': None,
                            'sp_after_opt': None,
                            'solv_sp_gas': None,
                            'solv_sp_liq': None,
                            'solv_correction': None,
                            'sp_include_solv_correction': None,
                        },

                'output':   {
                            'initial_screening_sp': None,
                            'opt': None,
                            'fine_opt': None,
                            'sp_after_opt': None,
                            'solv_sp_gas': None,
                            'solv_sp_liq': None,
                            'solv_correction': None,
                            'sp_include_solv_correction': None,
                            },

            },
}


default_job_info_dict_for_initial_sp_screening = \
{
'project': None,  # project name, str
'is_initial_sp_screening': True,  # used to identify type of info file when read from disk
'conformer_to_screen_hash_ids': None,  # tuples of conformer (identified by its hash id) that will be screened via sp energy
'colliding_conformer_hash_ids': None,
'crashing_conformer_hash_ids': None,
'project_folder_path': None,  # absolute path where the project info is saved, str
'calc_solvation_sp_correction': None,  # bool
'dihedrals_considered_in_this_file': None,  # tuple of dihedrals considered in this file, useful for splitting files for parallelization
'n_point_each_torsion': None,
'comment': None,  # reserved for additional info
'memory': None,  # job memory

'level_of_theory': {
                    'initial_screening_sp': None,  # initial sp energy used to screen conformers, hartree, float
                    'opt': None,  # optimization after conformer screening
                    'fine_opt': None,  # optional fine optimization
                    'sp_after_opt': None,  # high level gas phase sp energy computed using optimized geometry, hatree, float
                    'solv_sp_gas': None,  # gas phase sp energy computed using optimized geometry for solvation correction, hatree, float
                    'solv_sp_liq': None,  # liquid phase sp energy (e.g., SMD, PCM) computed using optimized geometry for solvation correction, hatree, float
                    'solv_correction': None,  # either (1) solv_sp_liq - solv_sp_gas for PCM, SMD corrections or (2) direct delta G solv correction such as COSMO-RS, hatree, float
                    },

'species': {
            'name': None,  # species name, str
            'smiles': None,
            'is_ts': None,  # bool
            'multiplicity': None,  # int
            'charge': None,  # int
            '1d_torsions': None,  # tuple of atom indices of all 1d rotatable dihedrals in the species
                                             # ((1, 2, 3, 4), (7, 8, 9, 10)) indicates two rotatable dihedrals

            'coord':    {
                        'file': None,  # files with coord info, can be xyz, gjf, log, out etc
                        'xyz_str': None,  # xyz format with atom symbol and coords only (no charge/multiplicity/atom count)
                        'arc_xyz': None,  # arc_xyz format
                        'zmat': None,  # standard zmat format
                        'arc_zmat': None,
                        'gaussian_std_zmat': None,
                        'connectivity': None,  # connectivity info deduced by ACS
                        },
            },

'conformers': dict()
}


default_conformer_info_dict_for_initial_sp_screening = \
{
'rotor_dimension': None,  #  number of dihedrals modified
'dihedral': None,  #  ((atom indices for dihedral X), float of dihedral angle X, int of relative position to the original dihedral angle)
                   #  ( ((1, 2, 3, 4), 45.0, 0), ((7, 8, 9, 10), 120.0, 5) ) for 2d dihedral changes with the first dihedral being the original angle and the second one incremented five times from the original one
'xyz_str': None,  # xyz format with atom symbol and coords only (no charge/multiplicity/atom count)
'arc_xyz': None,  # arc_xyz format
'is_colliding': None, # bool
'is_crashing': None, # bool
'initial_screening_sp_energy': None,
}


g16_slurm_array_script = """#!/bin/bash -l
#SBATCH -p normal
#SBATCH -J opt{name}
#SBATCH -N 1
#SBATCH -n 40
#SBATCH --time=5-0:00:00
#SBATCH --mem-per-cpu=9000
#SBATCH --array=0-{last_job_num}
#SBATCH --exclusive

export g16root=/home/gridsan/oscarwu/GRPAPI/Software
export PATH=$g16root/g16/:$g16root/gv:$PATH
echo "Gaussian PATH"
which g16

jnum=$SLURM_ARRAY_TASK_ID
fin=$(echo ${{jnum}}_*.gjf)
#fout="${{fin%.*}}".out

input=`basename $fin .gjf`
echo "============================================================"
echo "Job ID : $SLURM_JOB_ID"
echo "Job Name : $SLURM_JOB_NAME"
echo "task ID: $SLURM_ARRAY_TASK_ID"
echo "Starting on : $(date)"
echo "Running on node : $SLURMD_NODENAME"
echo "Current directory : $(pwd)"
echo "============================================================"

export GAUSS_SCRDIR=/home/gridsan/oscarwu/scratch/$SLURM_JOB_NAME-$SLURM_JOB_ID

export GAUSS_SCRDIR
. $g16root/g16/bsd/g16.profile

echo "GAUSS_SCRDIR : $GAUSS_SCRDIR"
mkdir -p $GAUSS_SCRDIR
chmod 750 $GAUSS_SCRDIR

g16 < $input.gjf > $input.log

rm -rf $GAUSS_SCRDIR



"""