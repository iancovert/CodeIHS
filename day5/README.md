# Day 5

We'll discuss the internet, how websites work, and the concept of servers. Once we establish the basics of how users visit websites, we'll give a demonstration of Flask (a Python framework) that makes it easy to deliver websites.

## Web pages

A web page (what you see at Facebook.com or Google.com) is displayed thanks to code written by the creators of those websites.

Websites almost always involve multiple files, and code written in multiple languages. The basic structure and content of the page is written in **HTML** (hypertext markup language), the style (sizes, colors, fonts) are written in **CSS** (cascading stylesheets), and interactivity (what happens when you click a button) is controlled by **Javascript**.

## Computer networks

We all know that computers communicate with one another over the internet. Let's discuss how this works.

Imagine a graph containing nodes and edges, where each computer is a node, and computers connected by an edge can communicate with one another. If such a system is designed properly, any computer in the graph can communicate with any other computer in the graph, *even without a direct connection*, because its messages can be forwarded from one computer to the next.

This is basically how computer networks work. The edges connecting computers can work in different ways. Your computer is probably connected to a device through WiFi, but it could also be connected using an ethernet cable. 

Most communications over computer networks eventually go through physical cables. There are different kinds of physical cables, and some modern ones are built to transmit information very quickly – nearly at the speed of light. Don't be fooled by the fact that you only ever deal with WiFi: physical cables are an essential part of how computer networks function. 

## The internet

To visit a website, you simply write the URL into the address bar of your browser. How does this really work?

We'll walk you through a slightly simplified picture of what happens when you visit a website.

### Servers

A *web server* is a computer connected to the internet, whose job is to wait for other computers to request some content. Computers making requests are called clients. 

When those other computers make requests, the server responds by sending what the client requested, like the files necessary to display a website.

### Domain names

A *domain name* is something like google.com. For the casual user, it's sufficient to know a website's domain name. But how is it that your computer figures out how to locate the server responsible for delivering the website's files?

When you type a domain name into your browser, your browser contacts a nearby *DNS server* (domain name service), which translates the domain name to an IP address. An IP address looks something like this: 

    172.217.6.46

### IP addresses

Every computer connected to the internet has an *IP address*. Think of this like a physical mailing address: when you want to send someone mail, you need to know their address. The name of their neighborhood (our anology for the website's domain name) does not give a precise sense of their location.

### Port numbers

Each computer connected to the internet has a single IP address, but many *port numbers*. Think of this as an apartment number. The IP address is like the building address for where you want to send your mail, but you must indicate who exactly within the apartment building should receive the mail.

Generally, the port number is used to indicate which application should see the data. Website-related communications have their own port number, as does email, various services operated by companies (AOL, Microsoft, Apple), etc. The port number used by the protocol for sending and delivering websites is 80.

### Application protocols

Now that you have domain names, IP addresses and port numbers, you essentially have a way to transmit communications to any computer on the internet. Now, how do you ask the server for a website?

A *application protocol* gives a precise pattern for how two computers should interact with one another for a certain application. There are precise protocols that dictate how clients should make requests to servers.

There's a specific pattern of communication that's used for website-related requests, called **HTTP** (hypertext transfer protocol). Basically, the client sends a request to the server, and the server responds by sending the relevant files. This kind of request from the client is called an *HTTP get request*.

A request might look like this:

```
GET /index.html HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)
Accept-Language: en-us
```

For our purposes, focus on the first line. It says what kind of request this is (get) and which file is being requested (index.html).

### Putting it all together

When you try to visit google.com, the following things happen:

- Type google.com into URL bar
- Browser communicates with nearby DNS server to translate the domain name into an IP address
- Browser sends requests to the appropriate server (using the correct IP address and port number), formatted according to HTTP rules
- Server responds to your computer by sending the appropriate files
- Browser renders the website using all the files retreived from the server

## Making our own website

To make a website means not only creating the code that instructs the browser how to display the web page, but creating a server that delivers those files to users who request them.

Luckily, there are tools available that make this very easy. Flask is one of them, and it's written in Python.

### Flask demonstrations

We demonstrate the following:

- Responding to a request with raw text
- Responding to a request with a simple HTML file
- Responding to a request with an HTML file with inline CSS stylesheet