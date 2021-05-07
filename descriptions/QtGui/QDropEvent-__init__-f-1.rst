.. sip:method-description::
    :status: todo
    :pysig: 5dfcaf55b11ed6a821af685e37dcaff9
    :realsig: (const QPointF&,Qt::DropActions,const QMimeData*,Qt::MouseButtons,Qt::KeyboardModifiers,QEvent::Type)
    :digest: 020ecafa0d24e3c59251fb02a90c7020

Constructs a drop event of a certain *type* corresponding to a drop at the point specified by *pos* in the destination widget's coordinate system.

The *actions* indicate which types of drag and drop operation can be performed, and the drag data is stored as MIME-encoded data in *data*.

The states of the mouse buttons and keyboard modifiers at the time of the drop are specified by *buttons* and *modifiers*.
