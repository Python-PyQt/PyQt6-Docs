Support for Old Versions of Python
==================================

Begining with PyQt v5.13 a formal policy for the support for older versions of 
Python v3 has been adopted.

When a Python version reaches it's end-of-life, support for it will be removed
in the next minor release of PyQt.  For example, if the current version of PyQt
is v5.x.y then the support will be removed in v5.x+1.0.  Specifically, PyQt
v5.13 will remove support for Python v3.0, v3.1, v3.2, v3.3 and v3.4.

Support for Python v2 is handled slightly differently.  Support for Python v2
is determined by the version of SIP being used.  PyQt will no longer support
Python v2 when SIP v6 is released (at which point SIP v4 will become
unsupported).
