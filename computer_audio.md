# Computer Audio

Video games aren't much fun in silence.

Sound is actually pressure waves traveling through a medium like air.

Computers play digitized sounds which are stored in formats like WAV, MP3, and Ogg Vorbis.

Sound is recorded by computers using an analog to digital process which takes samples of audio at fixed intervals and turns them into numbers which can be stored in a computer file.

This sampling has a sample rate and sample size in bits (binary digits). Sample rate is measured in Hertz, which is a unit meaning how many times something happens a second. This cycle rate of a sound is called it's frequency. The sample rate determines how high a frequency of sound (high pitch) can be accurately recorded.

Humans can hear frequencies between approximately 20 Hz and 20000 Hz.

The sample rate used by audio CDs is 44100 Hz. Sample rates of about 8000 Hz are common because this is about the quality you need for speech to be clear.

* 8-bit integer: 48 dB

* 16-bit integer: 96 dB

* 24-bit integer: 145 dB

* 32-bit floating point: near-infinite dB

These bit depths are before any kind of data compression is used. For example, MP3 uses lossy data compression to approximate the original sounds with greatly reduced amount of storage.

Audio CDs and most computer audio file formats use 16-bit integers.

Another way to represent sound is with MIDI which is designed to represent musical instruments and music composed for them instead of directly representing the output sound in a digital form.



## Audio in PyGame Zero

For example, 3000 hz for 1 second would be:

Here is an example of playing a tone with PyGame Zero.

```python
my_tone= tone.create(3000, 1.0)
my_tone.play()

```

You can play sounds from .wav or .ogg files in your games “sound” directory like this:



If your file is named “drum.wav” in “sounds” then this would play it in PyGame Zero.

```python
sounds.drum.play()
```

TODO: example of playing music with PyGame Zero

## References

- https://manual.audacityteam.org/man/digital_audio.html
- https://www.lifewire.com/computer-audio-basics-831415
- https://pygame-zero.readthedocs.io/en/stable/builtins.html#tone-generator 