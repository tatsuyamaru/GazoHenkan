from PIL import Image
import os

def convert_to_avif(input_path, output_path, quality, lossless):
    try:
        # Check if AVIF format is supported
        if '.avif' not in Image.registered_extensions():
            raise Exception("AVIF format not supported. Please install pillow-avif-plugin.")
        
        img = Image.open(input_path)
        output_dir = os.path.dirname(output_path)
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        print(f"Converting {input_path} to {output_path}")
        print(f"Quality: {quality}, Lossless: {lossless}")
        
        img.save(output_path, "AVIF", quality=quality, lossless=lossless)
        img.close()
        
        # Verify the file was created
        if os.path.exists(output_path):
            print(f"Successfully created: {output_path}")
            return True, output_path
        else:
            return False, "File was not created"
            
    except Exception as e:
        print(f"Error in convert_to_avif: {e}")
        return False, str(e)
