import tensorflow as tf

from layers import conv2d, fully_connected_layer, batch_norm, resnet_block


def deep_network(x, y=None, number_of_classes=2, filters=(16, 32, 64, 128), strides=(2, 1, 2, 1)):
  # TODO: Use the conv2d, tf.nn.relu and fully_connected_layer to create a (n+1)-layer network,
  # where n corresponds to the length of filters and strides.
  # your n first layers should be convoultional and the last layer fully connected.
  logits = None
  params = {}
  assert len(filters)==len(strides), 'The parameters filter and stride should have the same length, had length %d and %d' \
  %((len(filters), len(strides)))

  ###### YOUR CODE #######
  # Build your network and output logits

  # END OF YOUR CODE

  if y is None:
    return logits, params

  # TODO: Calculate softmax cross-entropy
  #  without using any of the softmax or cross-entropy functions from Tensorflow
  loss = None

  ###### YOUR CODE #######
  # Calculate loss

  # END OF YOUR CODE

  return logits, loss, params


def deep_network_with_batchnorm(x, y=None,
                                number_of_classes=2,
                                filters=(16, 32, 64, 128),
                                strides=(2, 1, 2, 1),
                                is_training=True):
  # TODO: Do the same as with deep_network, but this time add batchnorm before each convoulution.

  logits = None
  params = {}
  assert len(filters)==len(strides), 'The parameters filter and stride should have the same length, had length %d and %d' \
  %((len(filters), len(strides)))

  update_ops = [] #Fill this with update_ops from batch_norm

  ###### YOUR CODE #######
  # Build your network and output logits

  # END OF YOUR CODE

  if y is None:
    return logits, params, update_ops

  # TODO: Calculate softmax cross-entropy
  #  without using any of the softmax or cross-entropy functions from Tensorflow
  loss = None

  ###### YOUR CODE #######
  # Calculate loss

  # END OF YOUR CODE

  update_op = tf.group(*tuple(update_ops))
  return logits, loss, params, update_op


def deep_residual_network(x, y=None,
                                number_of_classes=2,
                                filters=(16, 32, 64, 128),
                                strides=(2, 1, 2, 1),
                                is_training=True):
  # TODO: Do the same as with deep_network_with_batchnorm*, but this time use the residual_blocks

  logits = None
  params = {}
  assert len(filters)==len(strides), 'The parameters filter and stride should have the same length, had length %d and %d' \
  %((len(filters), len(strides)))

  update_ops = [] #Fill this with update_ops from batch_norm

  ###### YOUR CODE #######
  # Build your network and output logits

  # END OF YOUR CODE


  update_op = tf.group(*tuple(update_ops))
  if y is None:
    return logits, params, update_ops

  # TODO: Calculate softmax cross-entropy loss
  #  without using any of the softmax or cross-entropy functions from Tensorflow
  loss = None

  ###### YOUR CODE #######
  # Calculate loss

  # END OF YOUR CODE

  return logits, loss, params, update_op