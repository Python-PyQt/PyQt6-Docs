.. sip:signal-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 840e84e3201e5dfcf00eea9e1affb647

This signal is emitted when the user clicks a custom button. *which* can be :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardButton.CustomButton1`, :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardButton.CustomButton2`, or :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardButton.CustomButton3`.

By default, no custom button is shown. Call :sip:ref:`~PyQt6.QtWidgets.QWizard.setOption` with :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardOptions.HaveCustomButton1`, :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardOptions.HaveCustomButton2`, or :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardOptions.HaveCustomButton3` to have one, and use :sip:ref:`~PyQt6.QtWidgets.QWizard.setButtonText` or :sip:ref:`~PyQt6.QtWidgets.QWizard.setButton` to configure it.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWizard.helpRequested`.
