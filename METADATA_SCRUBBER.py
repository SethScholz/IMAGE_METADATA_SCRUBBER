import os
import piexif
from PIL import Image
from tkinter import Tk, filedialog, messagebox

def remove_metadata(image_path):
    # Open image using Pillow
    img = Image.open(image_path)
    
    # Remove EXIF metadata
    try:
        if "exif" in img.info:
            exif_dict = piexif.load(img.info["exif"])
            exif_dict.clear()  # Clear EXIF data
            img.info["exif"] = piexif.dump(exif_dict)  # Remove EXIF metadata from the image
    except KeyError:
        pass  # No EXIF data to remove
    
    # Save the image without EXIF data
    new_image_path = os.path.splitext(image_path)[0] + "_no_metadata" + os.path.splitext(image_path)[1]

    # Ensure the image format is correct for saving
    try:
        img.save(new_image_path, format=img.format, exif=img.info.get("exif", b""))
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save the image: {e}")
        return None
    
    return new_image_path

def main():
    # Set up GUI for file selection
    Tk().withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title="Select an image", filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp;*.tiff")])
    
    if file_path:
        try:
            new_image = remove_metadata(file_path)
            if new_image:
                messagebox.showinfo("Success", f"Metadata successfully removed. New image saved as:\n{new_image}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showwarning("No File", "No file selected. Exiting.")

if __name__ == "__main__":
    main()