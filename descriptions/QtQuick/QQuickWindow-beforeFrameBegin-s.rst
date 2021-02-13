.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: bb66a2a7a1ea8c8cc499f9b073eb8fe2

This signal is emitted before the scene graph starts preparing the frame. This precedes signals like :sip:ref:`~PyQt6.QtQuick.QQuickWindow.beforeSynchronizing` or :sip:ref:`~PyQt6.QtQuick.QQuickWindow.beforeRendering`. It is the earliest signal that is emitted by the scene graph rendering thread when starting to prepare a new frame.

This signal is relevant for lower level graphics frameworks that need to execute certain operations, such as resource cleanup, at a stage where Qt Quick has not initiated the recording of a new frame via the underlying rendering hardware interface APIs.

**Warning:** This signal is emitted from the scene graph rendering thread. If your slot function needs to finish before execution continues, you must make sure that the connection is direct (see :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType`).

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.afterFrameEnd`, :sip:ref:`~PyQt6.QtQuick.QQuickWindow.rendererInterface`.
