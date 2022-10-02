.. sip:method-description::
    :status: todo
    :pysig: a41915d457521b2882989770f0d7a4c1
    :realsig: (QPaintDevice*)
    :digest: 5d593923c09cbf5cd77fd2a07b785ffe

Returns a new :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget` referencing a paint device object specified by *device*.

This option of redirecting rendering to a :sip:ref:`~PyQt6.QtGui.QPaintDevice` is available only when running with the ``software`` backend of Qt Quick.

**Note:** The :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget` does not take ownship of *device*, it is the caller's responsibility to ensure the object exists as long as necessary.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setRenderTarget`, :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl`.
