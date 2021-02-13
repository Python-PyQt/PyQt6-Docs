.. sip:method-description::
    :status: todo
    :pysig: 3d87b361e46af7a9d071f2e3463bbc7a
    :realsig: (QWidget*)
    :digest: fff9d5ecca56b8cdd409b0b39b3d1eb9

Sets the viewport to be the given *widget*. The :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea` will take ownership of the given *widget*.

If *widget* is ``nullptr``, :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea` will assign a new `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ instance for the viewport.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.viewport`.
