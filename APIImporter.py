import time
import requests

# ---------------------------------------------------------------------------- #
#                                 HTML Importer                                #
# ---------------------------------------------------------------------------- #

def ServiceTest(Address): #Take an adress and either returns the status code
    s = requests.get(Address)
    status = s.status_code
    return (status)

def StatusCodeMeaning(StatusCode):#Takes a HTML status code and returns a string describing it
    Codes = [100,101,102,103,200,201,202,203,204,205,206,207,208,226,300,301,302,303,304,305,307,308,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,421,422,423,424,426,428,429,431,451,500,501,502,503,504,505,506,507,508,510,511]
    Description = ["100-Continue: The Request is functioning and more data should be given","101-Switching Protocol: The Server is switching protocol","102-Processing: The server has recieved the request and is processing it.","103-Early Hints: User-agent can preload resources while the server responds","200-OK: Request has been succesful","201-Created:Request sucessful and a resource has been created","202-Accepted:Request Recieved, but no action has been taken yet.","203-Non-Authoritative Information: Request fufilled from a local/thrid-party server","204-No Content: No content, but only headers","205-Reset Content: User should reset the document that sent the request","206-Partial Content: Succefully sent the designated section of data","207-Multi-Status: Shows info about multiple resources","208-Already Reported: Used with <dav:propstat> to avoid an error","209-IM Used: Server fulfilled a GET request and is the represenation of multiple instance-manipulations","300-Multiple Choice: There are multiple Response and the user should choose one","301-Moved Permanently: The URL for this resource has been changed. A new URL is given","302-Found: The URI for this resource has been temporarily moved.","303-See Other: A alternative URI is sent as a result of the GET request","304-Not Modified:The response has not changed, client should used the current version","305-Use Proxy: Server requests you use a proxy for security reasons","307-Temporary Redirect: Server wants to redirect client to the requested resource at another URL wit the same HTTP method","308-Permanent Redirect: resource is pemenantly located at another URI (Described with Location:Header)with the same HTTP method","400-Bad Request: The server could not understand due to bad syntax","401-Unauthoriszed: The client is unauthenticated, client must authenticate to recieve a response","402-Payment Required: Currently is unused and has no standard convention","403-Forbidden: Cleint identity is know and has been denied due to lack of clearance","404-Not Found: Server can not find resource (Hidden resources may return 404)","405-Method Not Allowed: Request method is know but disabled (e.g. DELETE) GET and HEAD should never return this","406-Not Acceptable: No content that conforms to the give criteria","407-Proxy Authentication Required: The client must authenticate through a proxy","408-Request Timeout: Server has gone idle and shut down.","409-Conflict: Requests conflicts with current server state","410-Gone: The requests content is permanently deleted Cleint expedted to remove links/caches","411-Length Required: Server rejected requests beacuse the Content-Length header iss not defined","412-Precondition Failed: The client indicatied pre-conditions in the headers which the server does meet","413-Payload Too Large: Requests is larger than the limits defined by the server","414-URI Too Long: The URI requested by the client is longer than the server will interperet","415-Unsupported Media Type: The media format requested is not supported by the server","416-Range Not Satisfiable: The Range header can't be fufilled, might be outside size of the target URI's data","417-Expectation Failed: The server couldn't fufill Expect header","418-I'm a teapot: Server won't brew coffee with tea","421-Misdirected Request: The request was not ale to produce a reponse. This can be a server fault.""422-Unprocessable Entity: Request was well-formed unabled to be followed due to semantic errors","423-Locked: Resource that is being accessed is locked","424-Failed Dependency: Request failed due to prevous request","425-Too Early: Server is unwilling to risk processing a request that would be replayed","426-Upgrade Required: THe server refused request on current protocol, use Upgrade header to get correct protocol","428-Precondition Required: The orgin required the request to be conditional","429-Too Many Requests: Server has sent too many requests in a space of time","431-Request Header Fields Too Large: Server is unwilling to complete request because header is too large","451-Unavailable For Legal Reasons: Resource cannot legally be provided","500-Internal Server Error: Server fucked up","501-Not Implemented: Request method not supported","502-Bad Gateway: Error response got an invalid response from another server","503-Service Unavailable: The server is temporarily down use Retry-After:","504-Gateway Timeout: The server timed out from third-party","505-HTTP Version Not Supported: The HTTP version used is not supported","506-Variant Also Negotiates: Server has internal config error","507-Insufficient Storage: Server cannot store the representation of the request","508-Loop Detected: Server detected infinite loop while processing","510-Not Extended: Further extentiosn to the requests are required","511-Network Authentication Required: Client needs to authenticate to gain network access"]

    for x in range(61): #There are 61 status codes
        if StatusCode == Codes[x]:
            return Description[x]
    return ("Invalid Status Code")

def RefreshConnection(Address):#Take an adress
    s = requests.get(Address)
    return s

# ---------------------------------------------------------------------------- #
#                                Fact Generator                                #
# ---------------------------------------------------------------------------- #

def GenerateFact():
    if ServiceTest("https://uselessfacts.jsph.pl//random.txt?language=en") == 200:
        r = RefreshConnection("https://uselessfacts.jsph.pl//random.txt?language=en")
        Fact = r.text
        if (Fact) != 'Too Many Attempts.':
            return Fact
    else:  
        return ("Too Many Requests\nPlease Wait")