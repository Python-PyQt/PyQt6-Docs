.. sip:enum-description::
    :status: todo
    :digest: c862248924d658baefa7fbc84e4448cd

Use this enum for JavaScript language-specific types of Error objects.

They may be useful when emulating language features in C++ requires the use of specialized exception types. In addition, they may help to more clearly communicate certain typical conditions, instead of throwing a generic JavaScript exception. For example, code that deals with networking and resource locators may find it useful to propagate errors related to malformed locators using the URIError type.
