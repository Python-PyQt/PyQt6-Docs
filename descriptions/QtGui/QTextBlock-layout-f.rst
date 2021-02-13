.. sip:method-description::
    :status: todo
    :pysig: 2cf0ee2c1ec88bcb163991c24a7dec99
    :realsig: () const
    :digest: e55f189b67e39a2a10e520d467a1ea54

Returns the :sip:ref:`~PyQt6.QtGui.QTextLayout` that is used to lay out and display the block's contents.

Note that the returned :sip:ref:`~PyQt6.QtGui.QTextLayout` object can only be modified from the documentChanged implementation of a :sip:ref:`~PyQt6.QtGui.QAbstractTextDocumentLayout` subclass. Any changes applied from the outside cause undefined behavior.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextBlock.clearLayout`.
