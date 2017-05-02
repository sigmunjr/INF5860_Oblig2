from __future__ import print_function
import numpy as np
import sys
import os

if sys.version_info[0] == 3:
    import _pickle as cPickle
else:
    import cPickle


def load_cifar_file(path='./datasets/cifar-10-batches-py/data_batch_1'):
    if not os.path.exists(path):
        print('WARNING: path', path, 'does not exist.')
        return [], []
    data_file = open(path, 'rb')
    if sys.version_info[0] == 3:
        data_dict = cPickle.load(data_file, encoding='latin-1')
    else:
        data_dict = cPickle.load(data_file)

    images = data_dict['data'].reshape((-1, 3, 32, 32)).transpose([0, 2, 3, 1])
    if 'fine_labels' in data_dict:
      labels = np.array(data_dict['fine_labels'])
    else:
      labels = np.array(data_dict['labels'])
    return images, labels


def load_cifar(path='./datasets/cifar-10-batches-py', test=False):
  images = []; labels= []
  batches = ('test_batch',) if test else ('data_batch_1', 'data_batch_2', 'data_batch_3', 'data_batch_4', 'data_batch_5')
  for batch_name in batches:
    i, l = load_cifar_file(path + '/' + batch_name)
    if len(i)<1: continue
    images.append(i); labels.append(l)
  return np.concatenate(images, 0), np.concatenate(labels, 0)


if __name__ == '__main__':
    load_cifar('./input')