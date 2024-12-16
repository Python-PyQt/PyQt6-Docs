.. sip:class-description::
    :status: todo
    :brief: Abstract base class that must be subclassed when implementing new item editor creators
    :digest: 5df43369a414d091bcd2e338160fc4ff

The :sip:ref:`~PyQt6.QtWidgets.QItemEditorCreatorBase` class provides an abstract base class that must be subclassed when implementing new item editor creators.

:sip:ref:`~PyQt6.QtWidgets.QItemEditorCreatorBase` objects are specialized widget factories that provide editor widgets for one particular :sip:ref:`~PyQt6.QtCore.QVariant` data type. They are used by :sip:ref:`~PyQt6.QtWidgets.QItemEditorFactory` to create editors for :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate`\ s. Creator bases must be registered with :sip:ref:`~PyQt6.QtWidgets.QItemEditorFactory.registerEditor`.

An editor should provide a user property for the data it edits. QItemDelagates can then access the property using Qt's `meta-object system <https://doc.qt.io/qt-6/metaobjects.html>`_ to set and retrieve the editing data. A property is set as the user property with the USER keyword:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_itemviews_qitemeditorfactory.py
    :lines: 54-54

If the editor does not provide a user property, it must return the name of the property from :sip:ref:`~PyQt6.QtWidgets.QItemEditorCreatorBase.valuePropertyName`; delegates will then use the name to access the property. If a user property exists, item delegates will not call :sip:ref:`~PyQt6.QtWidgets.QItemEditorCreatorBase.valuePropertyName`.

QStandardItemEditorCreator is a convenience template class that can be used to register widgets without the need to subclass :sip:ref:`~PyQt6.QtWidgets.QItemEditorCreatorBase`.

.. seealso:: QStandardItemEditorCreator, :sip:ref:`~PyQt6.QtWidgets.QItemEditorFactory`, `Model/View Programming <https://doc.qt.io/qt-6/model-view-programming.html>`_.
