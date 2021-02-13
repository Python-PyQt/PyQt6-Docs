.. sip:class-description::
    :status: todo
    :brief: The base class for wizard pages
    :digest: 36531f19522aae742a0d9fea6745e102

The :sip:ref:`~PyQt6.QtWidgets.QWizardPage` class is the base class for wizard pages.

:sip:ref:`~PyQt6.QtWidgets.QWizard` represents a wizard. Each page is a :sip:ref:`~PyQt6.QtWidgets.QWizardPage`. When you create your own wizards, you can use :sip:ref:`~PyQt6.QtWidgets.QWizardPage` directly, or you can subclass it for more control.

A page has the following attributes, which are rendered by :sip:ref:`~PyQt6.QtWidgets.QWizard`: a :sip:ref:`~PyQt6.QtWidgets.QWizardPage.title`, a :sip:ref:`~PyQt6.QtWidgets.QWizardPage.subTitle`, and a :sip:ref:`~PyQt6.QtWidgets.QWizardPage.setPixmap`. See Elements of a Wizard Page for details. Once a page is added to the wizard (using :sip:ref:`~PyQt6.QtWidgets.QWizard.addPage` or :sip:ref:`~PyQt6.QtWidgets.QWizard.setPage`), :sip:ref:`~PyQt6.QtWidgets.QWizardPage.wizard` returns a pointer to the associated :sip:ref:`~PyQt6.QtWidgets.QWizard` object.

Page provides five virtual functions that can be reimplemented to provide custom behavior:

* :sip:ref:`~PyQt6.QtWidgets.QWizardPage.initializePage` is called to initialize the page's contents when the user clicks the wizard's Next button. If you want to derive the page's default from what the user entered on previous pages, this is the function to reimplement.

* :sip:ref:`~PyQt6.QtWidgets.QWizardPage.cleanupPage` is called to reset the page's contents when the user clicks the wizard's Back button.

* :sip:ref:`~PyQt6.QtWidgets.QWizardPage.validatePage` validates the page when the user clicks Next or Finish. It is often used to show an error message if the user has entered incomplete or invalid information.

* :sip:ref:`~PyQt6.QtWidgets.QWizardPage.nextId` returns the ID of the next page. It is useful when creating non-linear wizards, which allow different traversal paths based on the information provided by the user.

* :sip:ref:`~PyQt6.QtWidgets.QWizardPage.isComplete` is called to determine whether the Next and/or Finish button should be enabled or disabled. If you reimplement :sip:ref:`~PyQt6.QtWidgets.QWizardPage.isComplete`, also make sure that :sip:ref:`~PyQt6.QtWidgets.QWizardPage.completeChanged` is emitted whenever the complete state changes.

Normally, the Next button and the Finish button of a wizard are mutually exclusive. If :sip:ref:`~PyQt6.QtWidgets.QWizardPage.isFinalPage` returns ``true``, Finish is available; otherwise, Next is available. By default, :sip:ref:`~PyQt6.QtWidgets.QWizardPage.isFinalPage` is true only when :sip:ref:`~PyQt6.QtWidgets.QWizardPage.nextId` returns -1. If you want to show Next and Final simultaneously for a page (letting the user perform an "early finish"), call :sip:ref:`~PyQt6.QtWidgets.QWizardPage.setFinalPage`\ (true) on that page. For wizards that support early finishes, you might also want to set the :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardOptions.HaveNextButtonOnLastPage` and :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardOptions.HaveFinishButtonOnEarlyPages` options on the wizard.

In many wizards, the contents of a page may affect the default values of the fields of a later page. To make it easy to communicate between pages, :sip:ref:`~PyQt6.QtWidgets.QWizard` supports a "field" mechanism that allows you to register a field (e.g., a :sip:ref:`~PyQt6.QtWidgets.QLineEdit`) on a page and to access its value from any page. Fields are global to the entire wizard and make it easy for any single page to access information stored by another page, without having to put all the logic in :sip:ref:`~PyQt6.QtWidgets.QWizard` or having the pages know explicitly about each other. Fields are registered using :sip:ref:`~PyQt6.QtWidgets.QWizardPage.registerField` and can be accessed at any time using :sip:ref:`~PyQt6.QtWidgets.QWizardPage.field` and :sip:ref:`~PyQt6.QtWidgets.QWizardPage.setField`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWizard`, `Class Wizard Example <https://doc.qt.io/qt-6/qtwidgets-dialogs-classwizard-example.html>`_, `License Wizard Example <https://doc.qt.io/qt-6/qtwidgets-dialogs-licensewizard-example.html>`_.
