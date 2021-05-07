.. sip:method-description::
    :status: todo
    :pysig: b7e84e53784501ac47d2f0cd6c00d120
    :realsig: (Qt::ScreenOrientation,Qt::ScreenOrientation,const QRect&) const
    :digest: 71b6cf4e6bed42e5017b80faed0d6654

Maps the rect between two screen orientations.

This will flip the x and y dimensions of the rectangle *rect* if the orientation *a* is :sip:ref:`~PyQt6.QtCore.Qt.ScreenOrientation.PortraitOrientation` or :sip:ref:`~PyQt6.QtCore.Qt.ScreenOrientation.InvertedPortraitOrientation` and orientation *b* is :sip:ref:`~PyQt6.QtCore.Qt.ScreenOrientation.LandscapeOrientation` or :sip:ref:`~PyQt6.QtCore.Qt.ScreenOrientation.InvertedLandscapeOrientation`, or vice versa.

:sip:ref:`~PyQt6.QtCore.Qt.ScreenOrientation.PrimaryOrientation` is interpreted as the screen's :sip:ref:`~PyQt6.QtGui.QScreen.primaryOrientation`.
