.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 71f15f2faea498fc5309ad66df17af6a

This virtual function is called by :sip:ref:`~PyQt6.QtWidgets.QWizard.initializePage` to prepare the page just before it is shown either as a result of :sip:ref:`~PyQt6.QtWidgets.QWizard.restart` being called, or as a result of the user clicking Next. (However, if the :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardOptions.IndependentPages` option is set, this function is only called the first time the page is shown.)

By reimplementing this function, you can ensure that the page's fields are properly initialized based on fields from previous pages. For example:

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-classwizard-classwizard.py
    :lines: 414-420

The default implementation does nothing.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWizard.initializePage`, :sip:ref:`~PyQt6.QtWidgets.QWizardPage.cleanupPage`, :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardOptions.IndependentPages`.
