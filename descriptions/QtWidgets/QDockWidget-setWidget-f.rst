.. sip:method-description::
    :status: todo
    :pysig: 3d87b361e46af7a9d071f2e3463bbc7a
    :realsig: (QWidget*)
    :digest: 227c7ef6c12cb46e7c85f04483f79ffc

Sets the widget for the dock widget to *widget*.

If the dock widget is visible when *widget* is added, you must :sip:ref:`~PyQt6.QtWidgets.QWidget.show` it explicitly.

Note that you must add the layout of the *widget* before you call this function; if not, the *widget* will not be visible.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QDockWidget.widget`.
