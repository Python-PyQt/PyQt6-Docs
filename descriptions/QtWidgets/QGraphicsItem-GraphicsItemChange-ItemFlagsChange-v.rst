.. sip:enum-member-description::
    :status: todo
    :value: 21
    :digest: 7593d39bfd862040f82bec0fad85f2e6

The item's flags change. The value argument is the new flags (i.e., a quint32). Do not call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setFlags` in :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange` as this notification is delivered. Instead, you can return the new flags from :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange`.
