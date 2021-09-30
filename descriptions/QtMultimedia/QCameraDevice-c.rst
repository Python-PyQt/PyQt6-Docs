.. sip:class-description::
    :status: todo
    :brief: General information about camera devices
    :digest: 7ff465021d76dd8b3615d2633de60e37

The :sip:ref:`~PyQt6.QtMultimedia.QCameraDevice` class provides general information about camera devices.

:sip:ref:`~PyQt6.QtMultimedia.QCameraDevice` represents a physical camera device and its properties.

You can discover what cameras are available on a system using the availableCameras() and defaultCamera() functions. These are contained within QtMultimedia::MediaDevices.

This example prints the name of all available cameras:

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-camera.py
    :lines: 178-180

A :sip:ref:`~PyQt6.QtMultimedia.QCameraDevice` can be used to construct a :sip:ref:`~PyQt6.QtMultimedia.QCamera`. The following example instantiates a :sip:ref:`~PyQt6.QtMultimedia.QCamera` whose camera device is named ``mycamera``:

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-camera.py
    :lines: 187-191

You can also use :sip:ref:`~PyQt6.QtMultimedia.QCameraDevice` to get general information about a camera device such as description, physical position on the system, or camera sensor orientation.

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-camera.py
    :lines: 198-206

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QCamera`.
