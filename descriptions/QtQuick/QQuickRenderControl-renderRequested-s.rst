.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 11fe7ff45e2d104301345c638b137f83

This signal is emitted when the scene graph needs to be rendered. It is not necessary to call :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.sync`.

**Note:** Avoid triggering rendering directly when this signal is emitted. Instead, prefer deferring it by using a timer for example. This will lead to better performance.
