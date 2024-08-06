#!/usr/bin/env python

from os.path import join
from pathlib import Path
from argparse import ArgumentParser, Namespace, ArgumentDefaultsHelpFormatter
from chris_plugin import chris_plugin

from registration_tools import register_images_rigid



title = r"""

                        ###########################
                        ChRIS Register Image Plugin
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
parser.add_argument('--registered_moving_image', type=str, default='registered_moving_image.nii.gz',
                    help='relative path to the registered image in relation to output folder')
parser.add_argument('--transform_matrix', type=str, default='transform.mat',
                    help='relative path to the transformation matrix in relation to output folder')
parser.add_argument('--dof', type=str, default='6',
                    help='degrees of freedom to use in registration. Default = 6 (i.e. rigid registration).')
parser.add_argument('--cost', type=str, default='mutualinfo',
                    help='cost function used in registration. Default = mutualinfo (mutual information).')


# ToDo: how can I determine the minimum memory and CPU required for this plugin? I roughly estimated the required
#  memory by looking up how much memory the registration process needed on the Activity Monitor app on my Mac :D
@chris_plugin(
    parser=parser,
    title='register_image',
    category='3D Image Processing',
    min_memory_limit='2.5Gi',         # supported units: Mi, Gi
    min_cpu_limit='1000m',          # millicores, e.g. "1000m" = 1 CPU core
    min_gpu_limit=0)                # set min_gpu_limit=1 to enable GPU


def main(options: Namespace, inputdir: Path, outputdir: Path):

    print(title)

    fixed_image_path = join(inputdir, options.fixed_image)
    moving_image_path = join(inputdir, options.moving_image)
    registered_moving_image_path = join(outputdir, options.registered_moving_image)
    transform_matrix_path = join(outputdir, options.transform_matrix)
    dof = options.dof
    cost = options.cost

    register_images_rigid(fixed_image_path, moving_image_path, registered_moving_image_path, transform_matrix_path,
                          dof, cost)





if __name__ == '__main__':
    main()
