.. sip:enum-description::
    :status: todo
    :digest: 64ecb23dcdd085ac8a0da68a4c6a405a

This enum type lists the available page sizes as defined in the Postscript PPD standard. These values are duplicated in :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice` and :sip:ref:`~PyQt6.QtPrintSupport.QPrinter`.

The defined sizes are:

Due to historic reasons QPageSize::Executive is not the same as the standard Postscript and Windows Executive size, use QPageSize::ExecutiveStandard instead.

The Postscript standard size QPageSize::Folio is different to the Windows DMPAPER_FOLIO size, use the Postscript standard size QPageSize::FanFoldGermanLegal if needed.
