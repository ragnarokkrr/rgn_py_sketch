def nesting():
    count = [0]

    def nested():
        for j in range(2):
            try:
                count[0] += 1
            except:
                print "nois"

    for i in range(10):
        nested()
    print count[0]


nesting()
