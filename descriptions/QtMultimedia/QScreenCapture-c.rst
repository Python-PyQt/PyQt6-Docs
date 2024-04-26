.. sip:class-description::
    :status: todo
    :brief: This class is used for capturing a screen
    :digest: 90451be25a997a5de86c90e6d88af6bc

This class is used for capturing a screen.

The class captures a screen. It is managed by the :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession` class where the captured screen can be displayed in a video preview object or recorded to a file.

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-media.py
    :lines: 137-144

.. _qscreencapture-screen-capture-limitations:

Screen Capture Limitations
--------------------------

On Qt 6.5.2 and 6.5.3, the following limitations apply to using :sip:ref:`~PyQt6.QtMultimedia.QScreenCapture`:

* It is only supported with the FFmpeg backend.

* It is supported on all desktop platforms, except Linux with Wayland compositor, due to Wayland protocol restrictions and limitations.

* It is not supported on mobile operating systems, except on Android. There, you might run into performance issues as the class is currently implemented via :sip:ref:`~PyQt6.QtGui.QScreen.grabWindow`, which is not optimal for the use case.

* On Linux, it works with X11, but it has not been tested on embedded.

* In most cases, we set a screen capture frame rate that equals the screen refresh rate, except on Windows, where the rate might be flexible. Such a frame rate (75/120 FPS) might cause performance issues on weak CPUs if the captured screen is of 4K resolution.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QWindowCapture`, :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession`.
