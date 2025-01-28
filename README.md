sound-to-light-http
==================

Real-time detection of beats with Python from an audio input device (typically "Stereo Mix"). Outputs HTTP request to an API,
to be used for sound-to-light control.

It keeps track of the music "intensity" (calm, normal, intense) to switch lighting programs.

Required modules
----------------

- PyAudio
- PyQt5
- PyQwt
- matplotlib
- scipy

Usage
-----

`python beatDetector.py`

HTTP Requests
-----------

HTTP head requests are sent to `127.0.0.1:2890`, can be changed in `beatDetector.py`.

- `/beat` is sent for every beat detected.
- `/bar` is sent every to change the lighting scene.

Acknowledgments
---------------
Based on [scheb/sound-to-light-osc](https://github.com/scheb/sound-to-light-osc) [Original License](ORIGINAL_LICENSE)

This software is available under the [MIT license](LICENSE).
