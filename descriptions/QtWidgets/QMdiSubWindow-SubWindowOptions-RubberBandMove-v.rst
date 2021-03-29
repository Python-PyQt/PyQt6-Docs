.. sip:enum-member-description::
    :status: todo
    :value: 0x8
    :realname: QMdiSubWindow::SubWindowOption::RubberBandMove
    :digest: ca6dcb0ac8f3379f201b9f8dc394874a

If you enable this option, a rubber band control is used to represent the subwindow's outline, and the user moves this instead of the subwindow itself. As a result, the subwindow remains in its original position until the move operation has completed, at which time a :sip:ref:`~PyQt6.QtGui.QMoveEvent` is sent to the window. By default, this option is disabled.
