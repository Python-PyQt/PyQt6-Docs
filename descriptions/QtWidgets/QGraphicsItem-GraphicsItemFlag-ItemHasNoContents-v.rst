.. sip:enum-member-description::
    :status: todo
    :value: 0x400
    :digest: c52635a3db31fb64f0472e6bb7029806

The item does not paint anything (i.e., calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.paint` on the item has no effect). You should set this flag on items that do not need to be painted to ensure that Graphics View avoids unnecessary painting preparations. This flag was introduced in Qt 4.6.
