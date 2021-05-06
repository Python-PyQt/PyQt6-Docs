:orphan:

.. sip:class:: PyQt6.QtPrintSupport.QAbstractPrintDialog
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QDialog`
    :description: QtPrintSupport/QAbstractPrintDialog-c.rst

    .. sip:enum:: PyQt6.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption
        :description: QtPrintSupport/QAbstractPrintDialog-PrintDialogOption-e.rst

        .. sip:enum-member:: PyQt6.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption.PrintCollateCopies
            :description: QtPrintSupport/QAbstractPrintDialog-PrintDialogOption-PrintCollateCopies-v.rst

        .. sip:enum-member:: PyQt6.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption.PrintCurrentPage
            :description: QtPrintSupport/QAbstractPrintDialog-PrintDialogOption-PrintCurrentPage-v.rst

        .. sip:enum-member:: PyQt6.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption.PrintPageRange
            :description: QtPrintSupport/QAbstractPrintDialog-PrintDialogOption-PrintPageRange-v.rst

        .. sip:enum-member:: PyQt6.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption.PrintSelection
            :description: QtPrintSupport/QAbstractPrintDialog-PrintDialogOption-PrintSelection-v.rst

        .. sip:enum-member:: PyQt6.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption.PrintShowPageSize
            :description: QtPrintSupport/QAbstractPrintDialog-PrintDialogOption-PrintShowPageSize-v.rst

        .. sip:enum-member:: PyQt6.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption.PrintToFile
            :description: QtPrintSupport/QAbstractPrintDialog-PrintDialogOption-PrintToFile-v.rst

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
