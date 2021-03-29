.. sip:method-description::
    :status: todo
    :pysig: 3d87b361e46af7a9d071f2e3463bbc7a
    :realsig: (QWidget*)
    :digest: 73cdb2c27a29ce23a891c7c9559327ba

Sets the scroll area's *widget*.

The *widget* becomes a child of the scroll area, and will be destroyed when the scroll area is deleted or when a new widget is set.

The widget's :sip:ref:`~PyQt6.QtWidgets.QWidget.setAutoFillBackground` property will be set to ``true``.

If the scroll area is visible when the *widget* is added, you must :sip:ref:`~PyQt6.QtWidgets.QWidget.show` it explicitly.

Note that You must add the layout of *widget* before you call this function; if you add it later, the *widget* will not be visible - regardless of when you :sip:ref:`~PyQt6.QtWidgets.QWidget.show` the scroll area. In this case, you can also not :sip:ref:`~PyQt6.QtWidgets.QWidget.show` the *widget* later.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QScrollArea.widget`.
