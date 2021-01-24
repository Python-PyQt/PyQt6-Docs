Things to be Aware Of
=====================

TLS Support
-----------

Support for Transport Layer Security (TLS) is increasingly important,
particularly on mobile platforms where an application is typically a front end
to a cloud-based server.  As both Python and Qt implement different APIs that
support TLS, a PyQt application has a choice as to which to use.  This is
particularly important when deploying an application as the support may have to
be included with, or built into, the application itself.

Ideally the TLS implementation provided by the target would be used (e.g.
CryptoAPI on Windows, Secure Transport on macOS and iOS).  This would mean that
security updates, including certificate updates, would be handled by the vendor
of the target operating system and could be ignored by the application.
Unfortunately there is no common TLS API.  The resolution to this problem is
the subject of `PEP 543 <https://www.python.org/dev/peps/pep-0543>`__ but that
has yet to be implemented.

Python uses OpenSSL as its TLS implementation.  Python v3.7.4 and later use
OpenSSL v1.1.1.  Python v3.7.0 to v3.7.3 use OpenSSL v1.1.0.  Earlier versions
of Python use OpenSSL v1.0.2.  On Windows and macOS the standard Python binary
installers include copies of the corresponding OpenSSL libraries.

Qt has support for the native TLS implementation on macOS and iOS but on other
platforms (except for Linux) a deployed application must include it's own
OpenSSL implementaion.


Crashes On Exit
---------------

When the Python interpreter leaves a *scope* (for example when it returns from
a function) it will potentially garbage collect all objects local to that
scope.  The order in which it is done is, in effect, random.  Theoretically
this can cause problems because it may mean that the C++ destructors of any
wrapped Qt instances are called in an order that Qt isn't expecting and may
result in a crash.  However, in practice, this is only likely to be a problem
when the application is terminating.

As a way of mitigating this possiblity PyQt6 ensures that the C++ destructors
of any :sip:ref:`~PyQt6.QtCore.QObject` instances owned by Python are invoked
before the destructor of any :sip:ref:`~PyQt6.QtCore.QCoreApplication` instance
is invoked.  Note however that the order in which the
:sip:ref:`~PyQt6.QtCore.QObject` destructors are invoked is still random.


Keyword Arguments
-----------------

PyQt6 supports the use of keyword arguments for optional arguments.  Although
the PyQt6 and Qt documentation may indicate that an argument has a particular
name, you may find that PyQt6 actually uses a different name.  This is because
the name of an argument is not part of the Qt API and there is some
inconsistency in the way that similar arguments are named.  Different versions
of Qt may use a different name for an argument which wouldn't affect the C++
API but would break the Python API.

The docstrings that PyQt6 generates for all classes, functions and methods will
contain the correct argument names.


Garbage Collection
------------------

C++ does not garbage collect unreferenced class instances, whereas Python does.
In the following C++ fragment both colours exist even though the first can no
longer be referenced from within the program::

    col = new QColor();
    col = new QColor();

In the corresponding Python fragment, the first colour is destroyed when the
second is assigned to ``col``::

    col = QColor()
    col = QColor()

In Python, each colour must be assigned to different names.  Typically this is
done within class definitions, so the code fragment would be something like::

    self.col1 = QColor()
    self.col2 = QColor()

Sometimes a Qt class instance will maintain a pointer to another instance and
will eventually call the destructor of that second instance.  The most common
example is that a :sip:ref:`~PyQt6.QtCore.QObject` (and any of its
sub-classes) keeps pointers to its children and will automatically call their
destructors.  In these cases, the corresponding Python object will also keep a
reference to the corresponding child objects.

So, in the following Python fragment, the first
:sip:ref:`~PyQt6.QtWidgets.QLabel` is not destroyed when the second is
assigned to ``lab`` because the parent :sip:ref:`~PyQt6.QtWidgets.QWidget`
still has a reference to it::

    parent = QWidget()
    lab = QLabel("First label", parent)
    lab = QLabel("Second label", parent)


Multiple Inheritance
--------------------

It is not possible to define a new Python class that sub-classes from more than
one Qt class.  The exception is classes specifically intended to act as mixin
classes such as those (like :sip:ref:`~PyQt6.QtQml.QQmlParserStatus`) that
implement Qt interfaces.


Access to Protected Member Functions
------------------------------------

When an instance of a C++ class is not created from Python it is not possible
to access the protected member functions of that instance.  Attempts to do so
will raise a Python exception.  Also, any Python methods corresponding to the
instance's virtual member functions will never be called.


``None`` and ``NULL``
---------------------

Throughout PyQt6, the ``None`` value can be specified wherever ``NULL`` is
acceptable to the underlying C++ code.

Equally, ``NULL`` is converted to ``None`` whenever it is returned by the
underlying C++ code.


Support for ``void *``
----------------------

PyQt6 (actually SIP) represents ``void *`` values as objects of type
:py:class:`~PyQt6.sip.voidptr`.  Such values are often used to pass the
addresses of external objects between different Python modules.  To make this
easier, a Python integer (or anything that Python can convert to an integer)
can be used whenever a :py:class:`~PyQt6.sip.voidptr` is expected.

A :py:class:`~PyQt6.sip.voidptr` may be converted to a Python integer by using
the :py:func:`int` builtin function.

A :py:class:`~PyQt6.sip.voidptr` may be converted to a Python string by using
its :py:meth:`~PyQt6.sip.voidptr.asstring` method.  The
:py:meth:`~PyQt6.sip.voidptr.asstring` method takes an optional integer
argument which is the length of the data in bytes.

A :py:class:`~PyQt6.sip.voidptr` may also be given a size (i.e. the size of the
block of memory that is pointed to) by calling its
:py:meth:`~PyQt6.sip.voidptr.setsize` method.  If it has a size then it is also
able to support Python's buffer protocol and behaves like a Python
:py:class:`memoryview` object so that the block of memory can be treated as a
mutable list of bytes.  It also means that the Python :py:mod:`struct` module
can be used to unpack and pack binary data structures in memory, memory mapped
files or shared memory.
