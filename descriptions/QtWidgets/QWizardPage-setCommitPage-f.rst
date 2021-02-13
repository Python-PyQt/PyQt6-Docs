.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 125bbcc1e864fcf52b8933521e2d876b

Sets this page to be a commit page if *commitPage* is true; otherwise, sets it to be a normal page.

A commit page is a page that represents an action which cannot be undone by clicking Back or Cancel.

A Commit button replaces the Next button on a commit page. Clicking this button simply calls :sip:ref:`~PyQt6.QtWidgets.QWizard.next` just like clicking Next does.

A page entered directly from a commit page has its Back button disabled.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWizardPage.isCommitPage`.
