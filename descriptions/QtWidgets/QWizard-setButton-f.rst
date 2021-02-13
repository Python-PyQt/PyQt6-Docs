.. sip:method-description::
    :status: todo
    :pysig: 39cc0046c0239b415ece0a9b06038777
    :realsig: (QWizard::WizardButton,QAbstractButton*)
    :digest: 0929ddb3b9e762521f66c6e102c7fac2

Sets the button corresponding to role *which* to *button*.

To add extra buttons to the wizard (e.g., a Print button), one way is to call  with :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardButton.CustomButton1` to :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardButton.CustomButton3`, and make the buttons visible using the :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardOptions.HaveCustomButton1` to :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardOptions.HaveCustomButton3` options.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWizard.button`, :sip:ref:`~PyQt6.QtWidgets.QWizard.setButtonText`, :sip:ref:`~PyQt6.QtWidgets.QWizard.setButtonLayout`, `options <https://doc.qt.io/qt-6/qt-wrap-ui.html#options>`_.
