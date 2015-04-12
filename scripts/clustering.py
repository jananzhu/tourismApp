from numpy import ndarray
import numpy as np
import xml.etree.ElementTree as ET
from sklearn import cluster
from matplotlib import pyplot
from scipy.spatial import ConvexHull

def kmeanscluster(xmlfile,k):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    data = np.zeros([0,2])
    for child in root:
        data = np.concatenate((data,[[float(child[1][0].text),float(child[1][1].text)]]), axis = 0)
    kmeans = cluster.KMeans(n_clusters=k)
    kmeans.fit(data)
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_

    hulls = list()

    for i in range(k):
       
        ds = data[np.where(labels==i)]
        hulls.append(data[ConvexHull(ds).vertices])

    return hulls


if __name__ == "__main__":
    l = kmeanscluster('geo_coordinates.xml',7)
    