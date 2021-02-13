.. sip:method-description::
    :status: todo
    :pysig: af87d49684708b45a09f70becee5d037
    :realsig: (QWizard::WizardPixmap,const QPixmap&)
    :digest: 157acc0b980e2a7a13fb465ee3cf367b

Sets the pixmap for role *which* to *pixmap*.

The pixmaps are used by :sip:ref:`~PyQt6.QtWidgets.QWizard` when displaying a page. Which pixmaps are actually used depend on the wizard style.

Pixmaps can also be set for the entire wizard using :sip:ref:`~PyQt6.QtWidgets.QWizard.setPixmap`, in which case they apply for all pages that don't specify a pixmap.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWizardPage.pixmap`, :sip:ref:`~PyQt6.QtWidgets.QWizard.setPixmap`, Elements of a Wizard Page.
