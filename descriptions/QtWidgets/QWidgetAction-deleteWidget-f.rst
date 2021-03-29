.. sip:method-description::
    :status: todo
    :pysig: 3d87b361e46af7a9d071f2e3463bbc7a
    :realsig: (QWidget*)
    :digest: 6f32d7603353ea22c9170333ab3a2d79

This function is called whenever the action is removed from a container widget that displays the action using a custom *widget* previously created using :sip:ref:`~PyQt6.QtWidgets.QWidgetAction.createWidget`. The default implementation hides the *widget* and schedules it for deletion using :sip:ref:`~PyQt6.QtCore.QObject.deleteLater`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidgetAction.createWidget`.
