.. sip:enum-member-description::
    :status: todo
    :value: 1
    :digest: 478ef71ec8a82131fadb44c1df67ad21

If set, a cursor should be shown inside the preedit string at position start. The length variable determines whether the cursor is visible or not. If the length is 0 the cursor is invisible. If value is a `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ of type :sip:ref:`~PyQt6.QtGui.QColor` this color will be used for rendering the cursor, otherwise the color of the surrounding text will be used. There should be at most one Cursor attribute per event. If several are specified the behaviour is undefined.
