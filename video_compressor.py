from moviepy.editor import VideoFileClip

def compress_video(input_path, output_path, resolution=(1920, 1080), audio_quality="high"):
    try:
        # Load video clip
        video_clip = VideoFileClip(input_path)

        # Set audio quality
        if audio_quality == "high":
            audio_codec = "aac"

        # Preserve the original video rotation
        rotation = video_clip.rotation

        # Rotate the video without cropping or stretching
        rotated_clip = video_clip.rotate(rotation)

        # Set resolution after rotation
        rotated_clip = rotated_clip.resize(resolution)

        # Write the compressed video to the output path
        rotated_clip.write_videofile(output_path, codec="libx264", audio_codec=audio_codec)

        print(f"Compression successful for {input_path}")
    except Exception as e:
        print(f"Error compressing {input_path}: {str(e)}")

def compress_folder(original_folder, compress_folder):
    import os

    # Ensure the compress folder exists
    if not os.path.exists(compress_folder):
        os.makedirs(compress_folder)

    # Iterate over all files in the original folder
    for filename in os.listdir(original_folder):
        if filename.endswith(".mp4"):
            input_path = os.path.join(original_folder, filename)
            output_path = os.path.join(compress_folder, filename)
            compress_video(input_path, output_path)

if __name__ == "__main__":
    # Folders path
    original_folder = r"G:\Himachal Pradesh\original"                 #folder path change as you require
    compress_folder_path = r"G:\Himachal Pradesh\sapan003"            #folder path change as you require

    # Compress videos in the original folder and save to the compress folder
    compress_folder(original_folder, compress_folder_path)