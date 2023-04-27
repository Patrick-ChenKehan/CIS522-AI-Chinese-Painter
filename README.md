# CIS522-AI-Chinese-Painter
## Documents

- [Proposal](https://docs.google.com/document/d/1sx3odUWFPOJsPg79FHZpckVfEO-G1LKSqAN0X61I7Q8/edit?usp=share_link)
- [Report](https://docs.google.com/document/d/1eJ36d50nTtlIOGf2mf6LKthkFzwGvmw-OqPKzY8fik4/edit?usp=share_link)

## Dataset

The subset of the dataset can be downloaded to `Original_Images/` and `Generated_Images/`. Use `Dataset Generation/organize.ipynb` to reorganize data into `dataset/`.

## Usage

### VGG19

Run notebook in `VGG19/VGG19.ipynb`. The original idea for using vgg19 is generated from [1].

### pix2pix

#### Generate dataset for pix2pix

Use the following code.

```shell
python datasets/combine_A_and_B.py --fold_A dataset/A --fold_B dataset/A --fold_AB dataset/
```

#### Train pix2pix

Use the following code. The original code for pix2pix is in [2].

```shell
python train.py --dataroot ./datasets/facades --name facades_pix2pix --model pix2pix --direction AtoB
```

## References

[1] Implementing neural style transfer using pytorch. Medium. Retrieved April 10, 2023, from https://towardsdatascience.com/implementing-neural-style-transfer-using-pytorch-fd8d43fb7bfa

[2] Abdelmotaal, Hazem, et al. "Pix2pix conditional generative adversarial networks for scheimpflug camera color-coded corneal tomography image generation." Translational Vision Science & Technology 10.7 (2021): 21-21.
