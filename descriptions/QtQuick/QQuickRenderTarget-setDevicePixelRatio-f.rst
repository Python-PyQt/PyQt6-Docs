.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: (qreal)
    :digest: 80640d127cc1008e29f7785c276f413a

Sets the device pixel ratio for this render target to *ratio*. This is the ratio between *device pixels* and *device independent pixels*.

Note that the specified device pixel ratio value will be ignored if :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.renderWindow` is re-implemented to return a valid :sip:ref:`~PyQt6.QtGui.QWindow`.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget.devicePixelRatio`.
