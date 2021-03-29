.. sip:method-description::
    :status: todo
    :pysig: ea70e5f2843d7edcae70196827f92290
    :realsig: (QRubberBand::Shape,QWidget*)
    :digest: f0539bb39f8d05a870183422c7839b1b

Constructs a rubber band of shape *s*, with parent *p*.

By default a rectangular rubber band (\ *s* is ``Rectangle``) will use a mask, so that a small border of the rectangle is all that is visible. Some styles (e.g., native macOS) will change this and call :sip:ref:`~PyQt6.QtWidgets.QWidget.setWindowOpacity` to make a semi-transparent filled selection rectangle.
