.. sip:method-description::
    :status: todo
    :pysig: 90ac4f1d29730b91d85e6bd02ff01443
    :realsig: (Qt::NativeGestureType,const QPointingDevice*,const QPointF&,const QPointF&,const QPointF&,qreal,quint64,quint64)
    :digest: 1e905daccc364c0a4c97fd4581241e07

Use the other constructor, because *intValue* is no longer stored separately.

Constructs a native gesture event of type *type* originating from *device*.

The points *localPos*, *scenePos* and *globalPos* specify the gesture position relative to the receiving widget or item, window, and screen or desktop, respectively.

*realValue* is the macOS event parameter, *sequenceId* and *intValue* are the Windows event parameters.

**Note:** It's not possible to store realValue and *intValue* simultaneously: one or the other must be zero. If *realValue* == 0 and *intValue* != 0, it is stored in the same variable, such that :sip:ref:`~PyQt6.QtGui.QNativeGestureEvent.value` returns the value given as *intValue*.
