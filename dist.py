'''Script for peforming the nightly build.'''

import os
from time import strftime

def main():
    # Current file.
    dist_dir = os.path.abspath('./dist')
    dist_file = os.listdir(dist_dir)[0]

    o_dist_file = os.path.join(dist_dir, dist_file)

    # Remove extension.
    file_ext = '.tar.gz'
    n_dist_file = o_dist_file.replace(file_ext, '')

    # Rename.
    n_dist_file += '_'
    n_dist_file += strftime('%y%m%d%H%M%S')
    n_dist_file += file_ext
    n_dist_file = os.path.abspath(os.path.join(dist_dir, n_dist_file))

    # Move.
    os.rename(o_dist_file, n_dist_file)

if __name__ == '__main__':
    main()
