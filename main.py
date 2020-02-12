import tensorflow as tf 
from   tensorflow.examples.tutorials.mnist	import	input_data

mnist	=	input_data.read_data_sets("MNIST_data/", one_hot=True)	

#y labels	are	oh-encoded
#explanation for one_hot

#we use one-hot encoding to represent the labels number "3" of the images
n_train = mnist.train.num_examples # 55 000
n_validation = mnist.validation.num_examples #5000
n_test = mnist.test.num_examples #10 000

#store the number of units per layer in global variables

n_input	=	784		    	#	input	layer	(28x28	pixels)
n_hidden1	=	512			#	1st	hidden	layer
n_hidden2	=	256			#	2nd	hidden	layer
n_hidden3	=	128			#	3rd	hidden	layer
n_output	=	10			#	output	layer	(0-9	digits)

learning_rate	=	1e-4	#how much parameters will adjust at each step of the learning process
n_iterations	=	1000	#how many times we go through training steps
batch_size	=	128			#how many training examples are we using
dropout	=	0.5				#used in final hidden layer to give each unit 50% chance to get eleminated at every training step

#None is any amount of data that we will be feeding in an undefined number of 784-pixel images
X	=	tf.placeholder("float",	[None,	n_input])
#undefined number of label outputs with 10 possible classes
Y	=	tf.placeholder("float",	[None,	n_output])
#controls dropout rate
#use same tensor for training and testing
keep_prob	=	tf.placeholder(tf.float32)

weights	=	{
	'w1':	tf.Variable(tf.truncated_normal([n_input,	n_hidden1],	
stddev=0.1)),
	'w2':	tf.Variable(tf.truncated_normal([n_hidden1,	n_hidden2],	
stddev=0.1)),
	'w3':	tf.Variable(tf.truncated_normal([n_hidden2,	n_hidden3],	
stddev=0.1)),
	'out':	tf.Variable(tf.truncated_normal([n_hidden3,	n_output],stddev=0.1)),
}

#for bias we use a small constant value to ensure that the tensors activate in the 
#initial stages and therefore contribute to the propagation 

biases	=	{
	'b1':	tf.Variable(tf.constant(0.1,	shape=[n_hidden1])),
	'b2':	tf.Variable(tf.constant(0.1,	shape=[n_hidden2])),
	'b3':	tf.Variable(tf.constant(0.1,	shape=[n_hidden3])),
	'out':	tf.Variable(tf.constant(0.1,	shape=[n_output]))
}

#set up the layers by defining the operations that will manipulate tensors

layer_1	=	tf.add(tf.matmul(X,	weights['w1']),	biases['b1'])
layer_2	=	tf.add(tf.matmul(layer_1,	weights['w2']),	biases['b2'])
layer_3	=	tf.add(tf.matmul(layer_2,	weights['w3']),	biases['b3'])
layer_drop	=	tf.nn.dropout(layer_3,	keep_prob)
output_layer =	tf.matmul(layer_3,	weights['out'])	+	biases['out']

cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=Y,logits=output_layer))
train_step	=	tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

#we just finishing defining the network and build it out with TensorFlow

#Feeding the training dataset through the graph and optimizing the loss function 
#Evaluate accuracy in mini-batches

#argmax function to compare which images are being predicted correctly by looking 
#at the output_layer (predictions) and Y (labels)
#equal function to return a list of Booleans, we can cast the list to floats and calculate the mean
#to get a total accuracy score
correct_pred=tf.equal(tf.argmax(output_layer,1),	tf.argmax(Y,1))
accuracy=tf.reduce_mean(tf.cast(correct_pred,tf.float32))

init=tf.global_variables_initializer()
sess=tf.Session()
sess.run(init)

#	train	on	mini	batches
for	i in range(n_iterations):
	batch_x,	batch_y	=	mnist.train.next_batch(batch_size)
	sess.run(train_step,	feed_dict={
	X:	batch_x,	Y:	batch_y,	keep_prob:	dropout
})

#print	loss	and	accuracy	(per	minibatch)
if	i	%	100	==	0:
	minibatch_loss,	minibatch_accuracy	=	sess.run(
	[cross_entropy,	accuracy],feed_dict={X:	batch_x,	Y:	batch_y,	keep_prob:	1.0})
	print("Iteration",str(i),"\t|	Loss	=",str(minibatch_loss),"\t|	Accuracy	=",str(minibatch_accuracy))

test_accuracy	=	sess.run(accuracy,	feed_dict={X:	mnist.test.images,	Y:	
mnist.test.labels,	keep_prob:	1.0})
print("\nAccuracy	on	test	set:",	test_accuracy)		
