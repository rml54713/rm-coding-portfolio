# RM Coding Portfolio

A collection of automation scripts and utilities showcasing use of Claude.ai to build automation scripts and problem-solving approaches.

## 🎵 YouTube Audio Extractor

**Problem:** Most online audio extraction tools have restrictive time limits, making it difficult to extract audio from longer content like podcasts, lectures, or live music mixes.

**Solution:** Built a Python script using yt-dlp that bypasses YouTube's 1-hour download restrictions, allowing extraction of full-length audio content in high quality formats. User clicks icon on desktop and prompts user for URL to extract.

**Technologies:** Python, yt-dlp, ffmpeg

**Features:**
Confirms if user wants to download single video or entire playlist (if applicable)
- Extracts audio from YouTube videos of any length
- Multiple output formats (MP3, WAV, M4A)
- Batch processing capabilities
- Quality selection options
- Places completed audio files in /music subfolder

## 📈 TradingView Pine Script Indicators

**Problem:** Standard TradingView indicators didn't provide the specific technical analysis functionality needed for my trading strategy, particularly lacking multi-timeframe confluence signals for scalping.

**Solution:** Developed custom Pine Script indicators tailored to specific market analysis requirements, improving signal accuracy and decision-making process through advanced technical analysis.

**Technologies:** Pine Script v6, TradingView Platform, Claude.ai

### Featured Indicator: 4x Stochastic Scalping

A sophisticated multi-timeframe stochastic oscillator that combines four different periods (9, 14, 40, 60) to identify high-probability reversal zones through confluence.

**Key Features:**
- **Multi-Timeframe Analysis:** Uses 4 stochastic periods for comprehensive momentum analysis
- **Confluence-Based Signals:** Background shading only appears when ALL stochastics agree on extreme conditions
- **Visual Clarity:** Color-coded lines (red, green, teal, magenta) with intuitive background highlighting
- **Customizable Parameters:** Adjustable overbought/oversold levels and smoothing periods

**Trading Application:**
- Identifies strong overbought conditions (red background) when all 4 stochastics > 80
- Highlights oversold opportunities (green background) when all 4 stochastics < 20
- Reduces false signals through multi-timeframe confirmation
- Optimized for scalping and short-term reversal strategies

**Technical Implementation:**
- Pine Script v6 with efficient calculation methods
- Clean indicator display without chart overlay
- Proper zone highlighting and reference lines

---

## 🛠 Technologies Used
- **Languages:** Python, Pine Script
- **Tools:** yt-dlp, ffmpeg, TradingView, Claude.ai
- **Focus Areas:** Automation, Financial Analysis, Media Processing

## Contact
Feel free to reach out for questions about any of these projects or potential collaborations @ rmendoza5418@gmail.com
