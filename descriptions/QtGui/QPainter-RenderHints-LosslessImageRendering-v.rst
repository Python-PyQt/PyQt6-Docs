.. sip:enum-member-description::
    :status: todo
    :value: 0x40
    :realname: QPainter::RenderHint::LosslessImageRendering
    :digest: bbb8748d475992df66f749c7fe16eec1

Use a lossless image rendering, whenever possible. Currently, this hint is only used when :sip:ref:`~PyQt6.QtGui.QPainter` is employed to output a PDF file through :sip:ref:`~PyQt6.QtPrintSupport.QPrinter` or :sip:ref:`~PyQt6.QtGui.QPdfWriter`, where :sip:ref:`~PyQt6.QtGui.QPainter.drawImage`/\ :sip:ref:`~PyQt6.QtGui.QPainter.drawPixmap` calls will encode images using a lossless compression algorithm instead of lossy JPEG compression. This value was added in Qt 5.13.
