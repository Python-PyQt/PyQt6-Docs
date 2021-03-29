.. sip:enum-description::
    :status: todo
    :digest: 5fc929893a9a80549fe5385298a1cd0a

Numerical values in a database can have precisions greater than their corresponding C++ types. This enum lists the policies for representing such values in the application.

Note: The actual behaviour if an overflow occurs is driver specific. The Oracle database just returns an error in this case.
