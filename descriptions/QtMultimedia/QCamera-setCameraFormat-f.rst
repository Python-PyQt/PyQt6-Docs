.. sip:method-description::
    :status: todo
    :pysig: 93e6817a3a4c4747a2212b26971bbed6
    :realsig: (const QCameraFormat&)
    :digest: b31a6d16210f6885591f02208bd466ab

Tells the camera to use the format described by *format*. This can be used to define a specific resolution and frame rate to be used for recording and image capture.

**Note:** When using the FFMPEG backend on an Android target device if you request **YUV420P** format, you will receive either a fully planar 4:2:0 YUV420P or a semi-planar NV12/NV21. This depends on the codec implemented by the device OEM.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QCamera.cameraFormat`.
