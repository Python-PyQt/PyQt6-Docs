.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: ff9be1d67bda3de3ae9a36be62bf2e38

This virtual function is called by :sip:ref:`~PyQt6.QtWidgets.QWizard` to prepare page *id* just before it is shown either as a result of :sip:ref:`~PyQt6.QtWidgets.QWizard.restart` being called, or as a result of the user clicking Next. (However, if the :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardOptions.IndependentPages` option is set, this function is only called the first time the page is shown.)

By reimplementing this function, you can ensure that the page's fields are properly initialized based on fields from previous pages.

The default implementation calls :sip:ref:`~PyQt6.QtWidgets.QWizardPage.initializePage` on page(\ *id*).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWizardPage.initializePage`, :sip:ref:`~PyQt6.QtWidgets.QWizard.cleanupPage`.
