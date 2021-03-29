.. sip:method-description::
    :status: todo
    :pysig: 0281bb2a03f8f3624f862e1826a39fe8
    :realsig: (QObject*)
    :digest: fcc2f8839a2fc275f51b78fe5e0cbcff

Constructs an object with parent object *parent*.

The parent of an object may be viewed as the object's owner. For instance, a :sip:ref:`~PyQt6.QtWidgets.QDialog` is the parent of the OK and Cancel buttons it contains.

The destructor of a parent object destroys all child objects.

Setting *parent* to ``nullptr`` constructs an object with no parent. If the object is a widget, it will become a top-level window.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.parent`, :sip:ref:`~PyQt6.QtCore.QObject.findChild`, :sip:ref:`~PyQt6.QtCore.QObject.findChildren`.
