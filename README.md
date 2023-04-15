# Web_Server
A web server that handles one HTTP request at a time. It accept and parse the HTTP request, get the requested file from the server’s file system, create an HTTP response message consisting of the requested file preceded by header lines, and then send the response directly to the client. If the requested file is not present in the server, the server send an HTTP “404 Not Found” message back to the client.

ADDITIONAL
<h3>ADDITIONAL</h3>
Instead of using a browser, this is an HTTP client to test your server. Your client will connect to the server using a TCP connection, send an HTTP request to the server, and display the server response as an output. We can assume that the HTTP request sent is a GET method. The client takes command line arguments specifying the server IP address or hostname, the port at which the server is listening, and the path at which the requested object is stored at the server.
