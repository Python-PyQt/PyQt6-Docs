.. sip:class-description::
    :status: todo
    :brief: Widgets for editing item data in views and delegates
    :digest: d7ad572c3e522419d703c4a5a1956d98

The :sip:ref:`~PyQt6.QtWidgets.QItemEditorFactory` class provides widgets for editing item data in views and delegates.

When editing data in an item view, editors are created and displayed by a delegate. :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate`, which is the delegate by default installed on Qt's item views, uses a :sip:ref:`~PyQt6.QtWidgets.QItemEditorFactory` to create editors for it. A default unique instance provided by :sip:ref:`~PyQt6.QtWidgets.QItemEditorFactory` is used by all item delegates. If you set a new default factory with :sip:ref:`~PyQt6.QtWidgets.QItemEditorFactory.setDefaultFactory`, the new factory will be used by existing and new delegates.

A factory keeps a collection of :sip:ref:`~PyQt6.QtWidgets.QItemEditorCreatorBase` instances, which are specialized editors that produce editors for one particular :sip:ref:`~PyQt6.QtCore.QVariant` data type (All Qt models store their data in :sip:ref:`~PyQt6.QtCore.QVariant`\ s).

.. _qitemeditorfactory-standard-editing-widgets:

Standard Editing Widgets
------------------------

The standard factory implementation provides editors for a variety of data types. These are created whenever a delegate needs to provide an editor for data supplied by a model. The following table shows the relationship between types and the standard editors provided.

+------------------------------------+--------------------------------------------+
| Type                               | Editor Widget                              |
+====================================+============================================+
| bool                               | :sip:ref:`~PyQt6.QtWidgets.QComboBox`      |
+------------------------------------+--------------------------------------------+
| double                             | :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox` |
+------------------------------------+--------------------------------------------+
| int                                | :sip:ref:`~PyQt6.QtWidgets.QSpinBox`       |
+------------------------------------+--------------------------------------------+
| unsigned int                       |                                            |
+------------------------------------+--------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.QDate`     | :sip:ref:`~PyQt6.QtWidgets.QDateEdit`      |
+------------------------------------+--------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.QDateTime` | :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit`  |
+------------------------------------+--------------------------------------------+
| :sip:ref:`~PyQt6.QtGui.QPixmap`    | :sip:ref:`~PyQt6.QtWidgets.QLabel`         |
+------------------------------------+--------------------------------------------+
| QString                            | :sip:ref:`~PyQt6.QtWidgets.QLineEdit`      |
+------------------------------------+--------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.QTime`     | :sip:ref:`~PyQt6.QtWidgets.QTimeEdit`      |
+------------------------------------+--------------------------------------------+

Additional editors can be registered with the :sip:ref:`~PyQt6.QtWidgets.QItemEditorFactory.registerEditor` function.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate`, `Model/View Programming <https://doc.qt.io/qt-6/model-view-programming.html>`_.
