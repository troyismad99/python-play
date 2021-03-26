import time
print(time.ctime())

def show_default(arg=time.ctime()):
    print(arg)

show_default()
time.sleep(2)
show_default()
time.sleep(2)
show_default()

# always the same time
# default is evaluated once the first time called
# 

def show_defaultFIX(arg=None):
    if arg is None:
        arg = time.ctime()
    print(arg)

show_defaultFIX()
time.sleep(2)
show_defaultFIX()
time.sleep(2)
show_defaultFIX()
