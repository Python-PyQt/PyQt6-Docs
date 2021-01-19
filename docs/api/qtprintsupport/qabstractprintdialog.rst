:orphan:

.. sip:class:: PyQt6.QtPrintSupport.QAbstractPrintDialog
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QDialog`
    :description: QtPrintSupport/QAbstractPrintDialog-c.rst

    .. sip:enum:: PyQt6.QtPrintSupport.QAbstractPrintDialog.PrintDialogOptions
        :description: QtPrintSupport/QAbstractPrintDialog-PrintDialogOptions-e.rst

        .. sip:enum-member:: PyQt6.QtPrintSupport.QAbstractPrintDialog.PrintDialogOptions.PrintCollateCopies
            :description: QtPrintSupport/QAbstractPrintDialog-PrintDialogOptions-PrintCollateCopies-v.rst

        .. sip:enum-member:: PyQt6.QtPrintSupport.QAbstractPrintDialog.PrintDialogOptions.PrintCurrentPage
            :description: QtPrintSupport/QAbstractPrintDialog-PrintDialogOptions-PrintCurrentPage-v.rst

        .. sip:enum-member:: PyQt6.QtPrintSupport.QAbstractPrintDialog.PrintDialogOptions.PrintPageRange
            :description: QtPrintSupport/QAbstractPrintDialog-PrintDialogOptions-PrintPageRange-v.rst

        .. sip:enum-member:: PyQt6.QtPrintSupport.QAbstractPrintDialog.PrintDialogOptions.PrintSelection
            :description: QtPrintSupport/QAbstractPrintDialog-PrintDialogOptions-PrintSelection-v.rst

        .. sip:enum-member:: PyQt6.QtPrintSupport.QAbstractPrintDialog.PrintDialogOptions.PrintShowPageSize
            :description: QtPrintSupport/QAbstractPrintDialog-PrintDialogOptions-PrintShowPageSize-v.rst

        .. sip:enum-member:: PyQt6.QtPrintSupport.QAbstractPrintDialog.PrintDialogOptions.PrintToFile
            :description: QtPrintSupport/QAbstractPrintDialog-PrintDialogOptions-PrintToFile-v.rst

    .. sip:enum:: PyQt6.QtPrintSupport.QAbstractPrintDialog.PrintRange
        :description: QtPrintSupport/QAbstractPrintDialog-PrintRange-e.rst

        .. sip:enum-member:: PyQt6.QtPrintSupport.QAbstractPrintDialog.PrintRange.AllPages
            :description: QtPrintSupport/QAbstractPrintDialog-PrintRange-AllPages-v.rst

        .. sip:enum-member:: PyQt6.QtPrintSupport.QAbstractPrintDialog.PrintRange.CurrentPage
            :description: QtPrintSupport/QAbstractPrintDialog-PrintRange-CurrentPage-v.rst

        .. sip:enum-member:: PyQt6.QtPrintSupport.QAbstractPrintDialog.PrintRange.PageRange
            :description: QtPrintSupport/QAbstractPrintDialog-PrintRange-PageRange-v.rst

        .. sip:enum-member:: PyQt6.QtPrintSupport.QAbstractPrintDialog.PrintRange.Selection
            :description: QtPrintSupport/QAbstractPrintDialog-PrintRange-Selection-v.rst

    .. sip:method:: PyQt6.QtPrintSupport.QAbstractPrintDialog.__init__
        :args:
            :sip:ref:`~PyQt6.QtPrintSupport.QPrinter`
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtPrintSupport/QAbstractPrintDialog-__init__-f.rst

    .. sip:method:: PyQt6.QtPrintSupport.QAbstractPrintDialog.fromPage
        :returns:
            int
        :description: QtPrintSupport/QAbstractPrintDialog-fromPage-f.rst

    .. sip:method:: PyQt6.QtPrintSupport.QAbstractPrintDialog.maxPage
        :returns:
            int
        :description: QtPrintSupport/QAbstractPrintDialog-maxPage-f.rst

    .. sip:method:: PyQt6.QtPrintSupport.QAbstractPrintDialog.minPage
        :returns:
            int
        :description: QtPrintSupport/QAbstractPrintDialog-minPage-f.rst

    .. sip:method:: PyQt6.QtPrintSupport.QAbstractPrintDialog.printer
        :returns:
            :sip:ref:`~PyQt6.QtPrintSupport.QPrinter`
        :description: QtPrintSupport/QAbstractPrintDialog-printer-f.rst

    .. sip:method:: PyQt6.QtPrintSupport.QAbstractPrintDialog.printRange
        :returns:
            :sip:ref:`~PyQt6.QtPrintSupport.QAbstractPrintDialog.PrintRange`
        :description: QtPrintSupport/QAbstractPrintDialog-printRange-f.rst

    .. sip:method:: PyQt6.QtPrintSupport.QAbstractPrintDialog.setFromTo
        :args:
            int
            int
        :description: QtPrintSupport/QAbstractPrintDialog-setFromTo-f.rst

    .. sip:method:: PyQt6.QtPrintSupport.QAbstractPrintDialog.setMinMax
        :args:
            int
            int
        :description: QtPrintSupport/QAbstractPrintDialog-setMinMax-f.rst

    .. sip:method:: PyQt6.QtPrintSupport.QAbstractPrintDialog.setOptionTabs
        :args:
            Iterable[:sip:ref:`~PyQt6.QtWidgets.QWidget`]
        :description: QtPrintSupport/QAbstractPrintDialog-setOptionTabs-f.rst

    .. sip:method:: PyQt6.QtPrintSupport.QAbstractPrintDialog.setPrintRange
        :args:
            :sip:ref:`~PyQt6.QtPrintSupport.QAbstractPrintDialog.PrintRange`
        :description: QtPrintSupport/QAbstractPrintDialog-setPrintRange-f.rst

    .. sip:method:: PyQt6.QtPrintSupport.QAbstractPrintDialog.toPage
        :returns:
            int
        :description: QtPrintSupport/QAbstractPrintDialog-toPage-f.rst
