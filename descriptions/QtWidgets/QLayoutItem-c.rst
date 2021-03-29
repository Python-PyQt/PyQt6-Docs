.. sip:class-description::
    :status: todo
    :brief: Abstract item that a QLayout manipulates
    :digest: 142a8c6776dff63bc94dca8c49310d69

The :sip:ref:`~PyQt6.QtWidgets.QLayoutItem` class provides an abstract item that a :sip:ref:`~PyQt6.QtWidgets.QLayout` manipulates.

This is used by custom layouts.

Pure virtual functions are provided to return information about the layout, including, :sip:ref:`~PyQt6.QtWidgets.QLayoutItem.sizeHint`, :sip:ref:`~PyQt6.QtWidgets.QLayoutItem.minimumSize`, :sip:ref:`~PyQt6.QtWidgets.QLayoutItem.maximumSize` and expanding().

The layout's geometry can be set and retrieved with :sip:ref:`~PyQt6.QtWidgets.QLayoutItem.setGeometry` and :sip:ref:`~PyQt6.QtWidgets.QLayoutItem.geometry`, and its alignment with :sip:ref:`~PyQt6.QtWidgets.QLayoutItem.setAlignment` and :sip:ref:`~PyQt6.QtWidgets.QLayoutItem.alignment`.

:sip:ref:`~PyQt6.QtWidgets.QLayoutItem.isEmpty` returns whether the layout item is empty. If the concrete item is a `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_, it can be retrieved using :sip:ref:`~PyQt6.QtWidgets.QLayoutItem.widget`. Similarly for :sip:ref:`~PyQt6.QtWidgets.QLayoutItem.layout` and :sip:ref:`~PyQt6.QtWidgets.QLayoutItem.spacerItem`.

Some layouts have width and height interdependencies. These can be expressed using :sip:ref:`~PyQt6.QtWidgets.QLayoutItem.hasHeightForWidth`, :sip:ref:`~PyQt6.QtWidgets.QLayoutItem.heightForWidth`, and :sip:ref:`~PyQt6.QtWidgets.QLayoutItem.minimumHeightForWidth`. For more explanation see the *Qt Quarterly* article `Trading Height for Width <http://doc.qt.io/archives/qq/qq04-height-for-width.html>`_.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QLayout`.
