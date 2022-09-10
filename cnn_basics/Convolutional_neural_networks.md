Now that we know what standard Neural Networks are and how they work, we can learn about more elegant types of networks. One of these types is the Convolutional Neural Network.

# What are Convolutional Neural Networks?

Convolutional Neural Networks (CNNs) are structured similarly to regular Neural Networks. However, the data samples are form

# Why use Convolutional Neural Networks?

Standard Neural Networks face many challenges that could completely change an image's classification. Let's say you want to classify a photo of an airplane from the Cifar-10 dataset. A standard Neural Network would easily be able to classify it. However, let's say the image is backwards or at an angle. This makes it incredibly hard for the Neural Network to label this image accurately. CNNs can classify pictures regardless of the subject's apparent size, angle, location etc. Additionally, training regular Neural Networks require an incredible amount of computational power. Training CNNs, on the other hand, is much less resource intensive.

# How do Convolutional Neural Networks do this?

Before we move on with CNNs, how do we instantly recognize these images? Let's take our airplane example. We look at the individual features, the cylindrical body, the two wings, and the windows and piece them together. Because this image has all of the recognizable features of an airplane, we can deduce that this must be an image of an airplane. CNNs work in a similar fashion. Instead of classifying images straight away, CNNs augment the data first. CNNs use filters to draw out certain features in images.

# What is a filter?

A filter is a template or pattern which resembles specific features. The following filter is used to locate any loop patterns within an image.

![Images/Filter.png]

Filters work by being convolved through an image with a specific stride. The stride is how far the filter moves in one step. Convolved in this context is merging two sets of information to produce a third. For simplicity, we will use an image of the number 9 rather than an airplane. Outline the first 3x3 box because our filter has a size of 3x3.
Imagine that we put the filter over our image to cover the green box on the nine and line up all the smaller boxes.

![Image/Convolving.png]

Then take each number in all the matching boxes, multiply them together and then take the average of all the multiples. This will turn out to be

$$\frac{\left(-1*1\right)+\left(1*1\right)+\left(1*1\right)+\left(-1*1\right)+\left(1*-1\right)+\left(-1*1\right)+\left(-1*1\right)+\left(1*1\right)+\left(1*1\right)}{9}=-0.11$$

The next step in convolving is to move the filter to the right by one box because our stride is one, and then repeat the process until the filter has been applied to the entire image. All of these values are then recorded in a grid called the feature map.

# What is a feature map?

A feature map is a grid of numbers that tells whether a feature is found in an image. After applying our filter, our feature map would look like

![Image/Featuremap.png]

Before we analyze the feature map, we must pass all the numbers into the ReLU function to eliminate the negative numbers.

![Image/Featuremap_with_relu.png]

# What is sample pooling?

For the CNN to be less resource intensive, we must reduce the feature map size. This technique is called pooling, and there are many different types of pooling methods; however, one of the most commonly used methods is max pooling. Not only does pooling reduce the computational power required, but it also makes the CNN tolerant to distortions, clutter, and obscurations by only focusing on the main parts of a feature map.

We will perform max pooling on this feature map with a pool size of 2x2 and a stride of one. Just like with filters, imagine a 2x2 box on the top right of the feature map. We will only take the highest value in the square for max pooling to create a new, smaller feature map. Then we will shift the pool right by one and continue. The final feature map after max pooling would look like

![![Image/Pooling.png]

Notice how all of the boxes except two have minimal numbers. This means they do not match the features the filter is searching for. However, two of these boxes have incredibly high numbers. This means those two 3x3 squares probably have the feature the filter is looking for. It is important to note that we must apply multiple filters to classify an image.

# Why do Convolutional Neural Networks have to apply multiple filters?

To accurately classify an image, we have to apply additional filters to detect more unique characteristics and thus generate more feature maps; we cannot only search for one feature. Yes, the nine has a  loop at the top, but if we entered a six in, the computer would also detect a loop at the bottom, and for an eight, there would be two loops detected.

Let us say we do this process for our airplane. We can have three feature maps to identify the position of the wings, doors, and windows. Once we have these three feature maps, we can aggregate them and apply another filter to determine the location of the plane’s body.

We would then repeat this process until we have a few feature maps of a plane's critical components, such as its head, body, and tail. Now, this is where our knowledge of regular Neural Networks comes in. Just as we flatten images for standard Neural Networks, we will flatten and join all of these main feature maps from multiple 2-d arrays into a single 1-d array. Then this array will be the input into our Neural Network to determine whether all of the features are present to classify our image as a plane. The CNN picks up the main features anywhere within the image and then classifies those. This CNN is much more elegant than our standard Neural Network because it does not matter where our plane is in the picture, whether vertical, horizontal, at an angle, or whether a small portion of the airplane is obscured. However, it is important to note that the image of the 9 was in black and white whereas the image of our plane was a mixture of red, green, and blue. This means that instead of having a 2-d filter, we can also utilize 3-d filters to differentiate between the colors. Additionally, these filters are discovered by the Neural Network while being trained. We do not create them.

To summarize, the final CNN process ends up looking like

![![Image/Final_network.png]
