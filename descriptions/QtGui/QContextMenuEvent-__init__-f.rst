.. sip:method-description::
    :status: todo
    :pysig: c6368d92cf89818d3532cb87b7380050
    :realsig: (QContextMenuEvent::Reason,const QPoint&)
    :digest: 83b9b11dff67ad497a0a160a1b823166

Constructs a context menu event object with the accept parameter flag set to false.

The *reason* parameter must be :sip:ref:`~PyQt6.QtGui.QContextMenuEvent.Reason.Mouse` or :sip:ref:`~PyQt6.QtGui.QContextMenuEvent.Reason.Keyboard`.

The *pos* parameter specifies the mouse position relative to the receiving widget.

The :sip:ref:`~PyQt6.QtGui.QContextMenuEvent.globalPos` is initialized to :sip:ref:`~PyQt6.QtGui.QCursor.pos`, which may not be appropriate. Use the other constructor to specify the global position explicitly.
