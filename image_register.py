#!/usr/bin/env python

"""
ChRIS Project
Developed by Arman Avesta, MD, PhD
FNNDSC | Boston Children's Hospital | Harvard Medical School

This module contains argument parsing and main function for the image_register plugin.
"""
# --------------------------------------------- ENVIRONMENT SETUP -----------------------------------------------------
# Project imports:
from registration_tools import rigid_registration

# System imports:
from os.path import join
from pathlib import Path
from argparse import ArgumentParser, Namespace, ArgumentDefaultsHelpFormatter
from chris_plugin import chris_plugin

# ---------------------------------------------- ARGUMENT PARSING -----------------------------------------------------

title = r"""

                        ###########################
                        ChRIS Image Register Plugin
                        ###########################

"""

parser = ArgumentParser(description='This plugin registers a moving 3D image (CT, MRI, PET, etc) onto another'
                                    'fixed image and saves the registered moving image as well as '
                                    'the transformation matrix. The fixed, moving, and registered moving images '
                                    'are all in NIfTI format.',
                        formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument('--fixed_image', type=str, default='fixed_image.nii.gz',
                    help='relative path to the fixed image in relation to input folder')
parser.add_argument('--moving_image', type=str, default='moving_image.nii.gz',
                    help='relative path to the moving image in relation to input folder')
parser.add_argument('--registered_image', type=str, default='registered_image.nii.gz',
                    help='relative path to the registered image in relation to output folder')
parser.add_argument('--transform_matrix', type=str, default='transform.mat',
                    help='relative path to the transformation matrix in relation to output folder')

# ------------------------------------------- ChRIS PLUGIN WRAPPER ----------------------------------------------------

@chris_plugin(
    parser=parser,
    title='image_register',
    category='3D Image Processing',
    min_memory_limit='2.5Gi',         # supported units: Mi, Gi
    min_cpu_limit='1000m',          # millicores, e.g. "1000m" = 1 CPU core
    min_gpu_limit=0)                # set min_gpu_limit=1 to enable GPU

# ----------------------------------------------- MAIN FUNCTION -------------------------------------------------------

def main(options: Namespace, inputdir: Path, outputdir: Path):

    print(title)

    fixed_image_path = join(inputdir, options.fixed_image)
    moving_image_path = join(inputdir, options.moving_image)
    registered_image_path = join(outputdir, options.registered_image)
    transform_matrix_path = join(outputdir, options.transform_matrix)

    rigid_registration(fixed_image_path, moving_image_path, registered_image_path, transform_matrix_path)

# ------------------------------------------------ EXECUTE MAIN -------------------------------------------------------

if __name__ == '__main__':
    main()
