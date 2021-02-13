.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: (qreal)
    :digest: 435d6acf5e2063b62400d9b539fd1035

Specifies the curve flattening *threshold*, controlling the granularity with which the generated outlines' curve is drawn.

The default threshold is a well adjusted value (0.25), and normally you should not need to modify it. However, you can make the curve's appearance smoother by decreasing its value.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainterPathStroker.curveThreshold`.
