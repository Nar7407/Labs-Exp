import numpy as np
import scipy.ndimage as ndi

from exp11_common import banner

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    HAVE_MPL = True
except ImportError:
    HAVE_MPL = False


def to_grayscale(img):
    if img.ndim == 2:
        return img.astype(float)
    return (0.299 * img[..., 0] + 0.587 * img[..., 1] + 0.114 * img[..., 2]).astype(float)


def sobel_edges(gray):
    sx = ndi.sobel(gray, axis=0)
    sy = ndi.sobel(gray, axis=1)
    magnitude = ndi.gaussian_filter(np.hypot(sx, sy), sigma=1.0)
    return magnitude, magnitude > magnitude.mean()


def main():
    banner("PRACTICE 5 : scipy.datasets.face() - Edge Detection then Mean Filter")

    try:
        from scipy import datasets

        img = datasets.face()
        source = "scipy.datasets.face()"
    except Exception as exc:
        # face() ships as a raccoon image in recent SciPy; fall back to ascent().
        print(f"[info] datasets.face() unavailable ({exc}); using datasets.ascent()")
        from scipy import datasets

        img = datasets.ascent()
        source = "scipy.datasets.ascent()"

    print(f"Loaded : {source}")
    print(f"shape  : {img.shape}, dtype = {img.dtype}")
    print(f"value range : [{img.min()}, {img.max()}]")

    gray = to_grayscale(img)
    print(f"grayscale shape : {gray.shape}")

    print("\n--- Step 1 : edge detection ---")
    print("-" * 72)
    edges_soft, edges_bin = sobel_edges(gray)
    print(f"sobel(gray, axis=0) -> vertical gradient   range [{ndi.sobel(gray, axis=0).min():.1f}, "
          f"{ndi.sobel(gray, axis=0).max():.1f}]")
    print(f"sobel(gray, axis=1) -> horizontal gradient range [{ndi.sobel(gray, axis=1).min():.1f}, "
          f"{ndi.sobel(gray, axis=1).max():.1f}]")
    print(f"gradient magnitude range : [{edges_soft.min():.1f}, {edges_soft.max():.1f}]")
    print(f"thresholded at mean      : {edges_bin.mean():.1%} of pixels are edges")
    print(f"dtype of sobel output    : {ndi.sobel(gray, axis=0).dtype} "
          "(float, because the input was float)")

    print("\n--- Step 2 : uniform (mean) filter applied to the edge map ---")
    print("-" * 72)
    smoothed_edges = ndi.uniform_filter(edges_soft, size=5)
    smoothed_binary = ndi.uniform_filter(edges_bin.astype(float), size=5)
    print(f"uniform_filter(edges, size=5) range : [{smoothed_edges.min():.1f}, {smoothed_edges.max():.1f}]")
    print(f"peak sharpness reduced by smoothing : "
          f"{edges_soft.max():.1f} -> {smoothed_edges.max():.1f}")
    print(f"thresholded edge coverage after smoothing : {smoothed_binary.mean():.2%}")
    print("The mean filter blurs the thin edge lines, so nearby edges merge and noise is averaged away - the price of a stronger filter is a loss of detail.")

    print("\n--- Other operations from the theory section ---")
    print("-" * 72)
    flipped = np.fliplr(img)
    flipped_ud = np.flipud(img)
    rotated = ndi.rotate(gray, angle=45, reshape=True)
    rotated_360 = ndi.rotate(gray, angle=360)
    blurred = ndi.gaussian_filter(gray, sigma=3)
    median_blur = ndi.median_filter(gray, size=5)
    cropped = gray[50:400, 50:400]
    print(f"np.fliplr          -> {flipped.shape}")
    print(f"np.flipud          -> {flipped_ud.shape}")
    print(f"ndi.rotate(45)     -> {rotated.shape}  (reshape=True grows the canvas)")
    print(f"ndi.rotate(360)    -> {rotated_360.shape}  (round trip, back to original size)")
    print(f"round-trip max abs error : {np.abs(rotated_360 - gray).max():.2e}")
    print(f"gaussian_filter(sigma=3) -> {blurred.shape}")
    print(f"median_filter(size=5)    -> {median_blur.shape}  (preserves edges better)")
    print(f"plain NumPy crop   -> {cropped.shape}")
    print(f"uniform vs gaussian sd reduction : "
          f"{gray.std():.2f} -> {ndi.uniform_filter(gray, size=5).std():.2f} (uniform), "
          f"{blurred.std():.2f} (gaussian)")

    print("\nStructural operations on the binary edge mask:")
    struct = ndi.generate_binary_structure(2, 1)
    print(f"binary_dilation -> {ndi.binary_dilation(edges_bin, struct).mean():.2%} of pixels")
    print(f"binary_erosion  -> {ndi.binary_erosion(edges_bin, struct).mean():.2%} of pixels")
    print(f"binary_opening  -> {ndi.binary_opening(edges_bin, struct).mean():.2%} of pixels "
          "(removes speckle)")
    print(f"binary_closing  -> {ndi.binary_closing(edges_bin, struct).mean():.2%} of pixels "
          "(fills gaps)")

    if HAVE_MPL:
        fig, axes = plt.subplots(2, 4, figsize=(16, 8))
        panels = [
            (axes[0, 0], to_grayscale(img), "Original (grayscale)", "gray"),
            (axes[0, 1], edges_soft, "Step 1: sobel edges", "magma"),
            (axes[0, 2], smoothed_edges, "Step 2: mean filter on edges", "magma"),
            (axes[0, 3], img, "Original (RGB)", None),
            (axes[1, 0], flipped, "Flipped (np.fliplr)", None),
            (axes[1, 1], rotated, "Rotated 45 deg", "gray"),
            (axes[1, 2], blurred, "Blurred (gaussian sigma=3)", "gray"),
            (axes[1, 3], cropped, "Cropped [50:400, 50:400]", "gray"),
        ]
        for ax, data, title, cmap in panels:
            ax.imshow(data, cmap=cmap)
            ax.set_title(title, fontsize=10)
            ax.axis("off")
        plt.tight_layout()
        plt.savefig("practice5_image_ops.png", dpi=110)
        print("\nFigure written to practice5_image_ops.png (Agg backend, so it does not pop up; open the PNG to view the panels).")
        print("Delete the matplotlib.use(\"Agg\") line to get an interactive window instead.")
    else:
        print("\n[info] matplotlib not available - no figure produced.")


if __name__ == "__main__":
    main()