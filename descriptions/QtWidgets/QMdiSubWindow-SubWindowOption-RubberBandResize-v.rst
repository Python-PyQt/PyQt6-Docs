.. sip:enum-member-description::
    :status: todo
    :value: 0x4
    :digest: 045a826f477a16876ab499550d04cc4e

If you enable this option, a rubber band control is used to represent the subwindow's outline, and the user resizes this instead of the subwindow itself. As a result, the subwindow maintains its original position and size until the resize operation has been completed, at which time it will receive a single :sip:ref:`~PyQt6.QtGui.QResizeEvent`. By default, this option is disabled.
