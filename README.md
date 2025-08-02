# jupyter-notebooks
A collection of my own Jupyter Notebooks for learning and experimentation. 

The contents of this repo include:

1. `numpyNN.ipynb`: An implementation of LeNet-5 from scratch using only Numpy, Autograd and a lot of duct tape 
2. `SurvivalAnalysis.ipynb`: Assessing marketing campaign effectiveness using Cox regression on a UCI Bank Marketing dataset

### Legacy Notebooks

There are also several legacy notebooks, developed ~2018, which have been preserved and are not maintained; a reminder of a time when TF still used lazy execution and YOLOv3 & Faster-RCNN were SOTA for object detection! 

- `dtree.ipynb`: A simple decision tree classifier for the iris data set (80% training, 20% testing)
- `manyclassifiers.ipynb`: A comparison of classification accuracies of three commonly used models for the Titanic Survivability problem.
- `convolutionkernels.ipynb`: Exploring the Convolution Operation in Convolutional Neural Networks
- `LOTR LSTM.ipynb`: A Sequence-2-Sequence Bidirectional LSTM for Lord of The Rings poetry generation. Applies a naive manual tokenization process that unintentionally introduces high cardinality, causing all sorts of interesting issues due to loss of word order, vocab fragmentation and increased embedding sparsity. The gibberish is fun to look at though.

Datasets are not included, but all non-legacy notebooks should pull them from configured sources at runtime.
