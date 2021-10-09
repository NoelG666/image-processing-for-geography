# An algorithm that fits of detecting water segments with different dynamic textures
## SEGMENTATION GUIDED LABEL PROPAGATION
### Image Segmentation
- Clustering-based segmentation method, based on the work of Blas et al. This method basically stands on a two-staged unsupervised learning process.
- In the first stage: 
    - the method clusters appearancebased descriptors of all pixels present in the input image - K-means algorithm
    - Then, every pixel in the input image is assigned to the closest basis vector in Euclidian terms.
    - The appearance descriptor vector herein considered encompasses texture information encoded in 5*5 Laws’ masks.
- In the second stage:
  - statistics of larger areas are learned. Concretely, the histograms of basis vectors over a window of 15*15 pixels are computed.
  - Then, these histograms are clustered together with K-means.
- In the final step:
  - A segmentation is computed by determining the connected components of the previously re-classified image.
  - Then, adjacent segments of similar appearance are aggregated.
### Label Propagation
- Our method proceeds by re-labelling as water all pixels
encompassed by segments that have, at least, half of their
pixels already labelled as water. 