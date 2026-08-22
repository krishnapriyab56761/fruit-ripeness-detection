import os
from collections import Counter
from PIL import Image

# ============================================================
# CONFIGURATION
# ============================================================

DATASET_PATH = r"D:\Projects\Fruit-Ripeness-detection\dataset\final_dataset"

SPLITS = ["train", "validation", "test"]

VALID_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".webp"
}


# ============================================================
# COUNT IMAGES
# ============================================================

def get_image_files(folder):

    image_files = []

    if not os.path.exists(folder):
        return image_files

    for root, dirs, files in os.walk(folder):

        for file in files:

            extension = os.path.splitext(file)[1].lower()

            if extension in VALID_EXTENSIONS:

                image_files.append(
                    os.path.join(root, file)
                )

    return image_files


# ============================================================
# CHECK CORRUPTED IMAGES
# ============================================================

def check_corrupted_images(image_files):

    corrupted = []

    for image_path in image_files:

        try:

            with Image.open(image_path) as img:

                img.verify()

        except Exception:

            corrupted.append(image_path)

    return corrupted


# ============================================================
# GET IMAGE INFORMATION
# ============================================================

def get_image_sizes(image_files):

    sizes = Counter()

    for image_path in image_files:

        try:

            with Image.open(image_path) as img:

                sizes[img.size] += 1

        except Exception:

            pass

    return sizes


# ============================================================
# CLASS-WISE COUNT
# ============================================================

def class_counts(split_path):

    counts = {}

    if not os.path.exists(split_path):

        return counts

    for class_name in sorted(os.listdir(split_path)):

        class_path = os.path.join(
            split_path,
            class_name
        )

        if not os.path.isdir(class_path):

            continue

        images = get_image_files(class_path)

        counts[class_name] = len(images)

    return counts


# ============================================================
# MAIN REPORT
# ============================================================

def main():

    print("=" * 70)
    print("             FRUIT DATASET REPORT")
    print("=" * 70)

    print("\nDataset location:")
    print(DATASET_PATH)

    print("\n")


    total_dataset_images = 0

    all_images = []


    # --------------------------------------------------------
    # SPLIT REPORT
    # --------------------------------------------------------

    for split in SPLITS:

        split_path = os.path.join(
            DATASET_PATH,
            split
        )

        print("-" * 70)
        print(f"{split.upper()} DATASET")
        print("-" * 70)

        if not os.path.exists(split_path):

            print("Folder not found!")
            continue


        counts = class_counts(split)

        split_total = sum(counts.values())

        total_dataset_images += split_total

        print(f"\nTotal {split} images: {split_total}")

        print("\nImages per class:")

        for class_name, count in counts.items():

            print(
                f"{class_name:<25} : {count}"
            )


        split_images = get_image_files(split_path)

        all_images.extend(split_images)


        # ----------------------------------------------------
        # FILE EXTENSIONS
        # ----------------------------------------------------

        extensions = Counter()

        for image_path in split_images:

            extension = os.path.splitext(
                image_path
            )[1].lower()

            extensions[extension] += 1


        print("\nFile types:")

        for extension, count in extensions.items():

            print(
                f"{extension:<10} : {count}"
            )


        # ----------------------------------------------------
        # IMAGE SIZE
        # ----------------------------------------------------

        sizes = get_image_sizes(split_images)

        print("\nImage sizes:")

        for size, count in sizes.most_common(10):

            print(
                f"{size[0]} x {size[1]} : {count}"
            )


    # ========================================================
    # TOTAL DATASET
    # ========================================================

    print("\n")
    print("=" * 70)
    print("TOTAL DATASET")
    print("=" * 70)

    print(
        f"\nTotal images in final dataset: "
        f"{total_dataset_images}"
    )


    # ========================================================
    # SPLIT PERCENTAGES
    # ========================================================

    print("\nDataset split percentage:")

    for split in SPLITS:

        split_path = os.path.join(
            DATASET_PATH,
            split
        )

        count = len(
            get_image_files(split_path)
        )

        if total_dataset_images > 0:

            percentage = (
                count /
                total_dataset_images
            ) * 100

        else:

            percentage = 0

        print(
            f"{split:<12}: "
            f"{count:<6} "
            f"({percentage:.2f}%)"
        )


    # ========================================================
    # CORRUPTED IMAGE CHECK
    # ========================================================

    print("\n")
    print("=" * 70)
    print("CORRUPTED IMAGE CHECK")
    print("=" * 70)

    print("\nChecking images...")

    corrupted = check_corrupted_images(
        all_images
    )

    print(
        f"\nTotal corrupted images: "
        f"{len(corrupted)}"
    )

    if corrupted:

        print("\nCorrupted files:")

        for image_path in corrupted:

            print(image_path)


    # ========================================================
    # CLASS BALANCE
    # ========================================================

    print("\n")
    print("=" * 70)
    print("CLASS BALANCE")
    print("=" * 70)

    total_class_counts = Counter()

    for image_path in all_images:

        relative_path = os.path.relpath(
            image_path,
            DATASET_PATH
        )

        parts = relative_path.split(
            os.sep
        )

        if len(parts) >= 2:

            class_name = parts[1]

            total_class_counts[
                class_name
            ] += 1


    for class_name, count in sorted(
        total_class_counts.items()
    ):

        print(
            f"{class_name:<25} : {count}"
        )


    # ========================================================
    # FINAL SUMMARY
    # ========================================================

    print("\n")
    print("=" * 70)
    print("FINAL SUMMARY")
    print("=" * 70)

    print(
        f"\nTotal images      : "
        f"{total_dataset_images}"
    )

    print(
        f"Corrupted images  : "
        f"{len(corrupted)}"
    )

    print(
        f"Valid images      : "
        f"{total_dataset_images - len(corrupted)}"
    )

    print(
        f"Number of classes : "
        f"{len(total_class_counts)}"
    )

    print("\nClasses:")

    for class_name in sorted(
        total_class_counts.keys()
    ):

        print(
            f"  - {class_name}"
        )


    print("\n")
    print("=" * 70)
    print("REPORT COMPLETED")
    print("=" * 70)


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":

    main()