.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 3cd0fa2e8bf6136889b0799cbd0bfbd0

Forces active focus on the item.

This method sets focus on the item and ensures that all ancestor `FocusScope <https://doc.qt.io/qt-6/qml-qtquick-focusscope.html>`_ objects in the object hierarchy are also given focus.

The reason for the focus change will be :sip:ref:`~PyQt6.QtCore.Qt.FocusReason.OtherFocusReason`. Use the overloaded method to specify the focus reason to enable better handling of the focus change.

.. seealso:: activeFocus.
