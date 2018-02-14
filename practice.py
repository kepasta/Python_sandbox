import time
import pymongo
import dtppl

m = pymongo.MongoClient()


i = 0
m.tests.insertTest.update(
    { "Method name" : "Juni" },
    {
      $set: { "cuisine": "American (New)" },
      $currentDate: { "lastModified": true }
    }
)

while (i < 50):

    doc = dtppl.pack(dtppl.appname, dtppl.methname, dtppl.message)

    start = time.time()
    m.tests.insertTest.insert(doc, manipulate=False, w=1)
    end = time.time()

    executionTime = (end - start) * 1000 # Convert to ms

    print(executionTime)

    i = i + 1
j = 0
k = 0
l = 0
for i in string:
    if i = ' ':
        if k = 0:
            year = int(string[:j])
            l = j + 1
        elif k = 1:
            month = int(string[l:j])
            l = j + 1
        elif k = 2:
            day = int(string[l:j])
            l = j + 1
        elif k = 3:
            hour = int(string[l:j])
            l = j + 1
        elif k = 4:
            minute = int(string[l:j])
            l = j + 1
        elif k = 5:
            second = int(string[l:j])
            l = j + 1
        else:
            ms = int(string[l:len(string)])
        k +=1
    j += 1
