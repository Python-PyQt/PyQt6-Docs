.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 70ae245e2475a50054a082296685a599

Virtual function that is called whenever the user triggers a step. The *steps* parameter indicates how many steps were taken. For example, pressing ``Qt::Key_Down`` will trigger a call to ``stepBy(-1)``, whereas pressing ``Qt::Key_PageUp`` will trigger a call to ``stepBy(10)``.

If you subclass ``QAbstractSpinBox`` you must reimplement this function. Note that this function is called even if the resulting value will be outside the bounds of minimum and maximum. It's this function's job to handle these situations.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractSpinBox.stepUp`, :sip:ref:`~PyQt6.QtWidgets.QAbstractSpinBox.stepDown`, :sip:ref:`~PyQt6.QtWidgets.QAbstractSpinBox.keyPressEvent`.
