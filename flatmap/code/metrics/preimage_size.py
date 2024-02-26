import voxcell as vc
import numpy as np
import sys

flatmap_nrrd = sys.argv[1]
pixel_res = int(sys.argv[2])
output_nrrd = sys.argv[3]

fmap_vd = vc.VoxelData.load_nrrd(flatmap_nrrd)
fmap = fmap_vd.raw
msk = fmap[:,:,:,0] > -1
pix_uniq, counts = np.unique(fmap[msk], axis=0, return_counts=True)

res = np.zeros((pixel_res, pixel_res), dtype=np.float32)
res[tuple(pix_uniq.T)] = counts

res_vd = vc.VoxelData(res, (1,1))
res_vd.save_nrrd(output_nrrd)
