"""
HTTPRouter using a Trie

For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the Trie data structure we learned previously.

There are many different implementations of HTTP Routers such as regular expressions or simple string matching,
but the Trie is an excellent and very efficient data structure for this purpose.

The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return.
In a dynamic web server, the content will often come from a block of code called a handler.

First we need to implement a slightly different Trie than the one we used for autocomplete.
Instead of simple words the Trie will contain a part of the http path at each node, building from the root node /

In addition to a path though, we need to know which function will handle the http request.
In a real router we would probably pass an instance of a class like Python's SimpleHTTPRequestHandler
which would be responsible for handling requests to that path.
For the sake of simplicity we will just use a string that we can print out to ensure we got the right handler

We could split the path into letters similar to how we did the autocomplete Trie,
but this would result in a Trie with a very large number of nodes and lengthy traversals if we have a lot of pages on our site.
A more sensible way to split things would be on the parts of the path that are separated by slashes ("/").
A Trie with a single path entry of: "/about/me" would look like:

(root, None) -> ("about", None) -> ("me", "About Me handler")

We can also simplify our RouteTrie a bit by excluding the suffixes method and the endOfWord property on RouteTrieNodes.
We really just need to insert and find nodes, and if a RouteTrieNode is not a leaf node,
it won't have a handler which is fine.

"""



# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler="root handler", not_found_handler="404 - Page not found"):
        self.root = RouteTrieNode(handler)
        self.not_found_handler = not_found_handler

    def insert(self, newpage, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        newpage = newpage.split("/")
        try:
            newpage.remove('')
            newpage.remove('')
        except ValueError:
            pass
        current_node = self.root

        for directory in newpage:
            if directory not in current_node.children:
                current_node.insert(directory)
            current_node = current_node.children[directory]

        current_node.handler = handler

    def find(self, url):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        url = url.split("/")
        try:
            url.remove('')
            url.remove('')
        except ValueError:
            pass

        if len(url) == 0:
            return self.root.handler
        current_node = self.root
        for directory in url:
            if directory not in current_node.children:
                return self.not_found_handler
            current_node = current_node.children[directory]

        return current_node.handler



# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = None):
        self.children = {}
        self.handler = handler

    def insert(self, page, handler = None):
        self.children[page] = RouteTrieNode(handler)


## some initial testing:
mypage = RouteTrie()
mypage.insert("about","about handler")
mypage.insert("about/me", "me handler")

mypage.find("about/me")
mypage.find("about")


"""
Next we need to implement the actual Router.
The router will initialize itself with a RouteTrie for holding routes and associated handlers.
It should also support adding a handler by path and looking up a handler by path.
All of these operations will be delegated to the RouteTrie.
Hint: the RouteTrie stores handlers under path parts, so remember to split your path around the '/' character
Bonus Points: Add a not found handler to your Router which is returned whenever a path is not found in the Trie.
More Bonus Points: Handle trailing slashes! A request for '/about' or '/about/' are probably looking for the same page.
Requests for '' or '/' are probably looking for the root handler. Handle these edge cases in your Router.
"""

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler=None, not_found_handler = None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.RouteTrie = RouteTrie(handler, not_found_handler)

    def add_handler(self, path, handler):
        self.RouteTrie.insert(path, handler)

    def lookup(self, url):
        return self.RouteTrie.find(url)








## Test case 1: From the problem set
# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

## Test case 2: An empty input
router = Router()
router.add_handler("/home/about", "about handler")  # add a route
print(router.lookup("/home/about"))
# 'about handler'
print(router.lookup("/home/notapage"))
# None

## Test case 3: Subsequently adding depth
router = Router()
router.add_handler("/home", "home handler")
router.add_handler("/home/about", "about handler")
router.add_handler("/home/about/me", "me handler")  # add a route
print(router.lookup("/home/about"))
# 'about handler'
print(router.lookup("/home/about/me"))
# me handler
print(router.lookup("/home/"))
# home handler












