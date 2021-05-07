.. sip:method-description::
    :status: todo
    :pysig: 3da0cfa41fe4eb28b9dd0abc07098a7e
    :realsig: (const QPoint&,Qt::DropActions,const QMimeData*,Qt::MouseButtons,Qt::KeyboardModifiers)
    :digest: 7ff73229b27413e6d858cce38e0813dd

Constructs a :sip:ref:`~PyQt6.QtGui.QDragEnterEvent` that represents a drag entering a widget at the given *point* with mouse and keyboard states specified by *buttons* and *modifiers*.

The drag data is passed as MIME-encoded information in *data*, and the specified *actions* describe the possible types of drag and drop operation that can be performed.

**Warning:** Do not create a :sip:ref:`~PyQt6.QtGui.QDragEnterEvent` yourself since these objects rely on Qt's internal state.
