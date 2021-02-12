.. sip:method-description::
    :status: todo
    :pysig: 0281bb2a03f8f3624f862e1826a39fe8
    :realsig: (QObject*)
    :digest: 5c56ebe2d5c8b3311903ac7ae63091ed

Constructs an object with parent object *parent*.

The parent of an object may be viewed as the object's owner. For instance, a dialog box is the parent of the OK and Cancel buttons it contains.

The destructor of a parent object destroys all child objects.

Setting *parent* to ``nullptr`` constructs an object with no parent. If the object is a widget, it will become a top-level window.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.parent`, :sip:ref:`~PyQt6.QtCore.QObject.findChild`, :sip:ref:`~PyQt6.QtCore.QObject.findChildren`.
