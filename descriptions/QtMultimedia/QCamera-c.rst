.. sip:class-description::
    :status: todo
    :brief: Interface for system camera devices
    :digest: 718f0e00c2339475b4d8aeb6500d739d

The :sip:ref:`~PyQt6.QtMultimedia.QCamera` class provides interface for system camera devices.

:sip:ref:`~PyQt6.QtMultimedia.QCamera` can be used within a :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession` for video recording and image taking.

You can use :sip:ref:`~PyQt6.QtMultimedia.QCameraDevice` to list available cameras and choose which one to use.

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-camera.py
    :lines: 187-191

On hardware that supports it, :sip:ref:`~PyQt6.QtMultimedia.QCamera` lets you adjust the focus and zoom. This also includes functionality such as a "Macro" mode for close up work (e.g. reading barcodes, or recognizing letters), or "touch to focus" - indicating an interesting area of the image for the hardware to attempt to focus on.

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-camera.py
    :lines: 244-245

The :sip:ref:`~PyQt6.QtMultimedia.QCamera.minimumZoomFactor` and :sip:ref:`~PyQt6.QtMultimedia.QCamera.maximumZoomFactor` methods provide the range of supported zoom factors. The :sip:ref:`~PyQt6.QtMultimedia.QCamera.zoomTo` method allows changing the zoom factor.

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-camera.py
    :lines: 249-249

After capturing the raw data for a camera frame, the camera hardware and software performs various image processing tasks to produce the final image. This includes compensating for ambient light color, reducing noise, as well as making some other adjustments to the image.

You can control many of these processing steps through the Camera properties. For example, you can set the white balance (or color temperature) used for processing images:

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-camera.py
    :lines: 237-237

For more information on image processing of camera frames, see `Camera Image Processing <https://doc.qt.io/qt-6/cameraoverview.html#camera-implementation-details-controlling-the-imaging-pipeline-image-processing-13>`_.

See the `camera overview <https://doc.qt.io/qt-6/cameraoverview.html>`_ for more information.

**Note:** On WebAssembly platform, due to it's asynchronous nature, :sip:ref:`~PyQt6.QtMultimedia.QMediaDevices.videoInputsChanged` signal is emitted when the list of video inputs is ready. User permissions are required. Works only on secure https contexts.
