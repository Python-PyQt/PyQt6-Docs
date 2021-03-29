.. sip:method-description::
    :status: todo
    :pysig: 127ec2d5e6f0b7f5dfc0ef0d9876dd36
    :realsig: (QEvent::Type,const QPoint&,const QPoint&)
    :digest: 38b5bf314d0c5770be5b59ad8e323a15

Constructs a help event with the given *type* corresponding to the widget-relative position specified by *pos* and the global position specified by *globalPos*.

*type* must be either :sip:ref:`~PyQt6.QtCore.QEvent.Type.ToolTip` or :sip:ref:`~PyQt6.QtCore.QEvent.Type.WhatsThis`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QHelpEvent.pos`, :sip:ref:`~PyQt6.QtGui.QHelpEvent.globalPos`.
