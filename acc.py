import matplotlib.pyplot as plt

# Sample data for accuracy and precision
thresholds = [0.1, 0.2, 0.3, 0.4, 0.5]  # Threshold values
accuracy = [0.8, 0.75, 0.85, 0.82, 0.78]  # Accuracy values
precision = [0.9, 0.88, 0.92, 0.85, 0.87]  # Precision values

# Plotting the accuracy-precision matrix
plt.plot(thresholds, accuracy, label='Accuracy')
plt.plot(thresholds, precision, label='Precision')
plt.xlabel('Threshold')
plt.ylabel('Value')
plt.title('Accuracy-Precision Matrix')
plt.legend()
plt.show()
