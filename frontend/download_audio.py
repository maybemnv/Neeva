"""
Download meditation audio files for the Wellness feature.
This script downloads royalty-free meditation music from various sources.
"""

import os
import urllib.request

# Create audio directory if it doesn't exist
audio_dir = "../public/audio"
os.makedirs(audio_dir, exist_ok=True)

# Free meditation audio URLs (these are placeholder URLs - replace with actual royalty-free sources)
# For production, download from:
# - Pixabay: https://pixabay.com/music/search/meditation/
# - YouTube Audio Library
# - Free Music Archive

audio_files = {
    "breathing.mp3": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",  # Placeholder
    "meditation.mp3": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",  # Placeholder
    "peaceful.mp3": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",  # Placeholder
    "calming.mp3": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3",  # Placeholder
    "nature.mp3": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3",  # Placeholder
    "ocean.mp3": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3",  # Placeholder
}

print("Downloading meditation audio files...")
print("Note: These are placeholder files. For production, use proper meditation music.")
print()

for filename, url in audio_files.items():
    filepath = os.path.join(audio_dir, filename)
    if os.path.exists(filepath):
        print(f"✓ {filename} already exists")
    else:
        try:
            print(f"Downloading {filename}...")
            urllib.request.urlretrieve(url, filepath)
            print(f"✓ Downloaded {filename}")
        except Exception as e:
            print(f"✗ Failed to download {filename}: {e}")

print()
print("Download complete!")
print(f"Audio files are in: {os.path.abspath(audio_dir)}")
print()
print("IMPORTANT: Replace these placeholder files with proper meditation music from:")
print("- Pixabay Music (https://pixabay.com/music/)")
print("- YouTube Audio Library")
print("- Free Music Archive")
