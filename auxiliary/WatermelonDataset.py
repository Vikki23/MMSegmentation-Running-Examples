# watermelon dataset
# @author: TommyZihao

from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset

@DATASETS.register_module()
class WatermelonDataset(BaseSegDataset):
    # class and self-defined colormap
    METAINFO = {
        'classes':['background', 'red', 'green', 'white', 'seed-black', 'seed-white'],
        'palette':[[127,127,127], [200,0,0], [0,200,0], [255,255,255], [30,30,30], [251,189,8]]
    }
    
    # specify the extension names of images and masks
    def __init__(self,
                 seg_map_suffix='.png',   # type of mask data
                 reduce_zero_label=False, # whether to remove class 0 (background) or not
                 **kwargs) -> None:
        super().__init__(
            seg_map_suffix=seg_map_suffix,
            reduce_zero_label=reduce_zero_label,
            **kwargs)