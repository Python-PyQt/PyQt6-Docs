.. sip:class-description::
    :status: todo
    :brief: Layout attribute describing horizontal and vertical resizing policy
    :digest: 4b308e44ffd67690e9fb721e83c85c7d

The :sip:ref:`~PyQt6.QtWidgets.QSizePolicy` class is a layout attribute describing horizontal and vertical resizing policy.

The size policy of a widget is an expression of its willingness to be resized in various ways, and affects how the widget is treated by the `layout engine <https://doc.qt.io/qt-6/layout.html>`_. Each widget returns a :sip:ref:`~PyQt6.QtWidgets.QSizePolicy` that describes the horizontal and vertical resizing policy it prefers when being laid out. You can change this for a specific widget by changing its :sip:ref:`~PyQt6.QtWidgets.QWidget.sizePolicy` property.

:sip:ref:`~PyQt6.QtWidgets.QSizePolicy` contains two independent :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.Policy` values and two stretch factors; one describes the widgets's horizontal size policy, and the other describes its vertical size policy. It also contains a flag to indicate whether the height and width of its preferred size are related.

The horizontal and vertical policies can be set in the constructor, and altered using the :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.setHorizontalPolicy` and :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.setVerticalPolicy` functions. The stretch factors can be set using the :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.setHorizontalStretch` and :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.setVerticalStretch` functions. The flag indicating whether the widget's :sip:ref:`~PyQt6.QtWidgets.QWidget.sizeHint` is width-dependent (such as a menu bar or a word-wrapping label) can be set using the :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.setHeightForWidth` function.

The current size policies and stretch factors be retrieved using the :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.horizontalPolicy`, :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.verticalPolicy`, :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.horizontalStretch` and :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.verticalStretch` functions. Alternatively, use the :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.transpose` function to swap the horizontal and vertical policies and stretches. The :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.hasHeightForWidth` function returns the current status of the flag indicating the size hint dependencies.

Use the :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.expandingDirections` function to determine whether the associated widget can make use of more space than its :sip:ref:`~PyQt6.QtWidgets.QWidget.sizeHint` function indicates, as well as find out in which directions it can expand.

Finally, the :sip:ref:`~PyQt6.QtWidgets.QSizePolicy` class provides operators comparing this size policy to a given policy, as well as a `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ operator storing this :sip:ref:`~PyQt6.QtWidgets.QSizePolicy` as a `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ object.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSize`, :sip:ref:`~PyQt6.QtWidgets.QWidget.sizeHint`, :sip:ref:`~PyQt6.QtWidgets.QWidget.sizePolicy`, :sip:ref:`~PyQt6.QtWidgets.QLayoutItem.sizeHint`.
