.. sip:method-description::
    :status: todo
    :pysig: 96fbdb3f2fc49eb183b29310c6e4bd98
    :realsig: (const QLineF*,int)
    :digest: 496e8f8ec9586f22bca7560e65197ab6

The default implementation splits the list of lines in *lines* into *lineCount* separate calls to :sip:ref:`~PyQt6.QtGui.QPaintEngine.drawPath` or :sip:ref:`~PyQt6.QtGui.QPaintEngine.drawPolygon` depending on the feature set of the paint engine.
