.. sip:method-description::
    :status: todo
    :pysig: 0445bd84a8153cfe86fab0ca19afa42c
    :realsig: (const QCameraDevice&)
    :digest: ecbfa80a0c7e9b9ae8d25e1559419f74

Connects the camera object to the physical camera device described by *cameraDevice*. Using a default constructed :sip:ref:`~PyQt6.QtMultimedia.QCameraDevice` object as *cameraDevice* will connect the camera to the system default camera device.

When switching camera devices, the :sip:ref:`~PyQt6.QtMultimedia.QCamera`'s capabilities are updated. Additionally, the :sip:ref:`~PyQt6.QtMultimedia.QCamera`'s control properties (such as :sip:ref:`~PyQt6.QtMultimedia.QCamera.focusMode`, :sip:ref:`~PyQt6.QtMultimedia.QCamera.flashMode`, :sip:ref:`~PyQt6.QtMultimedia.QCamera.focusDistance`, :sip:ref:`~PyQt6.QtMultimedia.QCamera.zoomFactor`) are updated as follows:

* If a property is supported on the new device, the property value is applied to the camera device.

* If a property is supported but its range of valid values was changed, the property is clamped to the new range and applied to the camera device.

* If the new camera device does not support a property, the property value is reset to default, and no changes are made to the camera device.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QCamera.cameraDevice`.
