.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 87b00d8119d54e18821edc198517b575

This signal is emitted when the scene graph has submitted a frame. This is emitted after all other related signals, such as :sip:ref:`~PyQt6.QtQuick.QQuickWindow.afterRendering`. It is the last signal that is emitted by the scene graph rendering thread when rendering a frame.

**Note:** Unlike :sip:ref:`~PyQt6.QtQuick.QQuickWindow.frameSwapped`, this signal is guaranteed to be emitted also when the Qt Quick output is redirected via :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl`.

**Warning:** This signal is emitted from the scene graph rendering thread. If your slot function needs to finish before execution continues, you must make sure that the connection is direct (see :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType`).

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.beforeFrameBegin`, :sip:ref:`~PyQt6.QtQuick.QQuickWindow.rendererInterface`.
