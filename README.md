# IMVU CDN Direct Data Access

## Reasons and Questions

### Why I did this?
- IMVU has had this same bug exist since they started using there http://userimages-akm.imvu.com

### What does this exploit do?
- This exploit allows a attacker to gain access to _any_ product on IMVUs CDN, and by gain access I mean they can download the contents of the product and simply recreate the CHKN (Fancy Zip File)quite easily.

### Why hasn't this been patched by IMVU Int yet?
- IMVU is fully aware this bug has existed for years in there system things like IMVU T3DE and other have completely exploited this bug to allow people to steal meshes and textures form creators.

### Why did you upload a fully working POC code for this?
- I uploaded code with this write up because I want creators and others to see just how simple it is to exploit this system I did this exploit in 30 mintues and only using 66 lines of python 2.7 code. 

## Detail data on how this works

IMVU uses the following domain for content creator's data that they created
``
http://userimages-akm.imvu.com
``

This URl has a few options that we can use to exploit in order to get the latest version of any product on IMVU those params are as follows: ``http://userimages-akm.imvu.com/productdata/``{PID}``/``{Revision}``/``{Filename}

- _Filename_: This is the actual file name from the ``_contents.json`` file that every product is given server side you can get this by using ``http://userimages-akm.imvu.com/productdata/39/8/_contents.json``
- _PID (Product ID)_: This is the shop ID given to the product by IMVUs database
- _Revision_: The current revision of the product in are test we check for 100 different revisions

## Minor things regrading this exploit
This exploit abuses a bug in which I have reported to IMVU Inc ages ago and have given them many ideas to patch this bug... This bug has been partially patched thank to IMVU Next (But only partially patched for Next)

This bug exist because IMVU refuses to use any form of validation on there end to make sure your on the client or using a valid session from there WebSocket System (Next) or there XML-RPC (Desktop Client)

## How can this be fixed
There is many ways IMVU Inc can patch this flaw in there system I will list a few below:

- Remove direct file access 
    - This goes hand and hand, by removing Direct File access they could serve the files as a Json encode string from a PHP file or a socket server and then use session validation and other means to make it much harder to exploit this system
- Disable the destkop client completely and move everything to IMVU Next as this bug doesn't fully exist in Next and it seems they already partially started patching it in later builds of Next.
