.. sip:method-description::
    :status: todo
    :pysig: 3d87b361e46af7a9d071f2e3463bbc7a
    :realsig: (QWidget*)
    :digest: f66af556053988a96b4280a9cd9e0c35

Sets the widget in the corner between the two scroll bars to be *widget*.

You will probably also want to set at least one of the scroll bar modes to ``AlwaysOn``.

Passing ``nullptr`` shows no widget in the corner.

Any previous corner widget is hidden.

You may call setCornerWidget() with the same widget at different times.

All widgets set here will be deleted by the scroll area when it is destroyed unless you separately reparent the widget after setting some other corner widget (or ``nullptr``).

Any *newly* set widget should have no current parent.

By default, no corner widget is present.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.cornerWidget`, :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.horizontalScrollBarPolicy`, :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.horizontalScrollBarPolicy`.
