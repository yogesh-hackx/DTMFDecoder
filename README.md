# DTMFDecoder

Python Program to decode live audio for DTMF signals.
Its not actually a decoder though. It just listens to live audio and detects the DTMF signals.

## Requirements

### Python Libraries Used

    01. Pyttsx3 (just for Text To Speech Functionality)
### Other Packages
    
    01. multimon-ng (for decoding DTMF) (Note: Build from official repo manually, not from apt-get install command)
    02. espeak (to support pyttsx3)
