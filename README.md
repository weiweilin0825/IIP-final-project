# Color Transfer Between Images with Skew Correctiont
This project is the final project of the course "Introduction to Image Processing". The project includes three parts: Content-Aware Rotation, Color transfer, and Transportation Map Regularization.

Our theme combines Content-Aware Rotation, Color Transfer, and Transportation Map Regularization (TMR). Many images become skewed due to incorrect shooting angles or other factors, requiring Content-Aware Rotation for correction. Additionally, Color Transfer has many applications, one of the most common being photo filters used by nearly everyone. Finally, TMR can improve images flawed by Color Transfer. Based on this, we have decided to focus on these three themes.

The followings are our results

## Content-Aware Rotation
We correct the tiled background while preserving the angle of Torre Pendente di Pisa.
<img src="https://github.com/PeiChiChen/Digital-Image-Processing-Project/blob/main/image/rotation.png" height="250px">

## Color Transfer
<img src="https://github.com/PeiChiChen/Digital-Image-Processing-Project/blob/main/image/color.png" height="250px">

## Transportation Map Regularization
<img src="https://github.com/PeiChiChen/Digital-Image-Processing-Project/blob/main/image/TMR.png" height="250px">

# Acknowledgement and Reference
The methods we use are based on the following papers.
```BibTeX
@INPROCEEDINGS{CAR,
  author={He, Kaiming and Chang, Huiwen and Sun, Jian},
  booktitle={2013 IEEE International Conference on Computer Vision}, 
  title={Content-Aware Rotation}, 
  year={2013},
  volume={},
  number={},
  pages={553-560},
  doi={10.1109/ICCV.2013.74}}

@ARTICLE{Color_Transfer,
  author={Reinhard, E. and Adhikhmin, M. and Gooch, B. and Shirley, P.},
  journal={IEEE Computer Graphics and Applications}, 
  title={Color transfer between images}, 
  year={2001},
  volume={21},
  number={5},
  pages={34-41},
  doi={10.1109/38.946629}}

@INPROCEEDINGS{TMR,
  author={Rabin, Julien and Delon, Julie and Gousseau, Yann},
  booktitle={2010 IEEE International Conference on Image Processing}, 
  title={Regularization of transportation maps for color and contrast transfer}, 
  year={2010},
  volume={},
  number={},
  pages={1933-1936},
  doi={10.1109/ICIP.2010.5650823}}
```
