# Documentation

* * *

## Authorization

After you received your API key you can start using this API. To get access you have to add a HTTP Authorization header to each of your requests:

    Authorization: YOUR_API_KEY


* * *

## Get chapters list
    

    https://api-ipc.herokuapp.com/api/v1/chapter

If the request is successful, the response body will be a JSON with the following data:

    {  
    "data":{  
       "result":[{  
             "from":"1 to 5",
             "number":"I",
             "title":"Introduction"
          },[(NEXT CHAPTERS)]],
      "message":"OK: Authorized"
      }
    }
>from: x-chapter containing sections

>number: Chapter number

>title	: Title/heading of the chapter
* * *

## Get sections list

    https://api-ipc.herokuapp.com/api/v1/section

You can get all sections list with it.  
If the request is successful, the response body will be a JSON with the following data:

    {  
       "data":{  
          "result":[{  
                "chapter":"I",
                "number":"1",
                "title":"Title and extent of operation of the Code."
             },[(NEXT SECTIONS)]]
       },
       "message":"OK: Authorized"
    }



>number	: x-section number

>chapter:	from Which chapter x-section belongs to

>title	: title of the x-section section

## Getting an specific chapter

    https://api-ipc.herokuapp.com/api/v1/chapter/<chapter-number>

><chapter-number>: 	chapter number without " < > "

You can get informations about a specific chapter with it.  
If the request is successful, the response body will be a JSON with the following data:

    {  
       "data":{  
          "description":"Introduction",
          "from":"1 to 5",
          "number":"I",
          "result":[{  
                "number":"1",
                "title":" Title and extent of operation of the Code...."
          },[(NEXT SECTIONS)]]
       },
       "message":"OK: Authorized"
    }



>description	: description about the chapter

>from:	chapter containing sections

>Number :	chapter number

>result[x]['number'] :	x-section number

>result[x]['title'] : x-section title

## Getting a specific section

	https://api-ipc.herokuapp.com/api/v1/section/<section-number>
<table>

><section-number>	: section number without " < > "

You can get informations about a specific section with it.  
If the request is successful, the response body will be a JSON with the following data:

	{  
	  "data":{ 
 	     "number":"1",
 	     "title":"Title and extent of operation of the Code"
   	     "result":[{  
               "chapter":"I",
         	   "from":"1 to 5"
         	   "chap-tilte":"Introduction"
             "text":"This Act shall be called the ..."
          },[(NEXT SECTIONS)]]
        },
      "message":"OK: Authorized"
    }


>number:	Section number

>title	: section title

>chapter	:chapter number from which x-section belongs to

>chap-title	:chapter title from which x-section belongs to

>text	:section main-text

* * *

## Search

	https://api-ipc.herokuapp.com/api/v1/search/<query>

><query>: search query without " < > "


You can search about any topic related to IPC with it.  
If the request is successful, the response body will be a JSON with the following data:

    {  
       "data":{  
       "q":"Title and extent",
       "result":[{  
                 "chapter":"I",
                 "number":"1",
                 "title":"Title and extent of operation of the Code"
            },[(NEXT RESULTS)]]
           },
       "message":"OK: Authorized"
    }

>q	:your search query

>chapter:	from Which chapter search result belongs to

>number :	from Which section search result belongs to

>title:	title of your search result

* * *

## Request statistics

To see how many requests you have left in this current period, you can look at the HTTP response header called "X-Ratelimit-Remaining" that comes with every response you receive.

## Try it out

    $ curl -H "Authorization: YOUR_API_KEY" "https://api-ipc.herokuapp.com/api/v1/section/370"</pre>

* * *

## Disclaimer

We don't have an uptime or availability guarantee. Some features may change in the future.

## Contact

If you have any question or feedback write me to [@NikkyAmresh](https://m.me/NikkiAmresh).

>Developer [@NikkyAmresh](https://m.me/NikkiAmresh)

