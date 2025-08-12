#!/usr/bin/env python3
"""
YouTube Audio Extractor
A tool to download audio from YouTube videos or playlists using yt-dlp
Bypasses YouTube's 1-hour download restrictions
"""

import os
import sys
import re
from pathlib import Path
import yt_dlp


class YouTubeAudioExtractor:
    def __init__(self):
        self.output_dir = Path("downloads")
        self.output_dir.mkdir(exist_ok=True)
        
    def extract_base_url(self, url):
        """Extract and validate YouTube URL"""
        # Remove extra parameters and normalize URL
        if 'youtube.com' in url or 'youtu.be' in url:
            # Extract video ID or playlist ID
            if 'playlist' in url:
                playlist_match = re.search(r'list=([a-zA-Z0-9_-]+)', url)
                if playlist_match:
                    return f"https://www.youtube.com/playlist?list={playlist_match.group(1)}"
            else:
                # Handle both youtube.com and youtu.be formats
                video_match = re.search(r'(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]+)', url)
                if video_match:
                    return f"https://www.youtube.com/watch?v={video_match.group(1)}"
        
        raise ValueError("Invalid YouTube URL provided")
    
    def get_video_info(self, url):
        """Get video/playlist information without downloading"""
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                return info
        except Exception as e:
            raise Exception(f"Failed to get video info: {str(e)}")
    
    def download_audio(self, url, is_playlist=False):
        """Download audio from YouTube URL"""
        # Configure yt-dlp options for audio extraction
        ydl_opts = {
            'format': 'bestaudio/best',
            'extractaudio': True,
            'audioformat': 'mp3',
            'audioquality': '192',
            'outtmpl': str(self.output_dir / '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'noplaylist': not is_playlist,  # Download playlist only if explicitly requested
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print(f"\n🎵 Starting download...")
                print(f"📁 Output directory: {self.output_dir.absolute()}")
                print("-" * 50)
                
                ydl.download([url])
                
                print("-" * 50)
                print("✅ Download completed successfully!")
                
        except Exception as e:
            print(f"❌ Error during download: {str(e)}")
            sys.exit(1)
    
    def display_info(self, info, is_playlist=False):
        """Display video/playlist information"""
        print("\n" + "=" * 60)
        
        if is_playlist:
            print(f"📋 PLAYLIST: {info.get('title', 'Unknown Playlist')}")
            print(f"👤 Channel: {info.get('uploader', 'Unknown')}")
            print(f"🎬 Videos: {len(info.get('entries', []))} videos")
            
            # Show first few videos
            entries = info.get('entries', [])[:5]  # First 5 videos
            print(f"\n📝 First {len(entries)} videos:")
            for i, entry in enumerate(entries, 1):
                duration = self.format_duration(entry.get('duration', 0))
                print(f"   {i}. {entry.get('title', 'Unknown')} ({duration})")
            
            if len(info.get('entries', [])) > 5:
                print(f"   ... and {len(info.get('entries', [])) - 5} more videos")
                
        else:
            print(f"🎬 VIDEO: {info.get('title', 'Unknown Video')}")
            print(f"👤 Channel: {info.get('uploader', 'Unknown')}")
            print(f"⏱️  Duration: {self.format_duration(info.get('duration', 0))}")
            print(f"👀 Views: {info.get('view_count', 'Unknown'):,}" if info.get('view_count') else "👀 Views: Unknown")
        
        print("=" * 60)
    
    def format_duration(self, seconds):
        """Format duration from seconds to HH:MM:SS"""
        if not seconds:
            return "Unknown"
        
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        
        if hours > 0:
            return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        else:
            return f"{minutes:02d}:{seconds:02d}"
    
    def get_user_choice(self, info):
        """Ask user whether to download video or playlist"""
        # Check if URL contains a playlist
        has_playlist = 'entries' in info and len(info.get('entries', [])) > 1
        
        if not has_playlist:
            print("\n🎵 This appears to be a single video.")
            return False
        
        print(f"\n🤔 This URL contains a playlist with {len(info.get('entries', []))} videos.")
        print("\nWhat would you like to download?")
        print("1. Single video only")
        print("2. Entire playlist")
        
        while True:
            choice = input("\nEnter your choice (1 or 2): ").strip()
            if choice == "1":
                return False
            elif choice == "2":
                return True
            else:
                print("❌ Invalid choice. Please enter 1 or 2.")
    
    def run(self):
        """Main program execution"""
        print("🎵 YouTube Audio Extractor")
        print("=" * 40)
        print("Extract audio from YouTube videos without time limits!")
        print()
        
        # Get URL from user
        while True:
            try:
                url = input("🔗 Enter YouTube URL: ").strip()
                if not url:
                    print("❌ Please enter a valid URL.")
                    continue
                
                # Extract and validate base URL
                base_url = self.extract_base_url(url)
                print(f"✅ Valid YouTube URL detected")
                break
                
            except ValueError as e:
                print(f"❌ {str(e)}")
                print("Please enter a valid YouTube URL (youtube.com or youtu.be)")
        
        # Get video/playlist information
        try:
            print("\n🔍 Fetching video information...")
            info = self.get_video_info(base_url)
        except Exception as e:
            print(f"❌ {str(e)}")
            sys.exit(1)
        
        # Determine if it's a playlist and get user choice
        is_playlist = self.get_user_choice(info)
        
        # Display information
        self.display_info(info, is_playlist)
        
        # Confirm download
        print(f"\n📥 Ready to download {'playlist' if is_playlist else 'video'} as MP3 audio")
        confirm = input("Continue? (y/n): ").strip().lower()
        
        if confirm in ['y', 'yes']:
            self.download_audio(base_url, is_playlist)
        else:
            print("❌ Download cancelled.")


def main():
    """Main entry point"""
    try:
        extractor = YouTubeAudioExtractor()
        extractor.run()
    except KeyboardInterrupt:
        print("\n\n⏹️  Download interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()