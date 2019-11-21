import numpy as np
import transformations
import transform_util as tf_util

if __name__ == '__main__':
    quat = np.array([0,np.sqrt(2),0,np.sqrt(2)])
    mat = transformations.quaternion_matrix(quat)
    mat = mat[:3, :3]
    rot_axis = np.array([0, 1, 0])
    dphi = np.pi/2.0
    rot_theta = dphi
    rot_mat = tf_util.axis_angle_to_rotation_matrix(rot_axis, rot_theta)
    mat = rot_mat.dot(mat)
    quat = transformations.quaternion_from_matrix(mat)
    print(quat)