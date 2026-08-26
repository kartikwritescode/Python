import cv2
import matplotlib.pyplot as plt


# ---------------------------------------------------------
# Load images
# ---------------------------------------------------------

img1 = cv2.imread(
    "clg_lab/opencv/image1.jpg",
    cv2.IMREAD_GRAYSCALE
)

img2 = cv2.imread(
    "clg_lab/opencv/image2.jpg",
    cv2.IMREAD_GRAYSCALE
)

if img1 is None or img2 is None:
    raise ValueError("Could not load images. Check the file paths.")


# ---------------------------------------------------------
# 1. SIFT + Brute Force
# ---------------------------------------------------------

def sift_bruteforce(img1, img2):

    # Create SIFT detector
    sift = cv2.SIFT_create()

    # Detect keypoints and descriptors
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    # Brute Force matcher
    # SIFT descriptors are floating-point
    # Therefore, use L2 distance
    bf = cv2.BFMatcher(
        cv2.NORM_L2,
        crossCheck=True
    )

    # Match descriptors
    matches = bf.match(des1, des2)

    # Sort matches according to distance
    matches = sorted(
        matches,
        key=lambda x: x.distance
    )

    # Draw top 50 matches
    result = cv2.drawMatches(
        img1,
        kp1,
        img2,
        kp2,
        matches[:50],
        None,
        flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
    )

    return result


# ---------------------------------------------------------
# 2. ORB + Brute Force
# ---------------------------------------------------------

def orb_bruteforce(img1, img2):

    # Create ORB detector
    orb = cv2.ORB_create()

    # Detect keypoints and descriptors
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    # ORB produces binary descriptors
    # Therefore, use Hamming distance
    bf = cv2.BFMatcher(
        cv2.NORM_HAMMING,
        crossCheck=True
    )

    # Match descriptors
    matches = bf.match(des1, des2)

    # Sort matches according to distance
    matches = sorted(
        matches,
        key=lambda x: x.distance
    )

    # Draw top 50 matches
    result = cv2.drawMatches(
        img1,
        kp1,
        img2,
        kp2,
        matches[:50],
        None,
        flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
    )

    return result


# ---------------------------------------------------------
# 3. SIFT + FLANN
# ---------------------------------------------------------

def sift_flann(img1, img2):

    # Create SIFT detector
    sift = cv2.SIFT_create()

    # Detect keypoints and descriptors
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    # FLANN parameters for SIFT
    # Algorithm 1 = KD-Tree
    index_params = dict(
        algorithm=1,
        trees=5
    )

    search_params = dict(
        checks=50
    )

    # Create FLANN matcher
    flann = cv2.FlannBasedMatcher(
        index_params,
        search_params
    )

    # K-nearest-neighbor matching
    # k=2 gives the two closest matches
    matches = flann.knnMatch(
        des1,
        des2,
        k=2
    )

    # Lowe's ratio test
    good_matches = []

    for m, n in matches:

        if m.distance < 0.7 * n.distance:
            good_matches.append(m)

    # Draw top 50 good matches
    result = cv2.drawMatches(
        img1,
        kp1,
        img2,
        kp2,
        good_matches[:50],
        None,
        flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
    )

    return result


# ---------------------------------------------------------
# 4. ORB + FLANN
# ---------------------------------------------------------

def orb_flann(img1, img2):

    # Create ORB detector
    orb = cv2.ORB_create()

    # Detect keypoints and descriptors
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    # FLANN parameters for ORB
    # Algorithm 6 = LSH
    index_params = dict(
        algorithm=6,
        table_number=6,
        key_size=12,
        multi_probe_level=1
    )

    search_params = dict(
        checks=50
    )

    # Create FLANN matcher
    flann = cv2.FlannBasedMatcher(
        index_params,
        search_params
    )

    # K-nearest-neighbor matching
    matches = flann.knnMatch(
        des1,
        des2,
        k=2
    )

    # Lowe's ratio test
    good_matches = []

    for m, n in matches:

        if m.distance < 0.7 * n.distance:
            good_matches.append(m)

    # Draw top 50 good matches
    result = cv2.drawMatches(
        img1,
        kp1,
        img2,
        kp2,
        good_matches[:50],
        None,
        flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
    )

    return result


# ---------------------------------------------------------
# Run all four methods
# ---------------------------------------------------------

result_sift_bf = sift_bruteforce(img1, img2)

result_orb_bf = orb_bruteforce(img1, img2)

result_sift_flann = sift_flann(img1, img2)

result_orb_flann = orb_flann(img1, img2)


# ---------------------------------------------------------
# Display results
# ---------------------------------------------------------

plt.figure(figsize=(18, 12))


# SIFT + Brute Force
plt.subplot(2, 2, 1)

plt.imshow(
    result_sift_bf,
    cmap="gray"
)

plt.title("SIFT + Brute Force")

plt.axis("off")


# ORB + Brute Force
plt.subplot(2, 2, 2)

plt.imshow(
    result_orb_bf,
    cmap="gray"
)

plt.title("ORB + Brute Force")

plt.axis("off")


# SIFT + FLANN
plt.subplot(2, 2, 3)

plt.imshow(
    result_sift_flann,
    cmap="gray"
)

plt.title("SIFT + FLANN")

plt.axis("off")


# ORB + FLANN
plt.subplot(2, 2, 4)

plt.imshow(
    result_orb_flann,
    cmap="gray"
)

plt.title("ORB + FLANN")

plt.axis("off")


# Adjust spacing
plt.tight_layout()

# Show results
plt.show()