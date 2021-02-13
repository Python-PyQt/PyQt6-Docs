.. sip:method-description::
    :status: todo
    :pysig: 62178eeb74e9074205b28c6759d2800a
    :realsig: () const
    :digest: e936b447d3cdb5989e58ada83c3f59bf

Returns a list of child objects. The QObjectList class is defined in the ``<QObject>`` header file as the following:

The first child added is the first object in the list and the last child added is the last object in the list, i.e. new children are appended at the end.

Note that the list order changes when `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ children are :sip:ref:`~PyQt6.QtWidgets.QWidget.raise_` or :sip:ref:`~PyQt6.QtWidgets.QWidget.lower`. A widget that is raised becomes the last object in the list, and a widget that is lowered becomes the first object in the list.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.findChild`, :sip:ref:`~PyQt6.QtCore.QObject.findChildren`, :sip:ref:`~PyQt6.QtCore.QObject.parent`, :sip:ref:`~PyQt6.QtCore.QObject.setParent`.
