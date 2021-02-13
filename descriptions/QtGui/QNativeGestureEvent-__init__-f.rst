.. sip:method-description::
    :status: todo
    :pysig: 90ac4f1d29730b91d85e6bd02ff01443
    :realsig: (Qt::NativeGestureType,const QPointingDevice*,const QPointF&,const QPointF&,const QPointF&,qreal,quint64,quint64)
    :digest: 9207e147b0f949aef3dfde1af5e50384

Constructs a native gesture event of type *type* originating from *device*.

The points *localPos*, *scenePos* and *globalPos* specify the gesture position relative to the receiving widget or item, window, and screen or desktop, respectively.

*realValue* is the macOS event parameter, *sequenceId* and *intValue* are the Windows event parameters.
