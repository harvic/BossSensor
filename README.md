# BossSensor
Hide your screen when your boss is approaching.

## 修复及声明

原始代码写于2017年，时间过于久远，很多函数已经不可使用，直接运行是运行不起来的。我对代码进行了修复。

整体配置流程不变，在环境中可能会用到pyqt5、opencv3.4.2、keras2.2.4这些组件的安装提示，切记安装我这里指定的版本，不然可能函数不匹配。对python比较熟悉的同学，可以直接使用本ReadMe中的提示进行配置即可。

另外，**我将我整个环境配置过程、所需要组件的下载链接、运行过程中的一些提示、以及代码修改方法进行了整合**，以使对python不熟悉的同学少走弯路。

**大家可以关注我的公众号【启舰杂谈】，回复【013】即可获得这个文档。**

![](/resource_for_readme/pic2.jpg)

## Demo
The boss stands up. He is approaching.

![standup](https://github.com/Hironsan/BossSensor/blob/master/resource_for_readme/standup.jpg)

When he is approaching, the program fetches face images and classifies the image.
 
![approaching](https://github.com/Hironsan/BossSensor/blob/master/resource_for_readme/approach.jpg)

If the image is classified as the Boss, it will monitor changes.

![editor](https://github.com/Hironsan/BossSensor/blob/master/resource_for_readme/editor.jpg)

## Requirements

* WebCamera
* Python3.5
* OSX
* Anaconda
* Lots of images of your boss and other person image

Put images into [data/boss](https://github.com/Hironsan/BossSensor/tree/master/data/boss) and [data/other](https://github.com/Hironsan/BossSensor/tree/master/data/other).

## Usage
First, Train boss image.

```
$ python boss_train.py
```


Second, start BossSensor. 

```
$ python camera_reader.py
```

## Install
Install OpenCV, PyQt4, Anaconda.

```
conda create -n venv python=3.5
source activate venv
conda install -c https://conda.anaconda.org/menpo opencv3
conda install -c conda-forge tensorflow
pip install -r requirements.txt
```

Change Keras backend from Theano to TensorFlow. 

## Licence

[MIT](https://github.com/Hironsan/BossSensor/blob/master/LICENSE)

## Author

[Hironsan](https://github.com/Hironsan)


