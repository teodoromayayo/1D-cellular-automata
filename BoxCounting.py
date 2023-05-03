import numpy as np
import matplotlib.pylab as plt

def box_counting(matrix, scalements, printing=True):

    box_counts = []
    box_sizes = []

    for i in range(scalements):
        box_size = 2**i
        num_boxes_row = matrix.shape[0] // box_size
        num_boxes_col = matrix.shape[1] // box_size
        
        box_count = 0
        for r in range(num_boxes_row):
            for c in range(num_boxes_col):
                box = matrix[r*box_size:(r+1)*box_size, c*box_size:(c+1)*box_size]
                if np.sum(box) > 0:
                    box_count += 1
        
        box_counts.append(box_count)
        box_sizes.append(box_size)

    # Remove zero values from box_counts and box_sizes
    nonzero_indices = np.nonzero(box_counts[1:])[0]
    filtered_box_counts = np.array(box_counts[1:])[nonzero_indices]
    filtered_box_sizes = np.array(box_sizes[1:])[nonzero_indices]

    # Calculate logarithms
    log_box_counts = np.log(filtered_box_counts)
    log_box_sizes = np.log(filtered_box_sizes)

    slope, intercept = np.polyfit(log_box_sizes, log_box_counts, 1)
    fractal_dimension = -slope

    if printing:
        print(fractal_dimension)

    return slope, intercept, log_box_counts, log_box_sizes, fractal_dimension

def plot_fractal_dimension(CA, log_box_counts, log_box_sizes, intercept, slope):
    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))

    # Plot the cellular automata pattern
    axs[0].imshow(CA, cmap='binary', aspect='equal')
    axs[0].axis('off')

    # Plot the linear regression line in the log-log plot of box counts and box sizes
    axs[1].plot(log_box_sizes, log_box_counts, 'o')
    x = np.linspace(min(log_box_sizes), max(log_box_sizes), 100)
    y = slope * x + intercept
    axs[1].plot(x, y)
    axs[1].set_xlabel('log(r)')
    axs[1].set_ylabel('log(N(r))')
    axs[1].set_title('Fractal Dimension Regression')

    plt.show()
