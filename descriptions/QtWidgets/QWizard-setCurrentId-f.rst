.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 6af7a66f6cbfaf0b4bc6207c1c2bda7b

Sets :sip:ref:`~PyQt6.QtWidgets.QWizard.currentId` to *id*, without visiting the pages between :sip:ref:`~PyQt6.QtWidgets.QWizard.currentId` and *id*.

Returns without page change, if

* wizard holds no pages

* current page is invalid

* given page equals :sip:ref:`~PyQt6.QtWidgets.QWizard.currentId`

* given page is out of range

Note: If pages have been forward skipped and *id* is 0, page visiting history will be deleted

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWizard.currentId`.
