.. sip:class-description::
    :status: todo
    :brief: This class is used for capturing a screen
    :digest: 5d14ce64f11a951d705f815f68b0d02a

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

* It is not supported on mobile operating systems, except on Android. Screen Capture on Android needs additional `Android foreground service permission <https://doc.qt.io/qt-6/https://developer.android.com/media/grow/media-projection#foreground_service_permission>`_ to be added to the ``AndroidManifest.xml`` file:

  ::

      <manifest ...>
      <uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
      <uses-permission android:name="android.permission.FOREGROUND_SERVICE_MEDIA_PROJECTION" />
      <application ...>
          <service android:name="org.qtproject.qt.android.multimedia.QtScreenCaptureService"
              android:foregroundServiceType="mediaProjection"
              android:exported="false"/>
          </service>
      </application>
      </manifest>

* On embedded with EGLFS, it has limited functionality. For Qt Quick applications, the class is currently implemented via :sip:ref:`~PyQt6.QtQuick.QQuickWindow.grabWindow`, which can cause performance issues.

* In most cases, we set a screen capture frame rate that equals the screen refresh rate, except on Windows, where the rate might be flexible. Such a frame rate (75/120 FPS) might cause performance issues on weak CPUs if the captured screen is of 4K resolution. On EGLFS, the capture frame rate is currently locked to 30 FPS.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QWindowCapture`, :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession`.
