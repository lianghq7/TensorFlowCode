from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data", one_hot = True)

#Training data size: 55000
print "Training data size: ", mnist.train.num_examples#55000

#Validatng data size: 5000
print "Validatng data size: ", mnist.validation.num_examples

#Testing data size: 10000
print "Testing data size: ", mnist.test.num_examples

#Example training data: :  [ 0.          0.   ...  0.38039219  0.37647063   ...  0. ]
print "Example training data: ", mnist.train.images[0]

#Example training data label: [ 0.  0.  0.  0.  0.  0.  0.  1.  0.  0.] 
print "Example training data label: ", mnist.train.labels[0]