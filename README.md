# PRISMA

Series of scripts to derive different computer vision tasks from a single image or video.

```Shell
conda env create -f environment.yml
conda activate prisma
python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'
sh download_models.sh
```

## Depth estimation (MiDAS 3.1)

**Paper:** [Towards Robust Monocular Depth Estimation: Mixing Datasets for Zero-shot Cross-dataset Transfer](https://arxiv.org/abs/1907.01341v3)

**Code Repo:** [isl-org/MiDaS](https://github.com/isl-org/MiDaS)

**Use:**

```Shell
depth_midas.py --input <IMAGE/VIDEO> --output <IMAGE/VIDEO>
```

Citation:
```
@ARTICLE {Ranftl2022,
    author  = "Ren\'{e} Ranftl and Katrin Lasinger and David Hafner and Konrad Schindler and Vladlen Koltun",
    title   = "Towards Robust Monocular Depth Estimation: Mixing Datasets for Zero-Shot Cross-Dataset Transfer",
    journal = "IEEE Transactions on Pattern Analysis and Machine Intelligence",
    year    = "2022",
    volume  = "44",
    number  = "3"
}
```

Citation for DPT-based model:
```
@article{Ranftl2021,
    author    = {Ren\'{e} Ranftl and Alexey Bochkovskiy and Vladlen Koltun},
    title     = {Vision Transformers for Dense Prediction},
    journal   = {ArXiv preprint},
    year      = {2021},
}
```


## Depth Estimation (ZoeDepth)

**Paper:** [Zero-shot Transfer by Combining Relative and Metric Depth](https://arxiv.org/abs/2302.12288)

**Code Repo:** [isl-org/ZoeDepth](https://github.com/isl-org/ZoeDepth)

**Use:**

```Shell
depth_zoe.py --input <IMAGE/VIDEO> --output <IMAGE/VIDEO>
```

Citation
```
@misc{https://doi.org/10.48550/arxiv.2302.12288,
    doi = {10.48550/ARXIV.2302.12288},
    url = {https://arxiv.org/abs/2302.12288},
    author = {Bhat, Shariq Farooq and Birkl, Reiner and Wofk, Diana and Wonka, Peter and Müller, Matthias},  
    keywords = {Computer Vision and Pattern Recognition (cs.CV), FOS: Computer and information sciences, FOS: Computer and information sciences},
    title = {ZoeDepth: Zero-shot Transfer by Combining Relative and Metric Depth},  
    publisher = {arXiv},
    year = {2023},
    copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## Depth Estimation (PatchFusion)

**Paper:** [PatchFusion: An End-to-End Tile-Based Framework for High-Resolution Monocular Metric Depth Estimation](https://zhyever.github.io/patchfusion/images/paper.pdf)

**Code Repo:** [zhyever/PatchFusion](https://github.com/zhyever/PatchFusion)

**Use:**

```Shell
depth_fusion.py --input <IMAGE/VIDEO> --output <IMAGE/VIDEO>
```

**Note:** [This pretrained model](https://huggingface.co/zhyever/PatchFusion/resolve/main/patchfusion_u4k.pt?download=true) needs to be downloaded and placed in the `models/` folder.


Citation

```
@article{li2023patchfusion,
    title={PatchFusion: An End-to-End Tile-Based Framework for High-Resolution Monocular Metric Depth Estimation}, 
    author={Zhenyu Li and Shariq Farooq Bhat and Peter Wonka},
    year={2023},
    eprint={2312.02284},
    archivePrefix={arXiv},
    primaryClass={cs.CV}}
```

## Optical Flow (RAFT)

Based on https://github.com/SharifElfouly/opical-flow-estimation-with-RAFT

Seems to be very good: [Optical Flow Estimation Benchmark](https://paperswithcode.com/sota/optical-flow-estimation-on-sintel-clean)

**Paper:** [RAFT: Recurrent All Pairs Field Transforms for Optical Flow](https://arxiv.org/pdf/2003.12039)

**Code Repo:** [princeton-vl/RAFT](https://github.com/princeton-vl/RAFT)

**Use:**

```Shell
flow.py --input <IMAGE/VIDEO> --output <IMAGE/VIDEO>
```

## Segmentation (Detectron2)

**Code Repo:** [Detectron2](https://github.com/facebookresearch/detectron2)

**Use:**


```Shell
mask_densepose.py --input <IMAGE/VIDEO> --output <IMAGE/VIDEO>
```

Citation:
```
@misc{wu2019detectron2,
  author =       {Yuxin Wu and Alexander Kirillov and Francisco Massa and
                  Wan-Yen Lo and Ross Girshick},
  title =        {Detectron2},
  howpublished = {\url{https://github.com/facebookresearch/detectron2}},
  year =         {2019}
}
```


## FcF-Inpainting

**Paper:** [eys to Better Image Inpainting: Structure and Texture Go Hand in Hand](https://praeclarumjj3.github.io/fcf-inpainting/)

**Code Repo:** [SHI-Labs/FcF-Inpainting](https://github.com/SHI-Labs/FcF-Inpainting)

**Use:**

```Shell
inpaint_fcfgan.py -input <IMAGE/VIDEO> -mask <IMAGE/VIDEO> -output <IMAGE/VIDEO> 
```

Citation:

```
@inproceedings{jain2022keys,
    title={Keys to Better Image Inpainting: Structure and Texture Go Hand in Hand},
    author={Jitesh Jain and Yuqian Zhou and Ning Yu and Humphrey Shi},
    booktitle={WACV},
    year={2023}
} 
```


## Super Resolution

**Code Repo:** [xinntao/Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN)

Citation:
```
@InProceedings{wang2021realesrgan,
    author    = {Xintao Wang and Liangbin Xie and Chao Dong and Ying Shan},
    title     = {Real-ESRGAN: Training Real-World Blind Super-Resolution with Pure Synthetic Data},
    booktitle = {International Conference on Computer Vision Workshops (ICCVW)},
    date      = {2021}
}
```

