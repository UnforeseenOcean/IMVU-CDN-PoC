import urllib2
import json
import os
import sys
import zipfile

maxRev = 100

def createCHKN(pid, path):
    ziph = zipfile.ZipFile("{0}".format(pid), "w", zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), file)

    ziph.close()

def requestContent(url):
    req = urllib2.Request(url)
    try:
        resp = urllib2.urlopen(req)
    except urllib2.HTTPError as e:
        return False
    else:
        # 200
        return resp.read()

def getOutputFolder(pid):
    if not os.path.exists("./output/{0}/".format(pid)):
        os.makedirs("./output/{0}/".format(pid))

    return "./output/{0}/".format(pid)

def getIMVUUrl(pid):
    currentRev = 1
    lastUrl = False
    lasContent = False
    lastRevision = False

    while (currentRev <= maxRev):
        url = "http://userimages-akm.imvu.com/productdata/{0}/{1}/_contents.json".format(pid, currentRev)
        content = requestContent(url)
        if content:
            lastUrl = url
            lastRevision = currentRev
            lasContent = content

        if not content:
            if lastUrl and lasContent and lastRevision:
                break

        currentRev = currentRev + 1
    
    return lastUrl, "http://userimages-akm.imvu.com/productdata/{0}/{1}/".format(pid, lastRevision), lasContent, lastRevision


def main(pid):
    contentsurl, baseurl, content, revision = getIMVUUrl(pid)

    if not contentsurl:
        print "Max revisions testing reached for PID {0}".format(pid)
        return
    
    saveFolder = getOutputFolder(pid)
    json_data = json.loads(content)

    productList = {}
    productList["_contents.json"] = contentsurl
    for item in json_data:
        if "url" in item:
            productList[item["name"]] = "{0}{1}".format(baseurl, item["url"])
            continue
        productList[item["name"]] = "{0}{1}".format(baseurl, item["name"])

    for key, value in productList.iteritems():
        savePath = "{0}{1}".format(saveFolder, key)
        contents = requestContent(value)

        if not contents:
            continue

        with open(savePath, "wb") as file:
            file.write(contents)

        print "Saved file contents for {0}".format(key)

    createCHKN("./output/{0}.chkn".format(pid), saveFolder)
    print "Created CHKN file at {0}".format("./output/{0}.chkn".format(pid))


main(sys.argv[1])
