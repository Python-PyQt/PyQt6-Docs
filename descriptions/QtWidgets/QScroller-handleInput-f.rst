.. sip:method-description::
    :status: todo
    :pysig: 800110801748e76658ce24d02178c355
    :realsig: (QScroller::Input,const QPointF&,qint64)
    :digest: c0ff57c588ba9d40fb8b9e6c7b5b3fa5

This function is used by gesture recognizers to inform the scroller about a new input event. The scroller changes its internal :sip:ref:`~PyQt6.QtWidgets.QScroller.state` according to the input event and its attached scroller properties. The scroller doesn't distinguish between the kind of input device the event came from. Therefore the event needs to be split into the *input* type, a *position* and a milli-second *timestamp*. The *position* needs to be in the target's coordinate system.

The return value is ``true`` if the event should be consumed by the calling filter or ``false`` if the event should be forwarded to the control.

**Note:** Using :sip:ref:`~PyQt6.QtWidgets.QScroller.grabGesture` should be sufficient for most use cases.
