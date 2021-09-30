.. sip:method-description::
    :status: todo
    :pysig: c3b655ea6b3d1ee8994dd3a3353625ab
    :realsig: (Qt::NativeGestureType,const QPointingDevice*,int,const QPointF&,const QPointF&,const QPointF&,qreal,const QPointF&,quint64)
    :digest: cb775e800cd95f79017400fca6c779b3

Constructs a native gesture event of type *type* originating from *device* describing a gesture at *scenePos* in which *fingerCount* fingers are involved.

The points *localPos*, *scenePos* and *globalPos* specify the gesture position relative to the receiving widget or item, window, and screen or desktop, respectively.

*value* has a gesture-dependent interpretation: for RotateNativeGesture or SwipeNativeGesture, it's an angle in degrees. For ZoomNativeGesture, *value* is an incremental scaling factor, usually much less than 1, indicating that the target item should have its scale adjusted like this: item.scale = item.scale \* (1 + event.value)

For PanNativeGesture, *delta* gives the distance in pixels that the viewport, widget or item should be moved or panned.

**Note:** The *delta* is stored in single precision (\ :sip:ref:`~PyQt6.QtGui.QVector2D`), so :sip:ref:`~PyQt6.QtGui.QNativeGestureEvent.delta` may return slightly different values in some cases. This is subject to change in future versions of Qt.
