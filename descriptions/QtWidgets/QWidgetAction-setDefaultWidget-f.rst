.. sip:method-description::
    :status: todo
    :pysig: 3d87b361e46af7a9d071f2e3463bbc7a
    :realsig: (QWidget*)
    :digest: fdb2d4acf0f5ba0d2d5eb126ec3cfb81

Sets *widget* to be the default widget. The ownership is transferred to :sip:ref:`~PyQt6.QtWidgets.QWidgetAction`. Unless :sip:ref:`~PyQt6.QtWidgets.QWidgetAction.createWidget` is reimplemented by a subclass to return a new widget the default widget is used when a container widget requests a widget through :sip:ref:`~PyQt6.QtWidgets.QWidgetAction.requestWidget`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidgetAction.defaultWidget`.
