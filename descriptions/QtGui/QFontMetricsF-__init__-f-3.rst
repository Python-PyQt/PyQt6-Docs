.. sip:method-description::
    :status: todo
    :pysig: d2c07d5ec2cba0baedb64b17ce995c76
    :realsig: (const QFont&,const QPaintDevice*)
    :digest: d5b7220038b4827e9d6069620219a09d

Constructs a font metrics object for *font* and *paintdevice*.

The font metrics will be compatible with the paintdevice passed. If the *paintdevice* is ``nullptr``, the metrics will be screen-compatible, ie. the metrics you get if you use the font for drawing text on a widgets or :sip:ref:`~PyQt6.QtGui.QPixmap`, not on a :sip:ref:`~PyQt6.QtGui.QPicture` or QPrinter.

The font metrics object holds the information for the font that is passed in the constructor at the time it is created, and is not updated if the font's attributes are changed later.
