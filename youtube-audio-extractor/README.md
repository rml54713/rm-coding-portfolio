# YouTube Audio Extractor

A Python tool that extracts high-quality audio from YouTube videos and playlists without time restrictions, bypassing YouTube's built-in 1-hour download limits.

## Problem Solved

YouTube's native audio extraction has restrictive time limits, making it impossible to download full-length content like:
- Long-form podcasts
- Music mixes and DJ sets  
- Educational lectures
- Extended interviews

This tool removes those limitations while providing better quality control and batch processing.

## Features

- **No Time Limits**: Download videos of any length
- **Playlist Support**: Choose between single video or entire playlist
- **High Quality Audio**: 192kbps MP3 output
- **Smart URL Processing**: Handles both youtube.com and youtu.be formats
- **Interactive Interface**: User-friendly prompts and confirmations
- **Progress Tracking**: Real-time download progress
- **Error Handling**: Robust error checking and user feedback

## Installation

### Prerequisites
- Python 3.7 or higher
- FFmpeg (for audio conversion)

### Install FFmpeg

**Windows:**
```bash
# Using chocolatey
choco install ffmpeg

# Or download from: https://ffmpeg.org/download.html
```

**Mac:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
sudo apt update
sudo apt install ffmpeg
```

### Install Python Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage
```bash
python extract_audio.py
```

### Example Session
```
YouTube Audio Extractor
========================================
Extract audio from YouTube videos without time limits!

Enter YouTube URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Valid YouTube URL detected

Fetching video information...

============================================================
VIDEO: Rick Astley - Never Gonna Give You Up
Channel: Rick Astley
Duration: 03:32
Views: 1,234,567,890
============================================================

Ready to download video as MP3 audio
Continue? (y/n): y

Starting download...
Output directory: C:\git\rm-coding-portfolio\youtube-audio-extractor\downloads
--------------------------------------------------
[download] Destination: downloads\Rick Astley - Never Gonna Give You Up.mp3
[download] 100% of 8.2MiB in 00:05
--------------------------------------------------
Download completed successfully!
```

### Playlist Example
```
Enter YouTube URL: https://www.youtube.com/playlist?list=PLExample123

This URL contains a playlist with 25 videos.

What would you like to download?
1. Single video only
2. Entire playlist

Enter your choice (1 or 2): 2
```

## Output

- Downloads are saved to `downloads/` folder
- Files are named: `{Video Title}.mp3`
- Audio quality: 192kbps MP3
- Metadata preserved when possible

## Technical Details

### Supported URLs
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://www.youtube.com/playlist?list=PLAYLIST_ID`
- URLs with additional parameters (automatically cleaned)

### Audio Processing
- Extracts best available audio stream
- Converts to MP3 format using FFmpeg
- Maintains 192kbps quality for optimal file size/quality balance
- Preserves original metadata when available

### Error Handling
- Invalid URL detection
- Network connectivity issues
- Age-restricted content warnings
- Private/deleted video handling

## Troubleshooting

### Common Issues

**"FFmpeg not found"**
```bash
# Install FFmpeg (see installation section above)
# Verify installation:
ffmpeg -version
```

**"Video unavailable"**
- Video may be private, deleted, or region-restricted
- Try a different video URL

**"SSL Certificate error"**
```bash
# Update yt-dlp:
pip install --upgrade yt-dlp
```

**Slow download speeds**
- Large files take time - this is normal
- Check your internet connection
- YouTube may throttle download speeds

## Legal Notice

This tool is for personal use only. Please respect:
- YouTube's Terms of Service
- Copyright laws and fair use
- Content creators' rights

Only download content you have permission to use.

## Updates

The tool automatically uses the latest yt-dlp backend, which receives regular updates to handle YouTube's changes.

To update:
```bash
pip install --upgrade yt-dlp
```

## Tips

- **Large Playlists**: Downloads can take significant time
- **Quality**: 192kbps provides good balance of quality and file size
- **Organization**: Files are automatically organized in the downloads folder
- **Interruption**: Use Ctrl+C to safely cancel downloads

## Contributing

This is a portfolio project, but suggestions and improvements are welcome!