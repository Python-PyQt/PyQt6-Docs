.. sip:method-description::
    :status: todo
    :pysig: 394afd13a1e1bf6f8890cf29c8be78a4
    :realsig: (QQuickItem::ItemChange,const QQuickItem::ItemChangeData&)
    :digest: 9f589b3333617ae9d31dd2508f201c67

Called when *change* occurs for this item.

*value* contains extra information relating to the change, when applicable.

If you re-implement this method in a subclass, be sure to call

::

    QQuickItem::itemChange(change, value);

typically at the end of your implementation, to ensure the :sip:ref:`~PyQt6.QtQuick.QQuickItem.windowChanged` signal will be emitted.
