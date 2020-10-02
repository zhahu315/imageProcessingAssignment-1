# 第一次作业说明

*张弛 202028013626005*

## 所用语言为`python3.x`,IDE为`pycharm2020`,所调用的外部库包括`numpy` ,`opencv-python`，系统自带库`time`,`sys`,`math`

1. 将灰度图读入数组，使用`shape`函数读取数组行列数，对行列数舍断取整得到中间行列数。利用数组切片，将中间行或列分别以行向量或列向量的形式读入新数组，生成灰度序列，显示图像后按任意键进入下一个图片处理。处理结果图片命名为'row_'+原名或'column\_'+原名放在根目录中。

   |     name      |                   中间行                    |                      中间列                       |
   | :-----------: | :-----------------------------------------: | :-----------------------------------------------: |
   | einstein.tif  |  ![row_einstein.tif](./1/row_einstein.tif)  |  ![column_einstein.tif](./1/column_einstein.tif)  |
   | cameraman.tif | ![row_cameraman.tif](./1/row_cameraman.tif) | ![column_cameraman.tif](./1/column_cameraman.tif) |

     

   

2. 先将图像以灰度图的形式读取显示为'raw'，作为自带函数的处理结果用以对比。实际操作时，将3通道RGB原图读入数组。初始化一个全0二维数组'out'用来存放结果。对于原图数组的第一维3通道，分别以'average'或'NTSC'对3通道数据进行处理在存入到'out'数组中去，再显示为图像。图像以'处理方式_'+原名的命名方式保存在根目录中。

   |                    raw                    |                          average                          |                        NTSC                         |
   | :---------------------------------------: | :-------------------------------------------------------: | :-------------------------------------------------: |
   | ![mandril_color.tif](2/mandril_color.tif) | ![average_mandril_color.tif](2/average_mandril_color.tif) | ![NTSC_mandril_color.tif](2/NTSC_mandril_color.tif) |
   |   ![lena512color](2/lena512color.tiff)    |   ![average_lena512color](2/average_lena512color.tiff)    |   ![NTSC_lena512color](2/NTSC_lena512color.tiff)    |

   

3. 对于图像填补，首先读取卷积核数组的行列数。读取原灰度图存入数组'arr_img'中，并得到其行列数。初始化数组'out_arr'作为存放最终卷积结果的二维数组，初始化数组'padding_img'作为扩展边界后的数组，扩展的行列数分别为2倍卷积核向下取整行列数的一半。将填补边界数组分为四个角，四条边，中间几个部分分别处理。中间部分直接用原图数组覆盖，其他八个部分，通过运算，将原数组中对应位置的数据填入，用0填补则全部放入0。卷积时，将卷积核按顺序与填补后的数组进行卷积计算，将得到的结果放入'ouy_arr'中，并进行输出。用一个$5\times5$的锐化卷积核进行测试，得到结果图像以'处理方法_'+原名的命名保存在根目录中。

   | raw                               | zero                                        | replicate                                             |
   | --------------------------------- | ------------------------------------------- | ----------------------------------------------------- |
   | ![cameraman.tif](3/cameraman.tif) | ![zero_cameraman.tif](3/zero_cameraman.tif) | ![replicate_cameraman.tif](3/replicate_cameraman.tif) |
   | ![einstein.tif](3/einstein.tif)   | ![zero_einstein.tif](3/zero_einstein.tif)   | ![replicate_einstein.tif](3/replicate_einstein.tif)   |

   由以上对比可以清晰看到，补零和复制两种处理方法滤波后的结果，在图像边缘处，补零方法会出现一条白色边框，而复制情况下则不会

4. 高斯滤波核w的最小大小用公式$min_m = math.ceil(3*sig)\times2+1$进行计算，其中`math.ceil`为向上取整。缺省m为-1，此时没有给出m，将m自动选为最小值。对于w的各个具体取值，则将二维高斯函数分布离散化填入，同时用sum记录各个值的累加合。最后将w的各个项均除以sum得到归一化的高斯滤波核。

5. 将所要读取的图像名以字符串传给f，将f用第2问的函数转为灰度图，返回处理后得到灰度图的名称给f，选定高斯滤波卷积核参数，传入`gaussKernel`函数，返回卷积核矩阵w，传入`twodConv`进行卷积处理。

## $\sigma = 1$与直接调用函数结果比较

|                         代码计算结果                         |                直接调用opencv函数结果                |
| :----------------------------------------------------------: | :--------------------------------------------------: |
|        ![NTSC_lena512color](5/NTSC_lena512color.tiff)        | ![cv_NTSC_lena512color](5/cv_NTSC_lena512color.tiff) |
| ![replicate_NTSC_cameraman.tif](5/replicate_NTSC_cameraman.tif) |  ![cv_NTSC_cameraman.tif](5/cv_NTSC_cameraman.tif)   |



## 比较补零和复制下的