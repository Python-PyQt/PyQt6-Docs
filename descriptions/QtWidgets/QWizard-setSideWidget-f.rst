.. sip:method-description::
    :status: todo
    :pysig: 3d87b361e46af7a9d071f2e3463bbc7a
    :realsig: (QWidget*)
    :digest: 79cd3bdae3344ce7ceecdc000ec11322

Sets the given *widget* to be shown on the left side of the wizard. For styles which use the :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardPixmap.WatermarkPixmap` (\ :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardStyle.ClassicStyle` and :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardStyle.ModernStyle`) the side widget is displayed on top of the watermark, for other styles or when the watermark is not provided the side widget is displayed on the left side of the wizard.

Passing ``nullptr`` shows no side widget.

When the *widget* is not ``nullptr`` the wizard reparents it.

Any previous side widget is hidden.

You may call  with the same widget at different times.

All widgets set here will be deleted by the wizard when it is destroyed unless you separately reparent the widget after setting some other side widget (or ``nullptr``).

By default, no side widget is present.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWizard.sideWidget`.
