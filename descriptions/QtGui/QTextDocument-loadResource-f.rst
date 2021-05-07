.. sip:method-description::
    :status: todo
    :pysig: 6d0326a171f9010df7bb3ffa33de1b6a
    :realsig: (int,const QUrl&)
    :digest: 18a33f98b4ad6326f8b66b2cd775be60

Loads data of the specified *type* from the resource with the given *name*.

This function is called by the rich text engine to request data that isn't directly stored by :sip:ref:`~PyQt6.QtGui.QTextDocument`, but still associated with it. For example, images are referenced indirectly by the name attribute of a :sip:ref:`~PyQt6.QtGui.QTextImageFormat` object.

When called by Qt, *type* is one of the values of :sip:ref:`~PyQt6.QtGui.QTextDocument.ResourceType`.

If the :sip:ref:`~PyQt6.QtGui.QTextDocument` is a child object of a :sip:ref:`~PyQt6.QtCore.QObject` that has an invokable  method such as :sip:ref:`~PyQt6.QtWidgets.QTextEdit`, :sip:ref:`~PyQt6.QtWidgets.QTextBrowser` or a :sip:ref:`~PyQt6.QtGui.QTextDocument` itself then the default implementation tries to retrieve the data from the parent.

.. seealso:: QTextDocument::ResourceProvider.
