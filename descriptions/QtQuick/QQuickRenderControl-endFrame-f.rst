.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 9e290459abc770ec8c7e888605084ccc

Specifies the end of a graphics frame. Calls to :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.sync` or :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.render` must be enclosed by calls to :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.beginFrame` and endFrame().

When this function is called, any graphics commands enqueued by the scenegraph are submitted to the context or command queue, whichever is applicable.

**Note:** This function does not need to be, and must not be, called when using the ``software`` adaptation of Qt Quick.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.beginFrame`, :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.initialize`, :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.sync`, :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.render`, :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsDevice`, :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget`.
