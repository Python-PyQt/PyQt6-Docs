.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 2452f8b275d6085a4730b0d758e8db50

This virtual function is called by :sip:ref:`~PyQt6.QtWidgets.QWizard` to find out which page to show when the user clicks the Next button.

The return value is the ID of the next page, or -1 if no page follows.

The default implementation calls :sip:ref:`~PyQt6.QtWidgets.QWizardPage.nextId` on the :sip:ref:`~PyQt6.QtWidgets.QWizard.currentPage`.

By reimplementing this function, you can specify a dynamic page order.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWizardPage.nextId`, :sip:ref:`~PyQt6.QtWidgets.QWizard.currentPage`.
