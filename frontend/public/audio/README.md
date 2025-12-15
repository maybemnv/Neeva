# Meditation Audio Files

This directory contains meditation and relaxation audio files for the Wellness exercises.

## Required Audio Files

The following audio files are needed (all in MP3 format, 320kbps recommended):

1. **breathing.mp3** - Gentle breathing meditation music (5-10 min loop)
2. **meditation.mp3** - Deep meditation ambiance (10-15 min loop)
3. **peaceful.mp3** - Peaceful meditation sounds (8-12 min loop)
4. **calming.mp3** - Calming music for loving-kindness meditation (12-15 min loop)
5. **nature.mp3** - Nature sounds with gentle music (15-20 min loop)
6. **ocean.mp3** - Ocean waves and calming music (7-10 min loop)

## Recommended Sources for Royalty-Free Meditation Music

1. **YouTube Audio Library** (https://studio.youtube.com/channel/UC/music)
   - Filter by "Meditation" or "Ambient" genre
   - Download as MP3 using youtube-dl or similar tools

2. **Free Music Archive** (https://freemusicarchive.org/)
   - Search for "meditation", "ambient", "relaxation"
   - Ensure CC0 or CC-BY license

3. **Pixabay Music** (https://pixabay.com/music/)
   - Search for "meditation music"
   - All tracks are royalty-free

4. **Incompetech** (https://incompetech.com/)
   - Search for "meditation" or "ambient"
   - Attribution required

## Audio Specifications

- **Format**: MP3
- **Bitrate**: 320kbps (high quality)
- **Sample Rate**: 44.1kHz
- **Channels**: Stereo
- **Duration**: Should loop seamlessly
- **Volume**: Normalized to -14 LUFS

## Installation

1. Download the audio files from the sources above
2. Convert to MP3 if needed (using ffmpeg or similar)
3. Rename files according to the list above
4. Place all files in this directory (`public/audio/`)

## Example ffmpeg command to convert and optimize:

```bash
ffmpeg -i input.wav -codec:a libmp3lame -b:a 320k -ar 44100 output.mp3
```
