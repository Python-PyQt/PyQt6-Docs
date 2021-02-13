.. sip:method-description::
    :status: todo
    :pysig: dc77380dd11c6e7dd6375ca4f292cdf9
    :realsig: (Qt::ScreenOrientation,Qt::ScreenOrientation,const QRect&) const
    :digest: 97e2ae20d2c6fcf8c460a61f4941009e

Convenience function to compute a transform that maps from the coordinate system defined by orientation *a* into the coordinate system defined by orientation *b* and target dimensions *target*.

Example, *a* is Qt::Landscape, *b* is Qt::Portrait, and *target* is :sip:ref:`~PyQt6.QtCore.QRect`\ (0, 0, w, h) the resulting transform will be such that the point :sip:ref:`~PyQt6.QtCore.QPoint`\ (0, 0) is mapped to :sip:ref:`~PyQt6.QtCore.QPoint`\ (0, w), and :sip:ref:`~PyQt6.QtCore.QPoint`\ (h, w) is mapped to :sip:ref:`~PyQt6.QtCore.QPoint`\ (0, h). Thus, the landscape coordinate system :sip:ref:`~PyQt6.QtCore.QRect`\ (0, 0, h, w) is mapped (with a 90 degree rotation) into the portrait coordinate system :sip:ref:`~PyQt6.QtCore.QRect`\ (0, 0, w, h).

:sip:ref:`~PyQt6.QtCore.Qt.ScreenOrientations.PrimaryOrientation` is interpreted as the screen's :sip:ref:`~PyQt6.QtGui.QScreen.primaryOrientation`.
