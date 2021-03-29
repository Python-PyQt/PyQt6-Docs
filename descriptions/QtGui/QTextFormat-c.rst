.. sip:class-description::
    :status: todo
    :brief: Formatting information for a QTextDocument
    :digest: b553c2229068617f798a4c80dc9e6d65

The :sip:ref:`~PyQt6.QtGui.QTextFormat` class provides formatting information for a :sip:ref:`~PyQt6.QtGui.QTextDocument`.

A :sip:ref:`~PyQt6.QtGui.QTextFormat` is a generic class used for describing the format of parts of a :sip:ref:`~PyQt6.QtGui.QTextDocument`. The derived classes :sip:ref:`~PyQt6.QtGui.QTextCharFormat`, :sip:ref:`~PyQt6.QtGui.QTextBlockFormat`, :sip:ref:`~PyQt6.QtGui.QTextListFormat`, and :sip:ref:`~PyQt6.QtGui.QTextTableFormat` are usually more useful, and describe the formatting that is applied to specific parts of the document.

A format has a ``FormatType`` which specifies the kinds of text item it can format; e.g. a block of text, a list, a table, etc. A format also has various properties (some specific to particular format types), as described by the Property enum. Every property has a corresponding Property.

The format type is given by :sip:ref:`~PyQt6.QtGui.QTextFormat.type`, and the format can be tested with :sip:ref:`~PyQt6.QtGui.QTextFormat.isCharFormat`, :sip:ref:`~PyQt6.QtGui.QTextFormat.isBlockFormat`, :sip:ref:`~PyQt6.QtGui.QTextFormat.isListFormat`, :sip:ref:`~PyQt6.QtGui.QTextFormat.isTableFormat`, :sip:ref:`~PyQt6.QtGui.QTextFormat.isFrameFormat`, and :sip:ref:`~PyQt6.QtGui.QTextFormat.isImageFormat`. If the type is determined, it can be retrieved with :sip:ref:`~PyQt6.QtGui.QTextFormat.toCharFormat`, :sip:ref:`~PyQt6.QtGui.QTextFormat.toBlockFormat`, :sip:ref:`~PyQt6.QtGui.QTextFormat.toListFormat`, :sip:ref:`~PyQt6.QtGui.QTextFormat.toTableFormat`, :sip:ref:`~PyQt6.QtGui.QTextFormat.toFrameFormat`, and :sip:ref:`~PyQt6.QtGui.QTextFormat.toImageFormat`.

A format's properties can be set with the :sip:ref:`~PyQt6.QtGui.QTextFormat.setProperty` functions, and retrieved with :sip:ref:`~PyQt6.QtGui.QTextFormat.boolProperty`, :sip:ref:`~PyQt6.QtGui.QTextFormat.intProperty`, :sip:ref:`~PyQt6.QtGui.QTextFormat.doubleProperty`, and :sip:ref:`~PyQt6.QtGui.QTextFormat.stringProperty` as appropriate. All the property IDs used in the format can be retrieved with allPropertyIds(). One format can be merged into another using :sip:ref:`~PyQt6.QtGui.QTextFormat.merge`.

A format's object index can be set with :sip:ref:`~PyQt6.QtGui.QTextFormat.setObjectIndex`, and retrieved with :sip:ref:`~PyQt6.QtGui.QTextFormat.objectIndex`. These methods can be used to associate the format with a :sip:ref:`~PyQt6.QtGui.QTextObject`. It is used to represent lists, frames, and tables inside the document.

.. seealso:: `Rich Text Processing <https://doc.qt.io/qt-6/richtext.html>`_.
