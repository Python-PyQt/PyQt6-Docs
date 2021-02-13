.. sip:method-description::
    :status: todo
    :pysig: fa96f590ea1a070763e292aef19ec3f7
    :realsig: (const QPoint&,Qt::DropActions,const QMimeData*,Qt::MouseButtons,Qt::KeyboardModifiers,QEvent::Type)
    :digest: a2438a755a5157c6472b57d7ea5544af

Creates a :sip:ref:`~PyQt6.QtGui.QDragMoveEvent` of the required *type* indicating that the mouse is at position *pos* given within a widget.

The mouse and keyboard states are specified by *buttons* and *modifiers*, and the *actions* describe the types of drag and drop operation that are possible. The drag data is passed as MIME-encoded information in *data*.

**Warning:** Do not attempt to create a :sip:ref:`~PyQt6.QtGui.QDragMoveEvent` yourself. These objects rely on Qt's internal state.
