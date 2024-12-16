.. sip:class-description::
    :status: todo
    :brief: This class is used for capturing a screen
    :digest: 2ca07da47921d561d55ea0c1bd3592ab

This class is used for capturing a screen.

The class captures a screen. It is managed by the :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession` class where the captured screen can be displayed in a video preview object or recorded to a file.

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-media.py
    :lines: 137-144

.. _qscreencapture-screen-capture-limitations:

Screen Capture Limitations
--------------------------

On Qt 6.5.2 and above, the following limitations apply to using :sip:ref:`~PyQt6.QtMultimedia.QScreenCapture`:

* It is only supported with the FFmpeg backend.

* On Linux systems using the Wayland compositor, the screen capture implementation is experimental and comes with the following limitations. Due to restrictions of the Wayland protocol, it's impossible to set and get the target screen via the API of the ``QScreenCapture`` class. Instead, the OS will show a screen selection wizard upon invoking ``QScreenCapture::setActive(true)``. The screen capture feature requires the installation of the `ScreenCast <https://flatpak.github.io/xdg-desktop-portal/docs/doc-org.freedesktop.portal.ScreenCast.html>`_ service supported via `XDG Desktop Portal <https://flatpak.github.io/xdg-desktop-portal/docs/>`_ and {https://pipewire.org/}{PipeWire} (0.3). These limitations might change in the future.

* It is not supported on mobile operating systems, except on Android. There, you might run into performance issues as the class is currently implemented via :sip:ref:`~PyQt6.QtGui.QScreen.grabWindow`, which is not optimal for the use case.

* On embedded with EGLFS, it has limited functionality. For Qt Quick applications, the class is currently implemented via :sip:ref:`~PyQt6.QtQuick.QQuickWindow.grabWindow`, which can cause performance issues.

* In most cases, we set a screen capture frame rate that equals the screen refresh rate, except on Windows, where the rate might be flexible. Such a frame rate (75/120 FPS) might cause performance issues on weak CPUs if the captured screen is of 4K resolution. On EGLFS, the capture frame rate is currently locked to 30 FPS.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QWindowCapture`, :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession`.
