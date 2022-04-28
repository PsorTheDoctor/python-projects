import numpy as np
from sklearn.neighbors import NearestNeighbors


def best_fit_transform(A, B):

    assert A.shape == B.shape

    dim = A.shape[1]

    centroid_A = np.mean(A, axis=0)
    centroid_B = np.mean(B, axis=0)
    
    normalized_A = A - centroid_A
    normalized_B = B - centroid_B

    H = np.dot(normalized_A.T, normalized_B)
    U, S, Vt = np.linalg.svd(H)
    rot = np.dot(Vt.T, U.T)

    if np.linalg.det(rot) < 0:
        Vt[dim - 1, :] *= -1
        rot = np.dot(Vt.T, U.T)

    transl = centroid_B.T - np.dot(rot, centroid_A.T)

    transf = np.identity(dim + 1)
    transf[:dim, :dim] = rot
    transf[:dim, dim] = transl

    return transf, rot, transl


def nearest_neighbour(src, dst):

    assert src.shape == dst.shape

    neigh = NearestNeighbors(n_neighbors=1)
    neigh.fit(dst)
    distances, indices = neigh.kneighbors(src, return_distance=True)
    return distances.ravel(), indices.ravel()


def icp(A, B, init_pose=None, max_iters=20, tolerance=0.001):

    assert A.shape == B.shape

    dim = A.shape[1]

    src = np.ones((dim + 1, A.shape[0]))
    dst = np.ones((dim + 1, A.shape[0]))
    src[:dim, :] = np.copy(A.T)
    dst[:dim, :] = np.copy(A.T)

    if init_pose is not None:
        src = np.dot(init_pose, src)

    prev_error = 0
    distances = None
    i = 0

    for i in range(max_iters):
        distances, indices = nearest_neighbour(src[:dim, :].T, dst[:dim, :].T)

        final_transf, _, _ = best_fit_transform(src[:dim, :].T, dst[:dim, indices].T)

        src = np.dot(final_transf, src)

        mean_error = np.mean(distances)
        if np.abs(prev_error - mean_error) < tolerance:
            break

        prev_error = mean_error

    final_transf, _, _ = best_fit_transform(A, src[:dim, :].T)

    return final_transf, distances, i
 
