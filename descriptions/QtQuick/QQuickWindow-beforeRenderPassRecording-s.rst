.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: adda268e52afe77b36359a411347ccd7

This signal is emitted before the scenegraph starts recording commands for the main render pass. (Layers have their own passes and are fully recorded by the time this signal is emitted.) The render pass is already active on the command buffer when the signal is emitted.

This signal is emitted later than :sip:ref:`~PyQt6.QtQuick.QQuickWindow.beforeRendering` and it guarantees that not just the frame, but also the recording of the scenegraph's main render pass is active. This allows inserting commands without having to generate an entire, separate render pass (which would typically clear the attached images). The native graphics objects can be queried via :sip:ref:`~PyQt6.QtQuick.QSGRendererInterface`.

**Note:** Resource updates (uploads, copies) typically cannot be enqueued from within a render pass. Therefore, more complex user rendering will need to connect to both :sip:ref:`~PyQt6.QtQuick.QQuickWindow.beforeRendering` and this signal.

**Warning:** This signal is emitted from the scene graph rendering thread. If your slot function needs to finish before execution continues, you must make sure that the connection is direct (see :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType`).

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.rendererInterface`, `Scene Graph - RHI Under QML <https://doc.qt.io/qt-6/qtquick-scenegraph-rhiunderqml-example.html>`_.
