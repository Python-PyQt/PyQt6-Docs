.. sip:signal-description::
    :status: todo
    :pysig: a3840e2897b437c5116087497aff268c
    :realsig: (QRect,QPointF,QPointF)
    :digest: 37d4b6be71641cad71b828135de4e9d3

This signal is emitted when the rubber band rect is changed. The viewport Rect is specified by *rubberBandRect*. The drag start position and drag end position are provided in scene points with *fromScenePoint* and *toScenePoint*.

When rubberband selection ends this signal will be emitted with null vales.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.rubberBandRect`.
