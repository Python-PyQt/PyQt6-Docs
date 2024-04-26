.. sip:class-description::
    :status: todo
    :brief: Allows drawing of custom text objects in QTextDocuments
    :digest: 479fca2b0a03712fe420e6e9f42e39a8

The :sip:ref:`~PyQt6.QtGui.QTextObjectInterface` class allows drawing of custom text objects in :sip:ref:`~PyQt6.QtGui.QTextDocument`\ s.

A text object describes the structure of one or more elements in a text document; for instance, images imported from HTML are implemented using text objects. A text object knows how to lay out and draw its elements when a document is being rendered.

Qt allows custom text objects to be inserted into a document by registering a custom object type with :sip:ref:`~PyQt6.QtGui.QTextCharFormat`. A :sip:ref:`~PyQt6.QtGui.QTextObjectInterface` must also be implemented for this type and be :sip:ref:`~PyQt6.QtGui.QAbstractTextDocumentLayout.registerHandler` with the :sip:ref:`~PyQt6.QtGui.QAbstractTextDocumentLayout` of the document. When the object type is encountered while rendering a :sip:ref:`~PyQt6.QtGui.QTextDocument`, the :sip:ref:`~PyQt6.QtGui.QTextObjectInterface.intrinsicSize` and :sip:ref:`~PyQt6.QtGui.QTextObjectInterface.drawObject` functions of the interface are called.

The following list explains the required steps of inserting a custom text object into a document:

* Choose an *objectType*. The *objectType* is an integer with a value greater or equal to :sip:ref:`~PyQt6.QtGui.QTextFormat.ObjectTypes.UserObject`.

* Create a :sip:ref:`~PyQt6.QtGui.QTextCharFormat` object and set the object type to the chosen type using the setObjectType() function.

* Implement the :sip:ref:`~PyQt6.QtGui.QTextObjectInterface` class.

* Call :sip:ref:`~PyQt6.QtGui.QAbstractTextDocumentLayout.registerHandler` with an instance of your :sip:ref:`~PyQt6.QtGui.QTextObjectInterface` subclass to register your object type.

* Insert QChar::ObjectReplacementCharacter with the aforementioned :sip:ref:`~PyQt6.QtGui.QTextCharFormat` of the chosen object type into the document. As mentioned, the functions of :sip:ref:`~PyQt6.QtGui.QTextObjectInterface` :sip:ref:`~PyQt6.QtGui.QTextObjectInterface.intrinsicSize` and :sip:ref:`~PyQt6.QtGui.QTextObjectInterface.drawObject` will then be called with the :sip:ref:`~PyQt6.QtGui.QTextFormat` as parameter whenever the replacement character is encountered.

A class implementing a text object needs to inherit both :sip:ref:`~PyQt6.QtCore.QObject` and :sip:ref:`~PyQt6.QtGui.QTextObjectInterface`. :sip:ref:`~PyQt6.QtCore.QObject` must be the first class inherited. For instance:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-qtextobject-textobjectinterface.py
    :lines: 56-59

The data of a text object is usually stored in the :sip:ref:`~PyQt6.QtGui.QTextCharFormat` using QTextCharFormat::setProperty(), and then retrieved with QTextCharFormat::property().

**Warning:** Copy and Paste operations ignore custom text objects.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextCharFormat`, :sip:ref:`~PyQt6.QtGui.QTextLayout`.
