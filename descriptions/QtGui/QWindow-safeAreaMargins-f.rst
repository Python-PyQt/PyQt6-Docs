.. sip:method-description::
    :status: todo
    :pysig: 1cf12541c702e4d2092f5ca9947eb176
    :realsig: () const
    :digest: 6523cb3bfb53098ae607fa866b369235

Returns the safe area margins of the window.

The safe area represents the part of the window where content can be safely placed without risk of being obscured by, or conflicting with, other UI elements, such as system UIs.

The margins are relative to the internal geometry of the window, i.e :sip:ref:`~PyQt6.QtCore.QRect`\ (0, 0, :sip:ref:`~PyQt6.QtGui.QWindow.width`, :sip:ref:`~PyQt6.QtGui.QWindow.height`).

::

    void PaintDeviceWindow::paintEvent(QPaintEvent *)
    {
        QPainter painter(this);
        QRect rect(0, 0, width(), height());
        painter.fillRect(rect, QGradient::SunnyMorning);
        painter.fillRect(rect - safeAreaMargins(), QGradient::DustyGrass);
    }

.. seealso:: :sip:ref:`~PyQt6.QtGui.QWindow.geometry`, :sip:ref:`~PyQt6.QtGui.QWindow.safeAreaMarginsChanged`.
