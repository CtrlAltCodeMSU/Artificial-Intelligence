for i in range(1 ,4):
  print(i)

l = [1,15,10,4,9,6]

for i in l:
  print(i)

  l.sort()
print(l)


s = "SANAULLLAH"
for i in s:
  print(i , " " , end="")

# import numpy as np
# import tensorflow as tf
# from tensorflow import keras

# # Define the custom model
# class CustomModel(keras.Model):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Define custom metrics
#         self.loss_tracker = keras.metrics.Mean(name="loss")
#         self.mae_metric = keras.metrics.MeanAbsoluteError(name="mae")

#     def train_step(self, data):
#         x, y = data

#         with tf.GradientTape() as tape:
#             y_pred = self(x, training=True)  # Forward pass
#             # Compute our own loss
#             loss = keras.losses.mean_squared_error(y, y_pred)

#         # Compute gradients
#         trainable_vars = self.trainable_variables
#         gradients = tape.gradient(loss, trainable_vars)

#         # Update weights
#         self.optimizer.apply_gradients(zip(gradients, trainable_vars))

#         # Compute our own metrics
#         self.loss_tracker.update_state(loss)
#         self.mae_metric.update_state(y, y_pred)
#         return {"loss": self.loss_tracker.result(), "mae": self.mae_metric.result()}

#     @property
#     def metrics(self):
#         # We list our `Metric` objects here so that `reset_states()` can be
#         # called automatically at the start of each epoch
#         # or at the start of `evaluate()`.
#         # If you don't implement this property, you have to call
#         # `reset_states()` yourself at the time of your choosing.
#         return [self.loss_tracker, self.mae_metric]

# # Construct an instance of CustomModel
# inputs = keras.Input(shape=(32,))
# outputs = keras.layers.Dense(1)(inputs)
# model = CustomModel(inputs, outputs)

# # Compile the model
# model.compile(optimizer="adam")

# # Generate some random data
# x = np.random.random((1000, 32))
# y = np.random.random((1000, 1))

# # Train the model
# model.fit(x, y, epochs=5)
