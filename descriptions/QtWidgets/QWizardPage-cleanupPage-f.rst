.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 50ddca5b9ff9e8d9679a50245895c195

This virtual function is called by :sip:ref:`~PyQt6.QtWidgets.QWizard.cleanupPage` when the user leaves the page by clicking Back (unless the :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardOptions.IndependentPages` option is set).

The default implementation resets the page's fields to their original values (the values they had before :sip:ref:`~PyQt6.QtWidgets.QWizardPage.initializePage` was called).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWizard.cleanupPage`, :sip:ref:`~PyQt6.QtWidgets.QWizardPage.initializePage`, :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardOptions.IndependentPages`.
