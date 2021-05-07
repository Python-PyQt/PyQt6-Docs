.. sip:method-description::
    :status: todo
    :pysig: 045c03f5abcc60c1306c15ffd639c796
    :realsig: (QLayoutItem*,int,int,int,int,Qt::Alignment)
    :digest: a0bbbd8d0f3fc56b04a72c4cf73052dc

Adds *item* at position *row*, *column*, spanning *rowSpan* rows and *columnSpan* columns, and aligns it according to *alignment*. If *rowSpan* and/or *columnSpan* is -1, then the item will extend to the bottom and/or right edge, respectively. The layout takes ownership of the *item*.

**Warning:** Do not use this function to add child layouts or child widget items. Use :sip:ref:`~PyQt6.QtWidgets.QGridLayout.addLayout` or :sip:ref:`~PyQt6.QtWidgets.QGridLayout.addWidget` instead.
