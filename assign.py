

def retrieve_user_data():
    return 1,2,3,4,5


ENV, SUB_ENV, REGION, QUALIFIED_ENV = retrieve_user_data()


print "VARS ", ENV, SUB_ENV, REGION, QUALIFIED_ENV