# TOOLS.md - Local Notes

Skills define *how* tools work. This file is for *your* specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:
- Camera names and locations
- SSH hosts and aliases  
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Current Capabilities (Updated 2026-01-27)

### TTS (sag - ElevenLabs)
- Available for voice storytelling, movie summaries, "storytime" moments
- Preferred voice: *(to be determined)*

### Smart Home
- **Hue Lights** (openhue) - Philips Hue lighting control
- **Sonos** (sonoscli) - Speaker control
  - Room/speaker names: *(to be configured)*

### Content & Notes
- **Obsidian** - Note management and knowledge organization
- **Whisper** (openai-whisper-api) - Audio transcription

### Development
- **Oracle** - Second-model review for debugging, refactors, design checks

## Examples

```markdown
### Cameras
- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH
- home-server → 192.168.1.100, user: admin

### TTS
- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
