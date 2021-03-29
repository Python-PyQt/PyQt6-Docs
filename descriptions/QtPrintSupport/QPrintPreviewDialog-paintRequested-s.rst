.. sip:signal-description::
    :status: todo
    :pysig: faee251a718408ee33735c75f47a3158
    :realsig: (QPrinter*)
    :digest: d613b3466816901ced96ecd1db6ec2af

This signal is emitted when the :sip:ref:`~PyQt6.QtPrintSupport.QPrintPreviewDialog` needs to generate a set of preview pages.

The *printer* instance supplied is the paint device onto which you should paint the contents of each page, using the :sip:ref:`~PyQt6.QtPrintSupport.QPrinter` instance in the same way as you would when printing directly.
