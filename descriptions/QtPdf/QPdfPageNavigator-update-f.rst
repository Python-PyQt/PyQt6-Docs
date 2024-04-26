.. sip:method-description::
    :status: todo
    :pysig: 03bb21c65b6a4c6b1c7f6a11158e951b
    :realsig: (int,const QPointF&,qreal)
    :digest: 60ac83bae59483106273cea63e0ff13b

Modifies the current destination, consisting of *page*, *location* and *zoom*.

This can be called periodically while the user is manually moving around the document, so that after :sip:ref:`~PyQt6.QtPdf.QPdfPageNavigator.back` is called, :sip:ref:`~PyQt6.QtPdf.QPdfPageNavigator.forward` will jump back to the most-recently-viewed destination rather than the destination that was last specified by push().

The ``currentZoomChanged``, ``currentPageChanged`` and ``currentLocationChanged`` signals will be emitted if the respective properties are actually changed. The :sip:ref:`~PyQt6.QtPdf.QPdfPageNavigator.jumped` signal is not emitted, because this operation represents smooth movement rather than a navigational jump.
