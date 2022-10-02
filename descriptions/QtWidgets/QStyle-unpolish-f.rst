.. sip:method-description::
    :status: todo
    :pysig: 3d87b361e46af7a9d071f2e3463bbc7a
    :realsig: (QWidget*)
    :digest: 143a2bc8c334487a29ae6f7afac9e23d

Uninitialize the given *widget*'s appearance.

This function is the counterpart to :sip:ref:`~PyQt6.QtWidgets.QStyle.polish`. It is called for every polished widget whenever the style is dynamically changed; the former style has to unpolish its settings before the new style can polish them again.

Note that unpolish() will only be called if the widget is destroyed. This can cause problems in some cases, e.g, if you remove a widget from the UI, cache it, and then reinsert it after the style has changed; some of Qt's classes cache their widgets.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStyle.polish`.
