import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('input.png', cv2.IMREAD_GRAYSCALE)

def median_filter(image, k=7): 
    pad = k // 2
    padded = np.pad(image, pad, mode='edge')
    output = np.zeros_like(image)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            window = padded[i:i+k, j:j+k]
            
            flattened = window.flatten()
            flattened.sort()
            output[i, j] = flattened[len(flattened) // 2]
    return output

def gaussian_kernel(size=5, sigma=3):
    ax = np.linspace(-(size//2), size//2, size)
    xx, yy = np.meshgrid(ax, ax)
    kernel = np.exp(-(xx**2 + yy**2)/(2*sigma**2))
    return kernel / np.sum(kernel)

def gaussian_filter(image, kernel):
    k = kernel.shape[0]
    pad = k // 2
    padded = np.pad(image, pad, mode='edge')
    output = np.zeros_like(image)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            window = padded[i:i+k, j:j+k]
            output[i, j] = np.sum(window * kernel)
    return output

def basic_contrast_brightness(image, alpha=1.5, beta=25):
    adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return adjusted

def unsharp_mask(image, blurred, alpha=1.3): 
    mask = image.astype(np.float32) - blurred.astype(np.float32)
    sharpened = image.astype(np.float32) + alpha * mask
    return np.clip(sharpened, 0, 255).astype(np.uint8)

img_bgr = cv2.imread('input.png')
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
r, g, b = cv2.split(img_rgb)

def process_channel(channel, channel_name=""):
    print(f"Memproses {channel_name} channel...")
    
    denoised = median_filter(channel, k=5) 
    adjusted = basic_contrast_brightness(denoised, alpha=1.2, beta=15)
    kernel = gaussian_kernel(3, 1)
    blurred_for_sharpen = gaussian_filter(adjusted, kernel)
    final_channel = unsharp_mask(adjusted, blurred_for_sharpen, alpha=0.8)
    
    return final_channel

r_final = process_channel(r, "Red")
g_final = process_channel(g, "Green")
b_final = process_channel(b, "Blue")

final_rgb = cv2.merge([r_final, g_final, b_final])

final_bgr = cv2.cvtColor(final_rgb, cv2.COLOR_RGB2BGR)
cv2.imwrite('output_color_improved4.jpg', final_bgr)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title("Original (Noisy)")
plt.imshow(img_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Restored Color (k=5)")
plt.imshow(final_rgb)
plt.axis('off')

plt.tight_layout()
plt.show()