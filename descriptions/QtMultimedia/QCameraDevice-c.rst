.. sip:class-description::
    :status: todo
    :brief: General information about camera devices
    :digest: 8b3d088272717ade0d69ba52e783b326

The :sip:ref:`~PyQt6.QtMultimedia.QCameraDevice` class provides general information about camera devices.

:sip:ref:`~PyQt6.QtMultimedia.QCameraDevice` represents a physical camera device and its properties.

You can discover what cameras are available on a system using the availableCameras() and defaultCamera() functions. These are contained within QtMultimedia::MediaDevices.

The :sip:ref:`~PyQt6.QtMultimedia.QCameraDevice` instance retains its properties throughout its lifetime, even if the corresponding physical device is disconnected or its settings are modified. To keep track of updated properties, the user should load new instances of :sip:ref:`~PyQt6.QtMultimedia.QCameraDevice` from :sip:ref:`~PyQt6.QtMultimedia.QMediaDevices` when the relevant signals are fired.

This example prints the name of all available cameras:

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-camera.py
    :lines: 178-180

A :sip:ref:`~PyQt6.QtMultimedia.QCameraDevice` can be used to construct a :sip:ref:`~PyQt6.QtMultimedia.QCamera`. The following example instantiates a :sip:ref:`~PyQt6.QtMultimedia.QCamera` whose camera device is named ``mycamera``:

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-camera.py
    :lines: 187-191

You can also use :sip:ref:`~PyQt6.QtMultimedia.QCameraDevice` to get general information about a camera device such as description and physical position on the system.

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-camera.py
    :lines: 198-206

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QCamera`.
