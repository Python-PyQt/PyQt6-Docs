.. sip:method-description::
    :status: todo
    :pysig: 2093f3020e91c79c5608f54478b6caf5
    :realsig: () const
    :digest: e936b447d3cdb5989e58ada83c3f59bf

Returns a list of child objects. The QObjectList class is defined in the ``<QObject>`` header file as the following:

The first child added is the first object in the list and the last child added is the last object in the list, i.e. new children are appended at the end.

Note that the list order changes when :sip:ref:`~PyQt6.QtWidgets.QWidget` children are :sip:ref:`~PyQt6.QtWidgets.QWidget.raise_` or :sip:ref:`~PyQt6.QtWidgets.QWidget.lower`. A widget that is raised becomes the last object in the list, and a widget that is lowered becomes the first object in the list.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.findChild`, :sip:ref:`~PyQt6.QtCore.QObject.findChildren`, :sip:ref:`~PyQt6.QtCore.QObject.parent`, :sip:ref:`~PyQt6.QtCore.QObject.setParent`.
