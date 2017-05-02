from __future__ import print_function
import tensorflow as tf
import numpy as np


def conv2d(x, number_of_features, k_size=3, stride=1):
  """
  
  :param x: Input of 4-dimensional tensorflow tensor
  :param number_of_features: Number of output channels
  :param k_size: The spatial size of the filter in both weight and width
  :param stride: Stride in spatial dimensions
  :return: x filtered by the kernal W and added bias b
  """
  params = {'W': None, 'b': None}
  out = None
  #------------------------------------------------------------#
  # TODO: Implement a 2D convolutional layer
  # Use the tf.nn.conv2d function from tensorflow and add a bias, but use no activation function.
  # store the weight and bias variables in the params dictionary.

  #YOUR CODE

  #END OF YOUR CODE
  return out, params


def fully_connected_layer(x, out_size):
  params = {'W': None, 'b': None}
  out = None
  #------------------------------------------------------------#
  # TODO: Implement a fully connected layer
  # Use tf.matmul. The dimension of x is either 2 or 4,
  # but the output should have 2 dimensions (batch_size, out_size)

  #YOUR CODE

  #END OF YOUR CODE
  return out, params


def batch_norm(x, is_training=True):
  params = {'gamma': None, 'beta': None, 'average_mean': None, 'average_var': None}
  update_op = None
  out = None
  is_training_tensor = tf.convert_to_tensor(is_training)
  assign_mean = None
  assign_var = None
  # TODO: Implement batch norm
  # Average over batches and spatial size, but not over channels.
  # Use exponential smoothing (https://en.wikipedia.org/wiki/Exponential_smoothing)
  # to keep the average mean and average variation.
  # Gamma should be initialized to 1 and beta 2, but remember that they should be trainable (Variable)

  #YOUR CODE

  #END OF YOUR CODE
  update_op = tf.group(assign_mean, assign_var)
  return out, params, update_op




def resnet_block(x, filters=(32, 64), k_size=(3, 3), stride=1, is_training=True):
  params = {}
  out = None
  update_ops = []
  params = {'A/W': None, 'A/b': None, 'A/gamma': None, 'A/beta': None,
            'B/W': None, 'B/b': None, 'B/gamma': None, 'B/beta': None,
            'shortcut/W': None, 'shortcut/b': None}
  # TODO: implament a ResNet-block
  # In this exercise you should implement a "preactivated" resnet-block with 3 convolutions
  # and batch norm. The params should contain all parameters, and and the names of each conv and batch norm
  # should start with either 'A/', 'B/' or 'shortcut/', depending on which convolution it
  # belongs to.

  #YOUR CODE

  #END OF YOUR CODE
  update_op = tf.group(*tuple(update_ops))
  return out, params, update_op