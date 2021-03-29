.. sip:enum-member-description::
    :status: todo
    :value: 17
    :digest: 08ee6b14c307d5f4abb0d8c602011c7e

The item's cursor changes. The value argument is the new cursor (i.e., a `QCursor <https://doc.qt.io/qt-6/gui-changes-qt6.html#qcursor>`_). Do not call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setCursor` in :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange` as this notification is delivered. Instead, you can return a new cursor from :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange`.
