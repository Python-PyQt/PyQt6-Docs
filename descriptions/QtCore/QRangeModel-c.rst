.. sip:class-description::
    :status: review
    :brief: Implements QAbstractItemModel for a Python range
    :digest: b9cae762a88c11b443057dcfd21771f5
:sip:ref:`~PyQt6.QtCore.QRangeModel` implements
:sip:ref:`~PyQt6.QtCore.QAbstractItemModel` for a Python range.

:sip:ref:`~PyQt6.QtCore.QRangeModel` can make the data in any sequentially
iterable Python object available to the `model/view framework
<https://doc.qt.io/qt-6/model-view-programming.html>`_ of Qt. This makes it
easy to display existing data structures in the Qt Widgets and Qt Quick item
views, and to allow the user of the application to manipulate the data using a
graphical user interface.

The range is implemented using a :sip:ref:`~PyQt6.QtCore.QPyAbstractRange`
sub-class to wrap a Python object which is passed to the
:sip:ref:`~PyQt6.QtCore.QRangeModel` constructor.  The sub-class (currently
either :sip:ref:`~PyQt6.QtCore.QPySequenceRange` or
:sip:ref:`~PyQt6.QtCore.QPyTableRange`) determines how the structure of the
Python object should be interpreted.

The following code will create a simple sequential model that would normally be
given to a :sip:ref:`~PyQt6.QtWidgets.QListView`::

    model = QRangeModel(QPySequenceRange(("Cat", "Dog", "Hamster")))

The following code will create a similar model but one that is editable::

    pets = ["Cat", "Dog", "Hamster"]
    model = QRangeModel(QPySequenceRange(pets, editable=True))

.. seealso:: `Model/View Programming <https://doc.qt.io/qt-6/model-view-programming.html>`_.

.. note::
    This API should be considered experimental.  It should be extended to
    support:

    - the insertion and removal of Python objects from the range
    - the addition of a ``QPyTreeRange`` to be used with
      :sip:ref:`~PyQt6.QtWidgets.QTreeView`.

