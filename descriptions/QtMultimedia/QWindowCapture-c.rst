.. sip:class-description::
    :status: todo
    :brief: This class is used for capturing a window
    :digest: ca76b145ba03a6a65815bf0b38210f6d

This class is used for capturing a window.

The class captures a window. It is managed by the :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession` class where the captured window can be displayed in a video preview object or recorded to a file.

.. _qwindowcapture-window-capture-limitations:

Window Capture Limitations
--------------------------

The following limitations apply to using :sip:ref:`~PyQt6.QtMultimedia.QWindowCapture`:

* :sip:ref:`~PyQt6.QtMultimedia.QWindowCapture` is only supported with the FFmpeg backend.

The following limitations apply when using ``QWindowCapture`` on X11 systems:

* On Linux X11 systems, when a window is moved partially outside the visible screen area, only the visible region is captured. As a result, the emitted video frames may have a size smaller than the window’s geometry.

* Windows that are outside the visible screen area cannot be captured, and an error signal is emitted in that case.

* The behavior of minimized windows or those located on an invisible virtual workspace depends on the window manager. For example, such windows can be captured on GNOME, whereas on WindowMaker or Xfwm such capturing is not allowed, and the window capture instance emits an error.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession`, :sip:ref:`~PyQt6.QtMultimedia.QCapturableWindow`.
