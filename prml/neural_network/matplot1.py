import matplotlib.pyplot as plt

# Data extracted from the provided log
train_losses = [
    1.5325, 1.1022, 0.9189, 0.8039, 0.7271, 0.6735, 0.6278, 0.5881, 0.5577, 0.5310,
    0.4990, 0.4776, 0.4534, 0.4377, 0.4214, 0.4089, 0.3872, 0.3733, 0.3610, 0.3402,
    0.3307, 0.3180, 0.3138, 0.2994, 0.2897, 0.2836, 0.2714, 0.2629, 0.2551, 0.2451,
    0.1863, 0.1650, 0.1541, 0.1489, 0.1441, 0.1402, 0.1371, 0.1335, 0.1285, 0.1284,
    0.1220, 0.1190, 0.1163, 0.1107, 0.1124, 0.1070, 0.1055, 0.1089, 0.1090, 0.1075,
    0.1081, 0.1062, 0.1048, 0.1076, 0.1050, 0.1069, 0.1055, 0.1038, 0.1066, 0.1046,
    0.1059, 0.1066, 0.1076, 0.1068, 0.1066, 0.1054, 0.1050, 0.1062, 0.1058, 0.1076,
    0.1091, 0.1075, 0.1067, 0.1080, 0.1059, 0.1060, 0.1061, 0.1104, 0.1039, 0.1077,
    0.1068, 0.1051, 0.1080, 0.1080, 0.1080, 0.1082, 0.1066, 0.1092, 0.1065, 0.1088,
    0.1060, 0.1078, 0.1065, 0.1066, 0.1057, 0.1082, 0.1075, 0.1067, 0.1104, 0.1080
]

train_accuracies = [
    43.52, 60.72, 67.29, 71.52, 74.60, 76.53, 78.34, 79.83, 80.75, 81.60,
    82.81, 83.27, 84.31, 84.92, 85.39, 86.06, 86.75, 87.12, 87.62, 88.27,
    88.64, 89.02, 89.12, 89.68, 90.04, 90.12, 90.73, 90.81, 91.24, 91.56,
    93.81, 94.48, 94.86, 95.11, 95.30, 95.31, 95.50, 95.46, 95.79, 95.81,
    95.97, 96.17, 96.23, 96.38, 96.31, 96.58, 96.61, 96.47, 96.43, 96.59,
    96.47, 96.53, 96.61, 96.55, 96.61, 96.51, 96.67, 96.66, 96.55, 96.70,
    96.61, 96.53, 96.50, 96.41, 96.60, 96.56, 96.59, 96.59, 96.60, 96.44,
    96.51, 96.37, 96.50, 96.53, 96.53, 96.58, 96.47, 96.40, 96.72, 96.52,
    96.60, 96.64, 96.56, 96.56, 96.51, 96.45, 96.52, 96.47, 96.60, 96.46,
    96.62, 96.52, 96.59, 96.53, 96.57, 96.47, 96.48, 96.50, 96.47, 96.54
]

val_losses = [
    1.1768, 1.0135, 1.0095, 0.7044, 0.7976, 0.7645, 0.5956, 0.6027, 0.6125, 0.5197,
    0.5879, 0.4923, 0.5073, 0.7016, 0.4808, 0.4675, 0.4762, 0.5083, 0.5114, 0.4388,
    0.4853, 0.4400, 0.4482, 0.3739, 0.4703, 0.4915, 0.4100, 0.4038, 0.4514, 0.4001,
    0.3022, 0.2969, 0.2968, 0.2967, 0.3000, 0.2973, 0.2874, 0.2977, 0.2956, 0.3008,
    0.3028, 0.2975, 0.2989, 0.2929, 0.2995, 0.2922, 0.2995, 0.2946, 0.2959, 0.3001,
    0.2936, 0.2988, 0.2988, 0.2895, 0.3014, 0.2962, 0.2954, 0.3019, 0.2921, 0.2946,
    0.2986, 0.2949, 0.2993, 0.2962, 0.2938, 0.2927, 0.2939, 0.2994, 0.2915, 0.2973,
    0.2959, 0.2931, 0.3007, 0.2883, 0.2949, 0.2987, 0.2988, 0.2922, 0.2943, 0.2952,
    0.2980, 0.2963, 0.2936, 0.2988, 0.2956, 0.2995, 0.2985, 0.2931, 0.2946, 0.2925,
    0.2943, 0.2963, 0.3003, 0.2953, 0.2940, 0.3017, 0.2943, 0.2965, 0.2963, 0.2905
]

val_accuracies = [
    57.69, 62.45, 65.26, 75.22, 71.91, 73.60, 79.12, 78.84, 79.02, 82.01,
    80.10, 83.20, 82.82, 76.61, 83.68, 84.21, 83.75, 82.93, 82.42, 85.11,
    83.73, 85.09, 85.13, 87.25, 84.26, 83.92, 86.31, 86.35, 85.15, 86.55,
    89.45, 89.95, 90.39, 89.96, 89.99, 90.13, 90.59, 90.25, 90.13, 89.70,
    90.18, 90.33, 90.31, 90.25, 90.24, 90.36, 90.10, 90.35, 90.43, 90.15,
    90.22, 90.21, 90.47, 90.45, 90.28, 90.20, 90.24, 90.22, 90.59, 90.29,
    90.11, 90.14, 89.96, 90.42, 90.36, 90.39, 90.00, 90.49, 90.18, 90.33,
    90.38, 90.43, 89.91, 90.39, 90.27, 89.87, 90.48, 90.20, 90.32, 90.12,
    90.33, 90.35, 90.57, 90.18, 90.26, 90.03, 90.24, 90.29, 90.20, 90.37,
    90.49, 90.44, 90.18, 90.29, 90.27, 90.26, 90.10, 90.50, 90.26, 90.28
]

# Plot loss and accuracy curves
plt.figure(figsize=(12, 5))

# Loss plot
plt.subplot(1, 2, 1)
plt.plot(range(1, len(train_losses)+1), train_losses, label='Training Loss', color='blue')
plt.plot(range(1, len(val_losses)+1), val_losses, label='Validation Loss', color='orange')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Loss over Epochs')
plt.legend()

# Accuracy plot
plt.subplot(1, 2, 2)
plt.plot(range(1, len(train_accuracies)+1), train_accuracies, label='Training Accuracy', color='blue')
plt.plot(range(1, len(val_accuracies)+1), val_accuracies, label='Validation Accuracy', color='orange')
plt.xlabel('Epoch')
plt.ylabel('Accuracy (%)')
plt.title('Accuracy over Epochs')
plt.legend()

plt.tight_layout()
plt.show()