**********
Quickstart
**********

Installing
**********

To get started with ``httpsuite``, install the latest stable release from
`PyPi <https://pypi.org/project/httpsuite/>`_:

.. code-block:: bash

  pip install httpsuite


If you would like to use the latest non-stable release, you may install directly
from Github:

.. code-block:: bash

  pip install git+https://github.com/synchronizing/httpsuite

Getting Started
***************

There are two main abstractions that ``httpsuite`` provides, ``Request`` and
``Response``. Both provide an interface to interpret, modify, and compile
raw HTTP messages.

.. code-block:: python

  from httpsuite import Request, Response

You may either chose to initialize them via their ``__init__`` methods:

.. code-block:: python

  request = Request(
      method="GET",
      target="/",
      protocol="HTTP/1.1",
      headers=None,
      body=None
  )

  response = Response(
      protocol="HTTP/1.1",
      status=200,
      status_msg="OK",
      headers=None,
      body=None
  )

Or, parse them from raw HTTP messages via their ``parse()`` method:

.. code-block:: python

  request = Request.parse(b'GET / HTTP/1.1\r\n\r\n')
  response = Response.parse(b'HTTP/1.1 200 OK\r\n\r\n')

Once you have initialized a ``Request`` or ``Response`` message, you can modify
and then compile.

Modifying Messages
******************

Modifying ``Request`` or ``Response`` objects is done as one would expect:

.. code-block:: python

  request.method = "POST"
  response.status = b"300"
  response.status_msg = b"Continue"

Notice, however, that setting a ``Request`` or ``Response`` value is type-agnostic.
In other words, it does not matter if you set a piece of data as a ``str``,
``bytes``, or ``int``. Similarly, comparisons are type-agnostic:

.. code-block:: python

  request.status == 300     # True
  request.status == "300"   # True
  request.status == b"300"  # True

Compiling Message
*****************

After modifying the message, the final step is to compile the message. Compiling
is simply translating our object from Python to bytes (following specific rules),
so that another computer on the internet can understand us. One does this by calling
the property ``raw``:

.. code-block:: python

  body = json.dumps({"hello": "world"})
  request = Request(
      method="POST",
      target="/post",
      protocol="HTTP/1.1",
      headers={
          "Host": "httpbin.org",
          "Connection": "close",
          "Content-Length": len(body),
          "Accept": "*/*",
      },
      body=body,
  )

  print(request.raw)

.. code-block:: python

  b'POST /post HTTP/1.1\r\nHost: httpbin.org\r\nConnection: close\r\nContent-Length: 18\r\nAccept: */*\r\n\r\n{"hello": "world"}'

Example
*******

A simple example of using ``httpsuite`` with sockets to send our message above:

.. literalinclude:: ../../../examples/example_sockets.py
   :language: python
   :linenos:
