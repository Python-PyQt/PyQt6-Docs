.. _ref-build-system:

The PyQt6 Extension API
=======================

An important feature of PyQt6 (and SIP generated modules in general) is the
ability for other extension modules to build on top of it.
`QScintilla <https://www.riverbankcomputing.com/software/qscintilla/>`__ is
such an example.

PyQt6 provides a C++ extension API that can be used by other modules.  This has
the advantage of sharing code and also enforcing consistent behaviour.


C++ API
-------

The C++ API is a set of functions.  The addresses of each function is obtained
by calling SIP's :c:func:`sipImportSymbol` function with the name of the
function required.

The functions exported by PyQt6 are as follows:

.. cpp:function:: void pyqt6_cleanup_qobjects()

    Call the C++ destructor of any :sip:ref:`~PyQt6.QtCore.QObject` instance
    that is owned by Python (with the exception of any
    :sip:ref:`~PyQt6.QtCore.QCoreApplication` instance).

.. cpp:function:: void pyqt6_err_print()

    A replacement for :c:func:`PyErr_Print` that passes the text of the
    exception and traceback to :c:func:`qFatal`.

.. cpp:function:: char **pyqt6_from_argv_list(PyObject *argv_list, int &argc)

    Convert a Python list to a standard C array of command line arguments and
    an argument count.

    :param argv_list:
        is the Python list of arguments.
    :param argc:
        is updated with the number of arguments in the list.
    :return:
        an array of pointers to the arguments on the heap.


.. cpp:function:: PyObject *pyqt6_from_qvariant_by_type(QVariant &value, PyObject *type)

    Convert a :sip:ref:`~PyQt6.QtCore.QVariant` to a Python object according
    to an optional Python type.

    :param value:
        is the value to convert.
    :param type:
        is the Python type.
    :return:
        the converted value.  If it is ``0`` then a Python exception will have
        been raised.

.. cpp:function:: sipErrorState pyqt6_get_connection_parts(PyObject *slot, QObject *transmitter, const char *signal_signature, bool single_shot, QObject **receiver, QByteArray &slot_signature)

    Get the receiver object and slot signature to allow a signal to be
    connected to an optional transmitter.

    :param slot:
        is the slot and should be a callable or a bound signal.
    :param transmitter:
        is the optional :sip:ref:`~PyQt6.QtCore.QObject` transmitter.
    :param signal_signature:
        is the signature of the signal to be connected.
    :param single_shot:
        is ``true`` if the signal will only ever be emitted once.
    :param receiver:
        is updated with the :sip:ref:`~PyQt6.QtCore.QObject` receiver.  This
        may be a proxy if the slot requires it.
    :param slot_signature:
        is updated with the signature of the slot.
    :return:
        the error state.  If this is :c:data:`sipErrorFail` then a Python
        exception will have been raised.

.. cpp:function:: const QMetaObject *pyqt6_get_qmetaobject(PyTypeObject *type)

    Get the QMetaObject instance for a Python type.  The Python type must be a
    sub-type of :sip:ref:`~PyQt6.QtCore.QObject`'s Python type.

    :param type:
        is the Python type object.
    :return:
        the :sip:ref:`~PyQt6.QtCore.QMetaObject`.

.. cpp:function:: sipErrorState pyqt6_get_pyqtsignal_parts(PyObject *signal, QObject **transmitter, QByteArray &signal_signature)

    Get the transmitter object and signal signature from a bound signal.

    :param signal:
        is the bound signal.
    :param transmitter:
        is updated with the :sip:ref:`~PyQt6.QtCore.QObject` transmitter.
    :param signal_signature:
        is updated with the signature of the signal.
    :return:
        the error state.  If this is :c:data:`sipErrorFail` then a Python
        exception will have been raised.


.. cpp:function:: sipErrorState pyqt6_get_pyqtslot_parts(PyObject *slot, QObject **receiver, QByteArray &slot_signature)

    Get the receiver object and slot signature from a callable decorated with
    :sip:ref:`~PyQt6.QtCore.pyqtSlot`.

    :param slot:
        is the callable slot.
    :param receiver:
        is updated with the :sip:ref:`~PyQt6.QtCore.QObject` receiver.
    :param slot_signature:
        is updated with the signature of the slot.
    :return:
        the error state.  If this is :c:data:`sipErrorFail` then a Python
        exception will have been raised.


.. cpp:function:: sipErrorState pyqt6_get_signal_signature(PyObject *signal, const QObject *transmitter, QByteArray &signal_signature)

    Get the signature string for a bound or unbound signal.  If the signal is
    bound, and the given transmitter is specified, then it must be bound to the
    transmitter.

    :param signal:
        is the signal.
    :param transmitter:
        is the optional :sip:ref:`~PyQt6.QtCore.QObject` transmitter.
    :param signal_signature:
        is updated with the signature of the signal.
    :return:
        the error state.  If this is :c:data:`sipErrorFail` then a Python
        exception will have been raised.


.. cpp:function:: void pyqt6_register_from_qvariant_convertor(bool (*convertor)(const QVariant &, PyObject **))

    Register a convertor function that converts a
    :sip:ref:`~PyQt6.QtCore.QVariant` value to a Python object.

    :param convertor:
        is the convertor function.  This takes two arguments.  The first
        argument is the :sip:ref:`~PyQt6.QtCore.QVariant` value to be
        converted.  The second argument is updated with a reference to the
        result of the conversion and it will be ``0``, and a Python exception
        raised, if there was an error.  The convertor will return ``true`` if
        the value was handled so that no other convertor will be tried.


.. cpp:function:: void pyqt6_register_to_qvariant_convertor(bool (*convertor)(PyObject *, QVariant &, bool *))

    Register a convertor function that converts a Python object to a
    :sip:ref:`~PyQt6.QtCore.QVariant` value.

    :param convertor:
        is the convertor function.  This takes three arguments.  The first
        argument is the Python object to be converted. The second argument is a
        pointer to :sip:ref:`~PyQt6.QtCore.QVariant` value that is updated
        with the result of the conversion.  The third argument is updated with
        an error flag which will be ``false``, and a Python exception raised,
        if there was an error.  The convertor will return ``true`` if the value
        was handled so that no other convertor will be tried.


.. cpp:function:: void pyqt6_register_to_qvariant_data_convertor(bool (*convertor)(PyObject *, void *, int, bool *))

    Register a convertor function that converts a Python object to the
    pre-allocated data of a :sip:ref:`~PyQt6.QtCore.QVariant` value.

    :param convertor:
        is the convertor function.  This takes four arguments.  The first
        argument is the Python object to be converted. The second argument is a
        pointer to the pre-allocated data of a
        :sip:ref:`~PyQt6.QtCore.QVariant` value that is updated with the
        result of the conversion.  The third argument is the meta-type of the
        value.  The fourth argument is updated with an error flag which will be
        ``false``, and a Python exception raised, if there was an error.  The
        convertor will return ``true`` if the value was handled so that no
        other convertor will be tried.


.. cpp:function:: void pyqt6_update_argv_list(PyObject *argv_list, int argc, char **argv)

    Update a Python list from a standard C array of command line arguments and
    an argument count.  This is used in conjunction with
    :cpp:func:`pyqt6_from_argv_list` to handle the updating of argument lists
    after calling constructors of classes such as
    :sip:ref:`~PyQt6.QtCore.QCoreApplication`.

    :param argv_list:
        is the Python list of arguments that will be updated.
    :param argc:
        is the number of command line arguments.
    :param argv:
        is the array of pointers to the arguments on the heap.
