.. sip:method-description::
    :status: todo
    :pysig: 3d87b361e46af7a9d071f2e3463bbc7a
    :realsig: () const
    :digest: 1d47914610635253fb9a49624d792757

If this item manages a `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_, returns that widget. Otherwise, ``nullptr`` is returned.

**Note:** While the functions :sip:ref:`~PyQt6.QtWidgets.QLayoutItem.layout` and :sip:ref:`~PyQt6.QtWidgets.QLayoutItem.spacerItem` perform casts, this function returns another object: :sip:ref:`~PyQt6.QtWidgets.QLayout` and :sip:ref:`~PyQt6.QtWidgets.QSpacerItem` inherit :sip:ref:`~PyQt6.QtWidgets.QLayoutItem`, while `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ does not.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QLayoutItem.layout`, :sip:ref:`~PyQt6.QtWidgets.QLayoutItem.spacerItem`.
