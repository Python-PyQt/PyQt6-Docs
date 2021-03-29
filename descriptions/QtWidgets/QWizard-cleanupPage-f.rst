.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: c8f8de65da5c220b519fa30092efefaa

This virtual function is called by :sip:ref:`~PyQt6.QtWidgets.QWizard` to clean up page *id* just before the user leaves it by clicking Back (unless the :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardOptions.IndependentPages` option is set).

The default implementation calls :sip:ref:`~PyQt6.QtWidgets.QWizardPage.cleanupPage` on page(\ *id*).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWizardPage.cleanupPage`, :sip:ref:`~PyQt6.QtWidgets.QWizard.initializePage`.
