.. sip:method-description::
    :status: todo
    :pysig: 4a9b6ff976c8634bba7ef0090644545e
    :realsig: (Qt::ScreenOrientation,Qt::ScreenOrientation,const QRect&) const
    :digest: 71b6cf4e6bed42e5017b80faed0d6654

Maps the rect between two screen orientations.

This will flip the x and y dimensions of the rectangle *rect* if the orientation *a* is :sip:ref:`~PyQt6.QtCore.Qt.ScreenOrientations.PortraitOrientation` or :sip:ref:`~PyQt6.QtCore.Qt.ScreenOrientations.InvertedPortraitOrientation` and orientation *b* is :sip:ref:`~PyQt6.QtCore.Qt.ScreenOrientations.LandscapeOrientation` or :sip:ref:`~PyQt6.QtCore.Qt.ScreenOrientations.InvertedLandscapeOrientation`, or vice versa.

:sip:ref:`~PyQt6.QtCore.Qt.ScreenOrientations.PrimaryOrientation` is interpreted as the screen's :sip:ref:`~PyQt6.QtGui.QScreen.primaryOrientation`.
